N = int(input())
num_list = []
for i in range(N):
    num = int(input())
    num_list.append(num)

num_list.sort()

for i in num_list:
    print(i)