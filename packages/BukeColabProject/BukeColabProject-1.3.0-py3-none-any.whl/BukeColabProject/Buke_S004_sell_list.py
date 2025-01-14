from datetime import date, timedelta
import pandas as pd
from pandas import DataFrame
import math

from BukeColabProject.indicator import sma, ibs, pivot_standard, stochastic_fast_k, stochastic_fast_d, \
    pivot_standard_for_sellprice, 순거래대금
from BukeColabProject.function import rank, ts_min
from BukeColabProject.parameter import Market, MovingAverage
from BukeColabProject.tools import get_stock_exchange_tax, get_ask_price, get_bid_price


def what_day_is_it(date):

    days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    day = date.weekday()
    return days[day]


def str_to_date(trading_day: str) -> date:
    return date(int(trading_day[:4]), int(trading_day[5:7]), int(trading_day[8:]))


def int_to_str(x: int) -> str:

    try:
        x = int(x)
        return "%06d" % x
    except:
        return x


def read_trading_days(dir, start_date: date, end_date: date):

    df = pd.read_csv(f"{dir}/data_file/korea_trading_days.csv", index_col=0)
    df['날짜'] = df['날짜'].apply(lambda day: str_to_date(day))
    trading_days = df['날짜'].to_list()
    trading_days = [day for day in trading_days if start_date <= day <= end_date]
    return trading_days


def read_day_price(dir, start_date: date, end_date: date):
    df = pd.read_csv(f"{dir}/data_file/수급데이터_2022_to_{end_date.year}.csv", index_col=0)
    df['날짜'] = df['날짜'].apply(lambda day: str_to_date(day))
    # try:
    df['종목코드'] = df['종목코드'].apply(lambda x: int_to_str(x))
    # except:
    #     pass
    return df


def read_index_day_price(dir, start_date: date, end_date: date):

    df = pd.read_csv(f"{dir}/data_file/MSCI_한국_ETF.csv", index_col=0)
    df['날짜'] = df['날짜'].apply(lambda day: str_to_date(day))
    return df


def read_index_history(dir, start_date: date, end_date: date):

    ks_history = pd.read_csv(f"{dir}/data_file/코스피_종목리스트_2022_to_{end_date.year}.csv", index_col=0)
    ks_history['날짜'] = ks_history['날짜'].apply(lambda day: str_to_date(day))
    ks_history = ks_history.set_index('날짜')

    kq_history = pd.read_csv(f"{dir}/data_file/코스닥_종목리스트_2022_to_{end_date.year}.csv")
    kq_history['날짜'] = kq_history['날짜'].apply(lambda day: str_to_date(day))
    kq_history = kq_history.set_index('날짜')
    return ks_history, kq_history


