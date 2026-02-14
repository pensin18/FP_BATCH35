# l2 = [22,33,44,55]

# final = []
# for i in l2:
#     final.insert(0,i)
# print(final)  

# print(list(range(3,-1,-1)))
# final2=[]
# for i in range(len(l2)-1,-1,-1):
#     final2.append(l2[i])
# print(final2)


# final3=[]
# for i in range(-1,-len(l2)-1,-1):
#     final3.append(l2[i])
# print(final3)    


# s2 = 'tsla'
# f1 = ''
# for i in s2:
#     f1 = i + f1
# print(f1)

# f2 = ''
# for i in range(len(s2)-1,-1,-1):
#     f2 = f2 + s2[i]
# print(f2)

# f3 = ''
# for i in range(-1,-(len(s2)+1),-1):
#     f3 = f3+s2[i]
# print(f3)    

# table = 8
# for i in range(1,11):
#     print(f"{table} x {i} = {table*i}")

# num = input("Enter a number: ")
# list1 = [44,55,66,77,55,55,67,89]
# count = 0
# for i in list1:
#     if i == int(num):
#         count += 1
# print(f"Number {num} appears {count} times in the list.")


# def even_numbers(n):
#     even_numbers_list = []
#     for i in range(2,n+1,2):
#         even_numbers_list.append(i)
#     return even_numbers_list
# print(even_numbers(20))

# def even_numbers(n):
#     even_numbers_list = []
#     for i in range(1,n+1):
#         if i % 2 == 0:
#             even_numbers_list.append(i)
#     return even_numbers_list

# print(even_numbers(20))

def string_reverse(s):
    reversed_string = ""
    for i in range(len(s)-1,-1,-1):
        reversed_string += s[i]
    return reversed_string
print(string_reverse("fessorpro"))