from countingsort import *
from utils import *


original_names = ["BATURAY", "GORKEM", "GIRAY", "TAHIR", "BARIS"]

A = ["BATURAY", "GORKEM", "GIRAY", "TAHIR", "BARIS"]

print()
print(" ------ Sorting Strings with RadixSort: -------")
print()
print(" Initial list of strings:", original_names)

print(" Modifications: ", end="\n")

longest_name = longest(A)
longest_name_len = len(longest_name)


print(" 1. Find longest name:", longest_name, "({})".format(longest_name_len))

fill_name(A, longest_name_len)
print(" 2. Fill shorter names with 'A':", A)



#print("name_map: ", map.items() )

convert_ascii(A)
map = name_map(original_names, A)
#print("A after convert_ascii: ", A)
print(" 3. Convert names to ASCII numbers of their chars:")
for k, v in map.items():
    print("{}: {}".format(k, v))

print()


"""
convert_str(A)
print("A after convert_str: ", A)
"""

# [[1, 0, 19, 20, 17, 0, 24], 
# [6, 14, 17, 10, 4, 12, 0], 
# [6, 8, 17, 0, 24, 0, 0], 
# [19, 0, 7, 8, 17, 0, 0], 
# [1, 0, 17, 8, 18, 0, 0]]

#convert_str(A)
#print("init:", A)
#convert_ascii(A)
print()
print()
print(" --------- RadixSort Steps ---------")
print()

for k in range(longest_name_len-1, -1, -1):
    
    convert_str(A)
    print("start of index {}:".format(k), A)
    convert_ascii(A)

    countingsort(A, k)

    convert_str(A)
    print("end of index {}:".format(k), A)
    convert_ascii(A)

    print()

    
print("A after radixsort:", A)
convert_str(A)
print("A after convert_str: ", A)
