# ACTIVITY 2 ; CHUA, FORREST ZELLINE M.

order = []

for i in range(1, 6):
    order.append(input(f"Enter Order {i}: "))
original = order

print(f"""Original Orders: 
{original}""")
order.append(input("Enter Additional Order: "))
print(f"""Updated Orders:
{order}""")
order.insert(0, input("Enter Priority Order: "))
print(f"""Updated Orders:
{order}""")

search = input("Search for an Order: ")
print(f"Number of Occurrences: {order.count(search)}")
print(f"First Index: {order.index(search)}")

cancel = input("Enter Order to Cancel:")
order.remove(cancel)
order.pop(cancel)
print(f"""Updated List:
{order}""")

print(f"Last Order Removed: {cancel}")

print(f"""===== FINAL ORDER REPORT =====
Orders: {order}
Total Remaining Orders: {order.count(order)}""")