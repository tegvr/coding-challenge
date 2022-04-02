#tegarQ1

total = []
T = int(input(""))

while T > 0 :
	A = int(input(""))
	B = int(input(""))
	K = int(input(""))

	#constraint
	a = 1 <= T <= 100
	b = 1 <= A <= B < 10000
	c = 1 <= K < 10000

	if a and b and c:
		result = []
		for x in range(A,B+1):
			if x % K == 0: result.append(x)
			else: continue
		
		total.append(len(result))
		
		T-=1
	else :
		break

for x in range (len(total)):
	print("Case {0}: {1}".format(x+1,total[x]))