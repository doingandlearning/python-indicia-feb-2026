first_name = "Kevin"
last_name = "Cunningham"

# concatenate -> join together!
full_name = first_name + " " + last_name
print(full_name)

'He said, "Hello"'
"I don't think so"
# f-string  f""  f''
print(f"{ first_name } { last_name }")  # interpolation
print(f"1 + 1 = { 1 + 1 }")

print(f'''{first_name} {last_name}
Belfast
Northern Ireland''')
""""""

print(len(full_name)) # length
print(full_name.upper())
print(full_name.center(25))
print(full_name.ljust(25))
print(full_name.rjust(25))

print(full_name.find("in"))

# 0123456789
# Kevin Cunningham  

print(full_name.find('funny'))  # -1 means not found

# collections -> []
print(full_name[4])  # what is in position 4?
print(full_name[4:9])  # what are the values from 4 up to but not including 9
print(full_name[:7])
print(full_name[7:])