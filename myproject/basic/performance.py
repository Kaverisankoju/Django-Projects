nums = [1,2,3,4,5,6,7,8,9]
even_list_comp = [n for n in nums if n % 2 == 0]
even_filter = list(filter(lambda x: x % 2 == 0,nums))
squares = list(map(lambda x: x**2,nums))
print("LIST COMPREHENSION:",even_list_comp)
print("LAMBA AND FILTER:",even_filter)
print("MAP SQUARES:",squares)