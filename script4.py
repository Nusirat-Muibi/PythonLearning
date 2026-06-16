#shopping cart

prices = [12,45,8,23,67,15,34,9,52,28]
expensive_items = []
affordable_items = []

for price in prices:
    if price > 20:
        expensive_items.append(price)
else:
    affordable_items.append(price)

print("expensive_item:", expensive_items)
print("affordable_item:", affordable_items)
print("most expensive:", max(prices))
print("cheapest_items:", min(prices))
print("number of affordable items:", len(affordable_items))
print("total cost of all items:", sum(prices))
