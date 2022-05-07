num_list = list(map(int, input().split()))
list = []

num = int(num_list[0])
num2 = int(num_list[1])

for i in range(num):
    s = input()
    list.append(s)

list.reverse()


a = 0
b = 0
for i in range(num_list[0]):
    b = num2 // int(list[i])
    num2 = num2 % int(list[i])
    a = a + b
    
print(a)