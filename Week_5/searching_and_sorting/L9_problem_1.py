# ==============
# = Question 1 =
# ==============
a = [1, 2, 3, 4, 0]
b = [3, 0, 2, 4, 1]
c = [3, 2, 4, 1, 5]

# print a[0]
# print b[1]
# print a[a[1]]
# print b[b[2]]
# print a[b[2]]
# print c[a[b[3]]]
# print a[c[a[b[0]]]]
# print a[c[a[b[3]]]]

# ==============
# = Question 2 =
# ==============

# def foo(L):
#     val = L[0]
#     while (True):
#         print val
#         val = L[val]
# 
# # print foo(a)
# # print foo(b)
# print foo(c)



# ==============
# = Question 3 =
# ==============

num = 5
# L = [5, 0, 2, 4, 6, 3, 1]
L = [2, 0, 1, 5, 3, 4]
val = 0
for i in range(0, num):
    val = L[L[val]]

print val