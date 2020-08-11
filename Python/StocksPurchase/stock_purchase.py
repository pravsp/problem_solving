
def maxProfit(price):
    '''Find the maxium profit that a person can get.
     - price - list of price on each day
     - multiple_purchase is allowed
     - expeccted output is maxium profit per stock
    '''
    st_price = price[0]
    purchase_sell_list = []
    if len(price) <= 1:
        return purchase_sell_list

    bullish = bearish = False
    if st_price > price[1]:
        bearish = True
    else:
        bullish = True
        purchase_idx = 0

    st_idx = 1
    end_idx = len(price)
    while st_idx < end_idx:
        p = price[st_idx]
        if bearish and p > st_price:
            bullish = True
            bearish = False
            purchase_idx = st_idx - 1
        elif bullish and p < st_price:
            bearish = True
            bullish = False
            sell_idx = st_idx - 1
            purchase_sell_list.append((purchase_idx, sell_idx))
            purchase_idx = st_idx
        st_idx += 1
        st_price = p

    if bullish and purchase_idx != st_idx -1:
        purchase_sell_list.append((purchase_idx, st_idx-1))
    return purchase_sell_list



if __name__ == '__main__':
    price = [100, 180, 260, 310, 100, 40, 535, 695, 300]
    print(maxProfit(price))

