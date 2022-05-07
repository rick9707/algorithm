num = int(input())
num_list = list(map(int, input().split()))
a = 0
b = 0

num_list.sort()
for i in range(num):
    a = a + num_list[i]
    b = b + a
print (b)