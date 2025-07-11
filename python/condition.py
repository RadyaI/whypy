a = 200
b = 33
x = 44

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


if a > b: print("a is greater than b")

# If else tapi 1 baris
print("A") if a > b else print("B")

# If else 1 baris tapi ada 3 kondisi
print("A") if a > b else print("=") if a == b else print("B")

# Nested If
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# if statements cannot be empty, but if you for some reason have an if statement with no content,
#  put in the pass statement to avoid getting an error.
# Sumber penjelasan: w3schools.com
if b > a:
  pass