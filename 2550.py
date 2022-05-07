num = int(input())
num_list = list(map(int, input().split()))
num_list1 = list(map(int, input().split()))

num1 = int(num*num)

Matrix = [[0]*num1 for i in range(num)]


print(Matrix)
a = 0
c = []
d = 0
num_list[a]
for d in range(len(num_list1)):
    b = 0
    for a in range(len(num_list)):
        if num_list[d] == num_list1[a]:
            c.append(b)
            print(b)
            
        b = b + 1
        print(b)

print(c)