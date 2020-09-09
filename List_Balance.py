def Solution(L):
	sum1 = 0
	sum2 = 0
	for i in range(0,2):
		sum1 = sum1 + i
	for j in range(3,len(L):
		sum2 = sum2 + j
	if sum1 == sum2:
		retun 0
	else:
		return 1
N = int(input())
L = []
n = 0
for e in input().split():
	if n < N :
		L.append(int(e))
		n += 1
print(Solution(L), end = '')
