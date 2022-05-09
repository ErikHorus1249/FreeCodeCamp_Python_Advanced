# Tính chất của Tuple:
# + Ordered 
# + immutable 
# + allows duplicate elements 

# my_tuple = ("max", 28)
# my_tuple = tuple(["hi", "hello", "salut"])
# print(type(my_tuple))
# Nếu chỉ số là -1 nó sẽ quay lại item cuối 
# print(my_tuple[0])
# print(my_tuple[-1])

# Tìm kiếm một item trong tuple 
# if "hi" in my_tuple:
#     print("yes")
# else: 
#     print("No")

# Method len kiểm tra số lượng phần tử 
characters = ['a', 'b', 'c', 'c', 'v', 'f']
# print(len(characters))

# Đếm số lần item xuất hiện 
# print(characters.count('c'))
# Lấy giá trị thứ tự của item trong tuple 
# print(characters.index('b'))

# Chuyển đổi tuple thành list 
# my_list = list(my_tuple)
# print(type(my_list))
# Chuyển từ tuple sang list 
# my_tuple1 = tuple(my_list)
# print(type(my_tuple1))


# Tính chất list slicing tương tự cho tuple 
# a = (1, 2, 3, 4 ,5 , 6, 7, 8, 9)
# b = a[:4]
# print(b)


# Gán nhiều biến từ giá trị một biến tuple, số lượng biến phải tương đương với số lượng item 
# per_tuple = "max", 12, "Hanoi"
# name, age, loc = per_tuple
# print(name)
# print(age)
# print(loc)

# Sử dụng * để lấy tất các item nào ko có biến để map -> chuyển thành list
# numbers = (1, 2, 3, 5)
# num1, *num2, num3 = numbers
# print(num1)
# print(num2)
# print(num3)

# List khi lưu trữ sẽ chiếm nhiều không gian bộ nhớ hơn 
# import sys
# my_list = ["hi", "hello", "salut"]
# my_tuple = ("hi", "hello", "salut")
# print(sys.getsizeof(my_list))
# print(sys.getsizeof(my_tuple))