# Your Student ID: 230543001
# Your Name and Surname: Esra Gürbüz

word = input("Enter a string: ")

dictionary = {}

for char in word:
    if char in dictionary:
        dictionary[char] += 1
    else:
        dictionary[char] = 1

for char in sorted(dictionary):
    print(f"{char} : {dictionary[char]}")


