#Exercise 01
# programming_lanuage = ['python', 'java', 'c', 'note js', 'Html', 'css', 'react js']
# '''final_output_lanuage = ['python', 'note js', 'Html', 'react js']'''
#
# programming_lanuage=[x for (i,x) in enumerate (programming_lanuage) if i not in (1,2,5)]
# print(programming_lanuage)

#Exercise 02

# num = [3, 5, 7, 8, 4, 33, 44, 41, 13, 43]
# new_num = []
# for element in num:
#     if element % 2 == 1:
#         new_num.append(element)
# print(new_num)
#
# another_num_list = [elem for elem in num if elem %2 != 0]
# print(another_num_list)

# Exercise 03
# num = [3, 5, 7, 8, 4, 33, 44, 41, 13, 43, 66, 14, 143, 1114, 13]
# print(num.index(8))
# for element in num:
#     print(str(element).zfill(5), '*****', num.index(element))

# Exercise 04
#sample_list = emp3, emp4
# num = [3, 5, 7, 8, 4, 33, 44, 41, 13]
# num = ['emp'+str(x) for x in num]
# print(num)

# Exercise 05

list3 = [60, 70, 80]
list4 = [10, 90 ,30]
list4.extend(list3)
print(list4)
list4.sort()
print(list4)
list4.sort(reverse=True)
print(list4)