def add_indicator(day_price: DataFrame, index_day_price: DataFrame) -> DataFrame:

    group_list = []
    grouped = day_price.groupby('종목코드')
    for key, group in grouped:
        group = group.reset_index(drop=True)
        group = group.reset_index(drop=True)
        group['거래대금_이평선_5'] = sma(group['거래대금'], 5)
        group['pivot_기준선'] = pivot_standard(group['고가'], group['저가'], group['종가'])

        group['ibs'] = ibs(group['고가'], group['저가'], group['종가'])

        group['기관순거래대금_이평선_5'] = sma(group['기관순거래대금'], 5)
        group['기관순거래대금_이평선_10'] = sma(group['기관순거래대금'], 10)

        group['종가_최솟값_10'] = ts_min(group['종가'], 10)

        group['순거래대금'] = 순거래대금(group['종가'], group['거래량'], 1)
        group['순거래대금_이평선_5'] = sma(group['순거래대금'], 5)

        group['종가_이평선_20'] = sma(group['종가'], 20)

        group['스토캐스틱_fast'] = stochastic_fast_k(group['고가'], group['저가'], group['종가'], 20)
        group['스토캐스틱_slow'] = stochastic_fast_d(group['고가'], group['저가'], group['종가'], 20, 5, MovingAverage.sma)

    group_list.append(group)
    day_price = pd.concat(group_list, axis=0)
    day_price = day_price.reset_index(drop=True)

    group_list = []
    grouped = day_price.groupby('날짜')
    for key, group in grouped:
        group = group.reset_index(drop=True)
        group['거래대금_이평선_5_순위'] = rank(group['거래대금_이평선_5'])
        group['순거래대금_이평선_5_순위'] = rank(group['순거래대금_이평선_5'])
        group['시가총액_순위'] = rank(group['시가총액'])

        group_list.append(group)
    day_price = pd.concat(group_list, axis=0)
    day_price = day_price.reset_index(drop=True)

    day_price_dict = {}
    grouped = day_price.groupby('종목코드')
    for key, group in grouped:
        increase_condition1 = group['ibs'] < 0.7
        increase_condition2 = group['거래대금_이평선_5'] > group['거래대금']
        increase_condition3 = group['종가'] / group['종가_최솟값_10'] > 1.1
        increase_condition4 = group['종가'] / group['종가_이평선_20'] > 1.05
        increase_condition5 = group['기관순거래대금_이평선_5'] > 0
        increase_condition6 = group['기관순거래대금_이평선_10'] > 0

        increase_condition = increase_condition1 & increase_condition2 & increase_condition3 & increase_condition4 & \
                             increase_condition5 & increase_condition6

        liquidity_condition1 = group['순거래대금_이평선_5_순위'] > 0.3
        liquidity_condition2 = group['시가총액_순위'] > 0.3

        liquidity_condition = liquidity_condition1 & liquidity_condition2

        # Result
        group['#final_result'] = increase_condition & liquidity_condition

        group['#priority'] = group['스토캐스틱_slow'] - group['스토캐스틱_fast']

        group = group.set_index('날짜')
        day_price_dict[key] = group

    # Market Timing
    index_day_price['이평선_3'] = sma(index_day_price['종가'], 3)
    index_day_price['이평선_5'] = sma(index_day_price['종가'], 5)
    index_day_price['이평선_10'] = sma(index_day_price['종가'], 10)
    # index_day_price['pct_change_21'] = pct_change(index_day_price['close'], 21)
    index_day_price['#market_timing'] = (index_day_price['종가'] > index_day_price['이평선_3']) | \
                                        (index_day_price['종가'] > index_day_price['이평선_5']) | \
                                        (index_day_price['종가'] > index_day_price['이평선_10'])
    index_day_price = index_day_price.set_index('날짜')

    return day_price_dict, index_day_price



