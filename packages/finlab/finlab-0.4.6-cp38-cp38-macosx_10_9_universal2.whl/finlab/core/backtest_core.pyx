# distutils: language=c++
import cython
cimport cython
cimport numpy as np
import numpy as org_np
from finlab.core.mae_mfe cimport *
from finlab.core import mae_mfe
from finlab.core import aes
from libcpp.map cimport map as map
from libcpp.set cimport set
from libcpp.vector cimport vector
from libc.math cimport isnan
from libcpp.string cimport string
from libcpp cimport bool
from cython.operator import dereference, postincrement
import datetime

cdef dict stock_operations = {}

cpdef dict get_stock_operations():
    global stock_operations
    return stock_operations.copy()

def normalize_weight(weights, position_limit):

    weight_sum = 0.0

    for sid, w in weights.items():
        weight_sum += abs(weights[sid])

    for sid in weights:
        if weight_sum > 1:
            weights[sid] *= 1/weight_sum

    for sid in weights:
        if weights[sid] > position_limit:
            weights[sid] = position_limit
        elif weights[sid] < -position_limit:
            weights[sid] = -position_limit

    return weights

cdef double set_position(map[int, double] &p, int sid, double position, double cash, 
                       double fee_ratio, double tax_ratio, bool check_null=True, bool set_null=False, balance=1):

  exist =  p.find(sid) != p.end()  if check_null else True
  
  # check record is need
  if position == 0 and p.find(sid) != p.end() and p[sid] != 0:
    record_exit(sid)
  
  if position != 0 and (p.find(sid) == p.end() or p[sid] == 0):
    record_entry(sid, position/balance)
  
  # fast calculation when position is zero
  if position == 0:
    if exist:
      cash += p[sid] - abs(p[sid]) * (fee_ratio + tax_ratio)
      if set_null:
        p.erase(sid)
      else:
        p[sid] = 0
    return cash
  
  if not exist:
    p[sid] = 0

  amount = position - p[sid]
  buy = amount > 0
  is_entry = (position >= 0 and amount > 0) or (position <= 0 and amount < 0)
  cost = abs(amount) * fee_ratio if is_entry else abs(amount) * (fee_ratio + tax_ratio)
    
  if buy:
    cash -= amount
    p[sid] += amount - cost
  else:
    amount = -amount
    cash += amount - cost
    p[sid] -= amount
    
  if set_null and p[sid] == 0:
    p.erase(sid)
  
  return cash

cdef double rebalance(map[int, double] &p, np.ndarray[np.float64_t, ndim=1] newp, double cash, double fee_ratio, double tax_ratio, double position_limit):
  
  # calculate total balance b1
  cdef double balance = cash
  
  cdef map[int, double].iterator it = p.begin()
  while it != p.end():
    balance += dereference(it).second
    postincrement(it)
    
  cdef double v1
  cdef double v2
  
  cdef double ratio = balance / max(org_np.abs(newp).sum(), 1)
  if isnan(ratio):
    ratio = 1

  # buy_stocks
  cdef double check_cash = 0
  for sid, v in enumerate(newp):
    
    v2 = v * ratio
    if abs(v2) > balance * position_limit:
      sign = (v2 > 0) *2 - 1
      v2 = balance * position_limit * sign

    cash = set_position(p, sid, v2, cash,
              fee_ratio=fee_ratio, tax_ratio=tax_ratio, 
              check_null=True, set_null=True, balance=balance)
  
  return cash

cdef map_columns(price_columns, pos_columns):
  cdef map[string, unsigned] v
  for i, n in enumerate(price_columns):
    v[n.encode('UTF-8')] = i
  
  cdef map[unsigned, unsigned] ret
  cdef string nn
  for i, n in enumerate(pos_columns):
    nn = n.encode('UTF-8')
    if v.find(nn) != v.end():
      ret[i] = v[nn]
  return ret

