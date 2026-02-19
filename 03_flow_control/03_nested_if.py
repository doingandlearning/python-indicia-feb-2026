# nested things are possible but not always advisable ... 

# 2 -> 4 -> 8 -> 16

is_sunny = True
temp_in_celcius = 24
has_airconditioning = True

if is_sunny:
  if temp_in_celcius > 20:
    if has_airconditioning:
      print("Whack on the airconditioning (sorry planet)!")
    else:
      print("Try not to melt - too hot for me!")
  print("It's nice outside.")
else:
  print("I like it when it's not sunny.")

if is_sunny and temp_in_celcius > 20:
  print("Whack on the airconditioning (sorry planet)!") 

if is_sunny and not temp_in_celcius > 20:
  print("Whack on the airconditioning (sorry planet)!") 

if is_sunny or temp_in_celcius > 20:
  print("That's nice!")
