# Your Student ID: 230543001
# Your Name and Surname: Esra Gürbüz

original_list = list(range(1, 11))
print(original_list)

reverse_list = original_list[::-1]
print(reverse_list)

original_list = original_list + [11] + [12] + [13]
print(original_list)

length_of_original_list = len(original_list)
print(int(length_of_original_list))

original_list.remove(original_list[0])
original_list.remove(original_list[length_of_original_list-2]) #-2 because we removed 0
print(original_list)

original_list = list(range(1, 11))
even_numbers_list = original_list[1::2]
print(even_numbers_list)