# myUser = {"name": "David", "age": 128}

# print(myUser["age"])

# # This code outputs 'David'.




# myUser = {"name": "David", "age": 128}

# myUser["name"] = "The legendary David"
# print(myUser)

# # This code outputs 'name:'the legendary David', 'age':'128.



# myUser = {"name": "David", "age": 128}

# print(f"Your name is {myUser['name']} and your age is {myUser['age']}")


# myUser = {"name": "David", "age": 128}

# print(myUser["name"])



# myUser = {"name": "David", "age": 128}

# print(myUser["name"])


# myUser = {"name":"David", "age": 128}

# myUser["age"] = 1500

# print(myUser)



# myUser = {"name":"Andy", "age":128}

# myUser["age"] = 1500

# print(myUser)



name = input("Name: ").strip().capitalize()
dob = input("Date of Birth: ").strip()
tel = input("Telephone number: ").strip()
email = input("Email: ")
address = input("Address: ")
contact = {"name": name, "dob": dob, "tel": tel, "email": email, "address": address}

print()
print(f"""Name: {contact["name"]}""")
print(f"""DOB: {contact["dob"]}""")
print(f"""Tel: {contact["tel"]}""")
print(f"""Email: {contact["email"]}""")
print(f"""Address: {contact["address"]}""")