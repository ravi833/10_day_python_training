'''list methods in python'''
'''list mutable it contains modification'''
'''list allows several data types .list contain inside the list'''
'''list is a sequential'''

# a=[2,23,3.4,5.6,'ravi','program',None,[2,34]]
# print(a,type(a))
# print(a[4])  #ravi

# a[9]=5
# print(a)  #index error: list assignment out of range


# print(dir(list))  # 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# a=[2,23,3.4,5.6,'ravi','program',None,[2,34]]
# a.append(7)
# print(a) #   [2, 23, 3.4, 5.6, 'ravi', 'program', None, [2, 34], 7]

# a=[2,23,3.4,5.6,'ravi','program',None,[2,34]]
# a.clear()
# print(a)  #  []


# a=[2,23,3.4,5.6,'ravi','program',None,[2,34]]
# a.copy()
# print(a)   #[2, 23, 3.4, 5.6, 'ravi', 'program', None, [2, 34]]


# a=[2,23,3.4,5.6,'ravi','program',None,[2,34]]
# # d = a.count(2)
# # print(d)
# print(a.count(2))   #1

# a=[2,23,3.4,5.6,'ravi','program']
# b=[23,24]
# a.extend(b)
# print(a)  #[2, 23, 3.4, 5.6, 'ravi', 'program', 23, 24]
# b.extend(a)
# print(b)    #[23, 24, 2, 23, 3.4, 5.6, 'ravi', 'program', 23, 24]


# a=[2,23,3.4,5.6,'ravi','program',None,[2,34]]
# print(a.index(5.6))  #3
# print(a[0])  #2
# print(a[-1][1])  #34

# a=[2,23,3.4,5.6,'ravi','program',None,[2,34]]
# a[2]=56
# print(a)  #[2, 23, 56, 5.6, 'ravi', 'program', None, [2, 34]]


# a=[2,23,3.4,5.6,'ravi','program',None,[2,34]]
# a.pop(2)
# print(a)  # [2, 23, 5.6, 'ravi', 'program', None, [2, 34]]


# a=[2,23,3.4,5.6,'ravi','program',None,[2,34]]
# a.remove(23)
# print(a)  #  [2, 3.4, 5.6, 'ravi', 'program', None, [2, 34]]

# a=[2,23,3.4,5.6,'ravi','program',None,[2,34]]
# a.reverse()
# print(a)  #  [[2, 34], None, 'program', 'ravi', 5.6, 3.4, 23, 2]




# a=[2,23,55,6,2,3,.12]
# # a.sort(reverse=False)   #  [0.12, 2, 2, 3, 6, 23, 55]
# # print(a)
# a.sort(reverse=True)
# print(a)  #  [55, 23, 6, 3, 2, 2, 0.12]


'''tuple is immutable modification can't allows'''
'''tuple is sequential'''
'''tuple is several data types'''
'''tuple methoda in python'''
# from crypt import methods
# from typing import Tuple


# print(dir(tuple))    # ' count','index'

# a=23,35,67,6.4
# print(a.count(23))    #1


# print(a[1])  #35