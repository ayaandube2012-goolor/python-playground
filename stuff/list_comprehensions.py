numbers = [1, 2, 3, 66, 52804793, 2.1415926535897932384626433832795028841971693993751]
new_list = [num + 1 for num in numbers]
print(new_list)

me = 'Ayaan'
name_list = [letter for letter in me]
print(name_list)

ranger = range(1, 5)
range_doubled = [num * 2 for num in ranger]
print(range_doubled)

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 123456789, 1673, 1794823483483483483483483483483483, 67]
test = [num for num in numbers2 if num > 7]
print(test)