def back_testing(dir, start_date, end_date):

    # 0. 변수
    max_basket_size = 10
    liquidation_holding_days = 1
    cut_period = 0
    seed_money = 10000000
    fee = 0.00015  # when using kiwoom
    basket = {}  # key:ticker, value:buy_price, stock_num, holding_days
    pnl = {'date': [start_date], 'balance': [seed_money]}
    p_len = []


    # 1. 거래일 가져오기
    trading_days_list = read_trading_days(dir, start_date, end_date)

    # 2. 일봉 가져오기
    day_price = read_day_price(dir, start_date, end_date)

    index_day_price = read_index_day_price(dir, start_date, end_date)

    # 3. 지수 종목 구성 내역 가져오기
    kospi_history, kosdaq_history = read_index_history(dir, start_date, end_date)

    # 4. 매수 조건 및 우선순위 생성
    day_price, index_day_price = add_indicator(day_price, index_day_price)
    print(f"Finished data preprocessing...")
    # print(day_price[['#final_result','#priority','market_timing']])
    # print(day_price.tail())


    # 5. 백테스트
    for i, day in enumerate(trading_days_list):

        # if i > 1:
        # 당일 코스피, 코스닥 구성 종목 내역 가져오기
        kospi_ticker_list = kospi_history['종목리스트'].loc[day].split(',')
        kosdaq_ticker_list = kosdaq_history['종목리스트'].loc[day].split(',')

        # Market Timing
        buy_check = 1
        try:
            yesterday_market_time = bool(index_day_price['#market_timing'].loc[trading_days_list[i - 1]])
        except:
            buy_check = 0

            # 매수
        if len(basket) < max_basket_size and buy_check == 1:
            # buy at open price
            pre_buy_list = []
            for ticker in kospi_ticker_list + kosdaq_ticker_list:

                if ticker in basket:
                    continue
                try:
                    yesterday_buy_condition = bool(
                        day_price[ticker]['#final_result'].loc[trading_days_list[i - 1]])

                    # Market Time

                    if yesterday_market_time and yesterday_buy_condition :
                        priority_value = float(day_price[ticker]['#priority'].loc[trading_days_list[i - 1]])
                        ticker_data = (priority_value, ticker)
                        pre_buy_list.append(ticker_data)
                except:
                    pass

            if len(pre_buy_list) > 0:
                p_len.append(len(pre_buy_list))
                pre_buy_list.sort(reverse=True)
                # print(f"{day}, {pre_buy_list}")
                for priority_value, ticker in pre_buy_list[:max_basket_size - len(basket)]:
                    yesterday_low = int(day_price[ticker]['저가'].loc[trading_days_list[i - 1]])
                    tomorrow_pivot_standard_price = float(day_price[ticker]['pivot_기준선_for_sell'].loc[day])

                    # yesterday_close = int(day_price[ticker]['close'].loc[trading_days_list[i - 1]])

                    if ticker in kospi_ticker_list:
                        today_target_buy_price = get_ask_price(yesterday_low * 0.98, Market.kospi)
                        sell_price = get_bid_price(tomorrow_pivot_standard_price * 1.01,
                                                          Market.kospi)
                    else:
                        today_target_buy_price = get_ask_price(yesterday_low * 0.98, Market.kosdaq)
                        sell_price = get_bid_price(tomorrow_pivot_standard_price * 1.01,
                                                   Market.kosdaq)

                    today_open = int(day_price[ticker]['시가'].loc[day])
                    today_low = int(day_price[ticker]['저가'].loc[day])
                    today_name = day_price[ticker]['종목명'].loc[day]

                    real_buy_price = 0.

                    if today_open <= today_target_buy_price:
                        buy_price = math.ceil(today_open * (1 + fee))
                        real_buy_price = today_open
                    elif today_low < today_target_buy_price:
                        buy_price = math.ceil(today_target_buy_price * (1 + fee))
                        real_buy_price = today_target_buy_price
                    else:
                        continue

                    stock_num = (pnl['balance'][-1] // max_basket_size) // buy_price
                    stock_info = {'stock_num': stock_num, 'buy_price': buy_price, 'holding_days': 0, 'name':today_name, 'buy_date':day, 'real_buy_price':real_buy_price, 'sell_price':sell_price}

                    basket[ticker] = stock_info
                    #print(f"<Buy> date: {day}, ticker: {ticker}, buy_price: {buy_price}")

        # 매도
        today_profit = 0
        if len(basket) > 0:
            tax = get_stock_exchange_tax(day)

            sell_list = []
            for ticker in basket:

                holding_condition1 = basket[ticker]['holding_days'] >= liquidation_holding_days

                if holding_condition1:

                    yesterday_close = int(day_price[ticker]['종가'].loc[trading_days_list[i - 1]])
                    today_open = int(day_price[ticker]['시가'].loc[day])
                    today_high = int(day_price[ticker]['고가'].loc[day])
                    today_close = int(day_price[ticker]['종가'].loc[day])
                    # tomorrow_high = int(day_price[ticker]['고가'].loc[trading_days_list[i + 1]])
                    # tomorrow_low = int(day_price[ticker]['저가'].loc[trading_days_list[i + 1]])
                    pivot_standard_price = float(day_price[ticker]['pivot_기준선'].loc[day])
                    tomorrow_pivot_standard_price = float(day_price[ticker]['pivot_기준선_for_sell'].loc[day])

                    buy_date = basket[ticker]['buy_date']
                    sell_date = day
                    name = basket[ticker]['name']

                    # 익일 상폐 여부 확인
                    # trash_condition = ticker not in tomorrow_kospi_ticker_list + tomorrow_kosdaq_ticker_list

                    if yesterday_market_time is True:

                        if ticker in kospi_ticker_list:
                            target_sell_price = get_bid_price(pivot_standard_price * 1.01,
                                                              Market.kospi)
                            tomorrow_target_sell_price = get_bid_price(tomorrow_pivot_standard_price * 1.01,
                                                              Market.kospi)
                        else:
                            target_sell_price = get_bid_price(pivot_standard_price * 1.01,
                                                              Market.kosdaq)
                            tomorrow_target_sell_price = get_bid_price(tomorrow_pivot_standard_price * 1.01,
                                                              Market.kosdaq)

                        today_vol = int(day_price[ticker]['거래량'].loc[day])
                        basket[ticker]['sell_price'] = tomorrow_target_sell_price

                        if today_open >= target_sell_price:
                            sell_price = today_open
                        elif today_high > target_sell_price:
                            sell_price = target_sell_price
                        else:
                            basket[ticker]['holding_days'] += 1
                            continue
                    else:

                        if ticker in kospi_ticker_list:
                            target_sell_price = get_bid_price(pivot_standard_price * 1.01,
                                                              Market.kospi)
                            tomorrow_target_sell_price = get_bid_price(tomorrow_pivot_standard_price * 1.01,
                                                                       Market.kospi)
                        else:
                            target_sell_price = get_bid_price(pivot_standard_price * 1.01,
                                                              Market.kosdaq)
                            tomorrow_target_sell_price = get_bid_price(tomorrow_pivot_standard_price * 1.01,
                                                                       Market.kosdaq)

                        today_vol = int(day_price[ticker]['거래량'].loc[day])
                        # tomorrow_vol = int(day_price[ticker]['거래량'].loc[trading_days_list[i + 1]])
                        basket[ticker]['sell_price'] = tomorrow_target_sell_price

                        if today_open >= target_sell_price:
                            sell_price = today_open
                        elif today_high > target_sell_price:
                            sell_price = target_sell_price
                        else:
                            basket[ticker]['holding_days'] += 1
                            continue

                    profit = basket[ticker]['stock_num'] * (
                            math.floor(sell_price * (1 - (tax + fee))) - basket[ticker]['buy_price'])
                    today_profit += profit


                    #print(f"<Sell> date: {day}, ticker: {ticker}, sell_price: {sell_price}, profit: {profit}")
                    sell_list.append(ticker)

                else:
                    basket[ticker]['holding_days'] += 1
            for ticker in sell_list:
                basket.pop(ticker)


        # Balance Update
        pnl['date'].append(day)
        pnl['balance'].append(pnl['balance'][-1] + today_profit)

    return basket


def Buke_S004_sell_list(dir, today):


    path = f"{dir}/trade_list/{today}"

    end_date = today# today는 토요일 or 일요일
    start_date = end_date - timedelta(days=21)

    print(start_date, end_date)
    trading_days_list = read_trading_days(dir, start_date, end_date)

    real_start_date = trading_days_list[0]
    real_end_date = trading_days_list[-1]
    print("start_date : ", what_day_is_it(real_start_date))
    print("end_date   : ", what_day_is_it(real_end_date))
    print()

    basket = back_testing(dir, real_start_date, real_end_date)


    file_name = "sell_4"
    sell_basket = {'종목코드': [], '종목명': [], '매도가격': []}

    for ticker in basket:

        sell_price = basket[ticker]['sell_price']
        name = basket[ticker]['name']

        sell_basket['종목코드'].append(ticker)
        sell_basket['종목명'].append(name)
        sell_basket['매도가격'].append(sell_price)

    sell_basket = pd.DataFrame(sell_basket)
    sell_basket.to_csv(f"{path}/{file_name}_{str(today)[-5:]}.txt")