cpdef ioft(v):
  dd = datetime.datetime.fromtimestamp(v / 1e9)
  return dd

cpdef np.ndarray[np.float64_t] backtest_(

  # 收盤價等的數值，通常為 data.get('etl:adj_close').values
  np.ndarray[np.float64_t, ndim=2] price_values,
  np.ndarray[np.float64_t, ndim=2] high_values,
  np.ndarray[np.float64_t, ndim=2] low_values,
  np.ndarray[np.float64_t, ndim=2] open_values,

  # 通常為 data.get('etl:adj_close').index.values 的數值
  np.ndarray[np.int64_t, ndim=1] price_index,

  # 通常為 data.get('etl:adj_close').columns.values 的數值
  np.ndarray[np.str, ndim=1] price_columns,

  # 為 position.values
  np.ndarray[np.float64_t, ndim=2] pos_values, 

  # position.index.values
  np.ndarray[np.int64_t, ndim=1] pos_index,

  # position.columns.values
  np.ndarray[np.str, ndim=1] pos_columns,

  # resample dates
  np.ndarray[np.int64_t, ndim=1] resample,

  # 加密驗證碼
  encryption,

  # 回測相關參數
  double fee_ratio=1.425/1000, double tax_ratio=3/1000,
  double stop_loss=1.0, double take_profit=org_np.inf, bool touched_exit=False,
  double position_limit=1.0, bool retain_cost_when_rebalance=False, stop_trading_next_period=True, int mae_mfe_window=0, int mae_mfe_window_step=1):


  # 伺服器會驗證使用者是否為付費用戶，並且讓用戶可以回測到多少日期以後
  key = b'\x8a\xd9\xe6\xad\xe7{*\xf2\x86?\xce\xb6\xaf}\xa0\xa4'
  iv = b'\xd3;\xc2\t\xbdc~\x8dL\xaeQC\x1a$\xc1\xdd'
  cdef np.int64_t accepted_date = int(float(aes.AES(key).decrypt_ctr(encryption, iv).decode()))


  # 記錄回測結束後，要如何實際操作的資料結構
  global stock_operations

  # 模擬用戶銀行帳戶的資金大小 單位：(百分比)
  cdef double cash = 1

  # 模擬用戶的資金於股票的部位大小 單位：(百分比)
  cdef map[int, double] pos
  cdef map[int, double].iterator it

  # 紀錄上一次 rebalance 完的 pos (用於產生 report.weight 或 report.next_weight)
  cdef map[int, double] latest_rebalanced_pos

  # 將 pos.columns.values 的股票位置對應到 price.columns.values
  cdef map[int, int] pos2price = map_columns(price_columns, pos_columns)

  # 回測明天所要參照的 position.iloc[pos_id]
  cdef int pos_id = 0

  # 回測當天所要參照的 position.iloc[current_position_id]
  cdef int current_position_id = -1

  # 當天是否需要更新上述 pos_id，也就是 current_position_id != pos_id 之時
  cdef bool new_pos = False

  # 回測未實現和已實現損益，為所有的 cash + pos 的部位
  cdef double balance = 1

  # 判斷當天是否要進行再平衡
  cdef bool should_rebalance = False

  # 回測每天的淨資產部位
  cdef np.ndarray[double, ndim=1] creturn = org_np.empty(price_index.size, dtype=org_np.float64)

  # 回測當下的各個資產的損益 1.1 代表獲利 10%
  cdef np.ndarray[double, ndim=1] cr = org_np.ones(pos_values[0].size)

  # 回測當下的資產昨天價格
  cdef np.ndarray[double, ndim=1] previous_price = org_np.ones(pos_values[0].size)

  # 回測當下需要出場的股票紀錄
  cdef vector[int] exit_stocks

  # 回測預先記錄明天要出場的股票記錄
  cdef vector[int] exit_stocks_temp


  # 在 rebalance 之間停損停利的股票
  # 正號代表停利，負號代表停損
  cdef vector[int] exited_stocks

  # 停損停利
  cdef double stop_loss_abs = abs(stop_loss)
  cdef double take_profit_abs = abs(take_profit)

  # 以 price.index 的長度來記錄當天是否 position 需要 rebalance
  cdef vector[long long] date_rebalance = [0] * price_index.size

  ################################
  # 計算 date_rebalance
  ################################
  
  # calculate date rebalance values 0: no-rebalance 1: rebalance
  cdef ptr = 0
  for i in range(0, resample.size):
    d = resample[i]
    
    # 假如明天有數值，且明天的日期小於下個需要 rebalance 的日期，則當天不需要 rebalance ，跳過。
    while ptr+1 < price_index.size and price_index[ptr+1] <= d:
      ptr += 1

    # update date_rebalance
    date_rebalance[ptr] = 1

  # 用來記錄交易時進出場資訊
  start_analysis(price_values, pos2price, nstocks=pos_columns.size, window_=mae_mfe_window, window_step_=mae_mfe_window_step)

  
  # 開始回測
  for d, date in enumerate(price_index):


    # 快速計算，回測部位還未開始變化，淨值不變
    if date < pos_index[0]:
        creturn[d] = 1
        continue

    # 用來額外記錄交易記錄的模組設定
    record_date(d)

    ########################################
    # 開盤: 模擬價格變動，與觸發停損停利
    ########################################
    balance = cash
    it = pos.begin()
    while it != pos.end():

      # 股票的 id 還有此資產淨值
      sid = dereference(it).first
      val = dereference(it).second

      ########################################
      # 計算價格變化所帶來的損益
      ########################################


      # 股票的價格的 id （用於索取價格用）
      sidprice = pos2price[sid]

      # 計算前筆價格如是 NaN 填入當天這筆的價格，
      # 只有初次買入的股票才有可能是 NaN，之後都會是 real，
      if isnan(previous_price[sidprice]):
        previous_price[sidprice] = price_values[d][sidprice]

      # 報酬等於今天價格 / 昨天價格
      r = price_values[d][sidprice] / previous_price[sidprice]

      # 假如昨天價格或今天價格是 NaN，代表該資產還沒買入，
      # 或是當天不提供交易，則報酬率是不變化
      if isnan(r):
        r = 1

      # 該資產部位淨值
      pos[sid] *= r

      if org_np.isnan(cr).any():
          print('**WARRN: finlab numpy array has nan!')

      # 該資產報酬率變化
      cr[sid] *= r

      # 計算停損停利的資產淨值目標
      # todo: 以後用 cr 來計算會比較簡單一點
      entry_pos = pos[sid] / cr[sid]
      max_pos = entry_pos * (1+take_profit_abs
        if entry_pos >= 0 else 1-stop_loss_abs)
      min_pos = entry_pos * (1-stop_loss_abs
        if entry_pos >= 0 else 1+take_profit_abs)

      ########################################
      # 執行當天觸價停損停利(觸價出場)
      ########################################
      if touched_exit:

        # 計算考慮跳空的觸價停損停利

        # 當天資產最高報酬、最低報酬、開盤報酬
        high_r = high_values[d][sidprice] / previous_price[sidprice]
        low_r = low_values[d][sidprice] / previous_price[sidprice]
        open_r = open_values[d][sidprice] / previous_price[sidprice]

        # 當天資產的最高淨值、最低淨值、開盤淨值
        pos_high = pos[sid] / r * high_r
        pos_low = pos[sid] / r * low_r 
        pos_open = pos[sid] / r * open_r

        # 判斷最低、最高、開盤淨值是否有觸價
        # todo: 以後用 high_r, low_r, open_r 來計算會比較簡單
        touch_low = pos_low <= min_pos
        touch_high = pos_high >= max_pos
        touch_open = pos_open >= max_pos or pos_open <= min_pos

        # 最低最高價觸價停損停利
        if touch_high:
          pos[sid] = max_pos
        if touch_low:
          pos[sid] = min_pos

        # 無論如何還是以開盤觸價優先考慮，來確保跳空
        if touch_open:
          pos[sid] = pos_open
        
        # 觸價觸發
        if touch_low or touch_high or touch_open:


          # 紀錄停損停利
          if (touch_low and pos[sid] > 0) or (touch_high and pos[sid] < 0):
            exited_stocks.push_back(-sid)
          else:
            exited_stocks.push_back(sid)

          # 當下清空部位
          org_cash = cash

          # set_null=False since we will need to calculate balance later
          # so p[sid] should exist even when the value is zero
          cash = set_position(pos, sid, 0, cash,
                   fee_ratio=fee_ratio, tax_ratio=tax_ratio, 
                   check_null=False, set_null=False)

          # 將股票賣出換現金
          balance += cash - org_cash

      # 假如是下一根 kbar 賣出
      else:

        ########################################
        # 排定隔天需要停損停利(非觸價出場)
        # 此時需存在 exit_stocks_temp 而非 exit_stocks
        # 因為 exit_stocks 中還存有今天要出場的股票
        ########################################

        # 觸價則記錄在 exit_stocks_temp，準備明天賣出
        if pos[sid] >= max_pos:
          exit_stocks_temp.push_back(sid)
        elif pos[sid] < min_pos:
          exit_stocks_temp.push_back(-sid)


      # 將當下價格存起來，等到下個 iteration 變成昨日價格
      if not isnan(price_values[d][sidprice]):
        previous_price[sidprice] = price_values[d][sidprice]

      # 記錄今天的 balance 是多少
      balance += pos[sid]
      postincrement(it)

    
    ########################################
    # 執行當天的停損停利(非觸價出場)
    # 這個停損停利是昨天排定的，於今天執行
    ########################################
    for sid in exit_stocks:
      abssid = abs(sid)
      if pos.find(abssid) != pos.end() and pos[abssid] != 0:
        cash = set_position(pos, abssid, 0, cash,
                    fee_ratio=fee_ratio, tax_ratio=tax_ratio, 
                    check_null=False, set_null=True)
        exited_stocks.push_back(sid)

    exit_stocks.clear()
    
    ########################################
    # 排定隔天需要停損停利(非觸價出場)
    # 由於 exit_stocks 已經清空，可以排入明天的出場標的
    ########################################
    if exit_stocks_temp.size() != 0:
      exit_stocks.reserve(exit_stocks_temp.size())
      exit_stocks.assign(exit_stocks_temp.begin(), exit_stocks_temp.end())
      exit_stocks_temp.clear()

    ########################################
    # 整體資產再平衡
    ########################################
    if should_rebalance:

      # 當 retain_cost_when_rebalance 開啟時
      # 只要繼續持有，就算 rebalance 後報酬率不會重設
      if retain_cost_when_rebalance:
        for sid, pv in enumerate(pos_values[pos_id]):
          if pv != 0 and ((pos.find(sid) == pos.end()) or pos[sid] * pv <= 0):
              cr[sid] = 1
      else:
        cr.fill(1)


      # 當期已經停損停利，下一期不買入
      if stop_trading_next_period:
          for sid in exited_stocks:
              pos_values[pos_id][abs(sid)] = 0

      cash = rebalance(pos, pos_values[pos_id], cash=cash, fee_ratio=fee_ratio, tax_ratio=tax_ratio, position_limit=position_limit)
      exited_stocks.clear()
      exit_stocks_temp.clear()

      latest_rebalanced_pos = pos
      current_position_id = pos_id
      previous_price = price_values[d].copy()
    
    ########################################
    # 收盤 - 盤後結算
    ########################################
    # calculate balance
    balance = cash
    it = pos.begin()
    while it != pos.end():
      balance += dereference(it).second
      postincrement(it)
    
    creturn[d] = balance
    
    ########################################
    # 判斷明天是否需要再平衡
    ########################################
    # update future_pos
    # next_bar <= pos_id + 1

    # 計算下一根 k 棒的日期
    next_bar = price_index[d+1] if d < len(price_index)-1 else price_index[-1] + org_np.inf

    # 假如下次 rebalance 日期並沒有比下根 k 棒的日期大，則跳過當前的 pos_id
    while pos_id < len(pos_index)-1 and (pos_index[pos_id+1] < next_bar):
      pos_id += 1

    new_pos = pos_id != current_position_id
    
    if not new_pos or date_rebalance[d] == 0:
      should_rebalance = False
      continue
    
    # diff = ((current_position_id == -1) or (org_np.abs(pos_values[pos_id] - pos_values[current_position_id]).sum() > 0))
    # should_rebalance = diff
    should_rebalance = True

    if date > accepted_date:
      break

  end_analysis(pos)
  
  ########################################
  # 輸出結果
  ########################################
  stock_operations = {
    "actions": {},
    "weights": {},
    "next_weights": {}
  }

  # update latest position 
  latest_weight_sum = 0
  it = latest_rebalanced_pos.begin()
  while it != latest_rebalanced_pos.end():
    sid = dereference(it).first
    # weight = dereference(it).second
    weight = pos_values[current_position_id][sid]

    # deal with stopped trades
    if pos.find(sid) != pos.end():
        stock_operations["weights"][sid] = weight
    else:
        stock_operations["weights"][sid] = 0

    latest_weight_sum += weight
    postincrement(it)

  latest_weight_sum = max(1, latest_weight_sum)

  for key in stock_operations['weights']:
    stock_operations['weights'][key] /= latest_weight_sum

  for sid, val1 in enumerate(pos_values[pos_id]):
    
    # skip if the stock is already exited in current round
    if stop_trading_next_period:
        for exited_s in exited_stocks:
            if exited_s == sid:
                continue

    if val1 != 0:
      stock_operations["next_weights"][sid] = val1

  stock_operations['weights'] = normalize_weight(stock_operations['weights'], position_limit)

  stock_operations['next_weights'] = normalize_weight(stock_operations['next_weights'], position_limit)

  # check sell stocks
  if should_rebalance:
      for sid, val1 in enumerate(pos_values[pos_id]):
        if pos.find(sid) != pos.end():
          val0 = pos[sid]
        else:
          val0 = 0
        
        if val0 == 0 and val1 != 0:
          stock_operations['actions'][sid] = 'enter'
        if val0 != 0 and val1 == 0:
          stock_operations['actions'][sid] = 'exit'

  for sid in exit_stocks:
    stock_operations['actions'][abs(sid)] = 'tp' if sid > 0 else 'sl'

  for sid in exited_stocks:
    stock_operations['actions'][abs(sid)] = 'tp_' if sid > 0 else 'sl_'

  return creturn

cpdef get_trade_stocks(np.ndarray[np.str, ndim=1] pos_columns, np.ndarray[np.int64_t, ndim=1] price_index, bool touched_exit):

  global stock_operations
  
  ret = [
    [pos_columns[t[0]], # stock_id
     price_index[t[1]], # entry_date
     price_index[t[2]] if t[2] != -1 else -1, # exit_date
     price_index[t[1]-1] if not touched_exit else price_index[t[1]], # entry_sig_date
     (price_index[t[2]-1] if not touched_exit else price_index[t[2]]) if t[2] != -1 else -1, # exit_sig_date
     mae_mfe.trade_positions[i], # position
     t[2] - t[1] if t[2] != -1 else len(price_index) - t[1], # period
     t[1], # entry_index
     t[2], # exit_index
    ] for i, t in enumerate(mae_mfe.trades)]

  return ret, stock_operations
