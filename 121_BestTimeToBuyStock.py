import ipdb 

def maxProfit(prices):
    n = len(prices)

    # 增加一个判断。如果n=0时。 prices[0]会出错
    min_price = prices[0]
    profit = 0

    for i in range(n):
        if(prices[i]<min_price):
            min_price = prices[i]
        if(prices[i]-min_price>profit):
            profit = prices[i] - min_price
    return profit

if __name__=="__main__":
    prices = [7,1,5,3,6,4]
    ans = maxProfit(prices)
    print(ans)

