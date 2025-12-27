# prices = [200,300,400]
# volumes = [2000,4000,5000]
# #vwap = sum of (price * volume) / sum of volume

# total_price_volume = 0
# total_volume = 0
# for i in range(len(prices)):
#     total_price_volume += prices[i] * volumes[i]
#     total_volume += volumes[i]
# vwap = total_price_volume / total_volume
# print("VWAP is:", vwap)


stock_price = {'amzn': 400,'tsla':489,'nifty':389,'goog':890}
# for i in stock_price:
#     print(i,stock_price[i])

# print(stock_price.keys())
# print(stock_price.values())
# print(stock_price.items())    

# m = list(stock_price.values())[0]
# print(m)
# for i,j in stock_price.items():
#     if j > m:
#         m = j
#         name = i
# print("The highest stock price is of",name,"and the price is",m)
# num = 0
# even_num = []
# while True:
#     if num == 10:
#         break
#     num = num +1
#     if num % 2 == 0:
#         even_num.append(num)
# print("Even numbers entered:", even_num)

portfolio = []
while True:
    name = input("Enter stock name(q to exit)")
    if name.lower() == 'q':
        break
    if name == 'tsla':
        print("You cannot buy this stock")
        continue    
    found = stock_price.get(name)
    if found:
        portfolio.append(name)
    else:
        print("Stock not found")


print("Your portfolio:", portfolio)                         