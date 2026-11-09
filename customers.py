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