# --- Exercise 1 ---
customer = {
    "name": "Alice",
    "email": "alice@email.com",
    "tier": "silver",
    "ytd_spend": 1200
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)
# --- Exercise 2 ---
customer["phone"] = "555-123-4567"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)
# --- Exercise 3 ---
email = customer.get("email", "no email on file")
print(email)
try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")
# --- Exercise 4 ---
for key, value in customer.items():
    print(f"{key}: {value}")
# Without .items(), the loop only gives you the keys.
for key in customer:
    print(key)
# --- Exercise 5 ---
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}
discount_rate = tier_discounts.get(customer["tier"], 0)
purchase_price = 200

discount_amount = purchase_price * discount_rate
final_price = purchase_price - discount_amount
print("Customer tier:", customer["tier"])
print("Discount rate:", discount_rate * 100, "%")
print("Final price: $", final_price)
# --- Exercise 6 ---
dict1 = {
    "name": "Alice",
    "tier": "platinum"
}

dict2 = {
    "name": "Bob",
    "tier": "silver"
}

dict3 = {
    "name": "Charlie",
    "tier": "gold"
}
customers = [dict1, dict2, dict3]
for customer in customers:
    name = customer["name"]
    tier = customer["tier"]

    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(f"{name} | {tier} | Discount: ${discount_amount:.2f}")