sell = [[90, 11], [41, 98], [89, 120], [70, 51]]

bananas = [52, 41, 94, 141]

for i in range(len(bananas)):
    sell[i].append(bananas[i])

sell[1][0] += round(sell[2][0] * 0.5)
sell[2][0] += round(sell[3][0] * 0.5)

sumFruit = [0, 0, 0]
for i in range(len(sell)):
    sumFruit[0] += sell[i][0]
    sumFruit[1] += sell[i][1]
    sumFruit[2] += sell[i][2]
maxSumFruit = max(sumFruit)
print("3. ", "Jablka" if maxSumFruit == sumFruit[0] else "", "Hrušky" if maxSumFruit == sumFruit[1] else "", "Banány" if maxSumFruit == sumFruit[2] else "")

minSell = min(list([sum(sell[0]), sum(sell[1]), sum(sell[2]), sum(sell[3])]))
print("4. ", "1. čtvrtletí" if minSell == sum(sell[0]) else "", "2. čtvrtletí" if minSell == sum(sell[1]) else "", "3. čtvrtletí" if minSell == sum(sell[2]) else "", "4. čtvrtletí" if minSell == sum(sell[3]) else "")