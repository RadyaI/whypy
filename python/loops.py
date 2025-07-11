i = 0
fruits = ["apple", "banana", "cherry"]

while i < 6:
    print(i)
    i += 1

# Berhenti loop kalo i nilainya 3
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# Skip loop kalo i nilainya 3
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

for x in fruits:
  print(x)

# Looping berdasarkan huruf yang ada di "banana"
for x in "banana":
  print(x)

# Berhenti Loop kalau x nya "banana"
# Berhenti kalau sudah sampai "banana"
for x in fruits:
  print(x)
  if x == "banana":
    break
  
# Skip kalau ketemu "banana"
for x in fruits:
  if x == "banana":
    continue
  print(x)

# For loops berdasarkan angka
# range 6 artinya loops dari x sampai 5
for x in range(6):
  print(x)

# Kalau ini start dari 2 sampai 5
for x in range(2, 6):
  print(x)