# Customer Registration System


print("=" * 50)
print("Customer Registration")
print("=" * 50)
print("Welcome! Please provide your information below.\n")

# Collect customer information
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email = input("Enter your email address: ")

# Collect and convert age
age_string = input("Enter your age: ")
age = int(age_string)

phone = input("Enter your phone number: ")

# Optional company
company_input = input("Enter your company name (or press Enter to skip): ")
company = None if company_input == "" else company_input

# Display summary
print("\n" + "=" * 50)
print("Registration Summary")
print("=" * 50)
print(f"Name: {first_name} {last_name}")
print(f"Email: {email}")
print(f"Age: {age}")
print(f"Phone: {phone}")
if company is not None:
    print(f"Company: {company}")

print("\nData Types:")
print(f"  first_name: {type(first_name)}")
print(f"  last_name: {type(last_name)}")
print(f"  email: {type(email)}")
print(f"  age: {type(age)}")
print(f"  phone: {type(phone)}")
print(f"  company: {type(company)}")

print("=" * 50)
print("✅ Registration complete!")
