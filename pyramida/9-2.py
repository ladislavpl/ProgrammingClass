sell = {
    "apples1": 90,
    "apples2": 41,
    "apples3": 89,
    "apples4": 70,
    "pears1": 11,
    "pears2": 98,
    "pears3": 120,
    "pears4": 51,
}

bananas = [52, 41, 94, 141]

for i in range(len(bananas)):
    sell[f"bananas{i + 1}"] = bananas[i]

sell["apples2"] += round(sell["apples2"] * 0.5)
sell["apples3"] += round(sell["apples3"] * 0.5)

sumFruit = [0, 0, 0]
for i in range(1, 5):
    sumFruit[0] += sell[f"apples{i}"]
    sumFruit[1] += sell[f"pears{i}"]
    sumFruit[2] += sell[f"bananas{i}"]
maxSumFruit = max(sumFruit)
print("3. ", "Jablka" if maxSumFruit == sumFruit[0] else "", "Hrušky" if maxSumFruit == sumFruit[1] else "", "Banány" if maxSumFruit == sumFruit[2] else "")

quarters = [0, 0, 0, 0]
for i in range(len(quarters)):
    quarters[i] += sell[f"apples{i + 1}"]
    quarters[i] += sell[f"pears{i + 1}"]
    quarters[i] += sell[f"bananas{i + 1}"]
minSell = min(quarters)
print("4. ", "1. čtvrtletí" if minSell == quarters[0] else "", "2. čtvrtletí" if minSell == quarters[1] else "", "3. čtvrtletí" if minSell == quarters[2] else "", "4. čtvrtletí" if minSell == quarters[3] else "")