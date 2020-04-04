def calculate(li, size):
	trace = 0
	rep_rows = 0
	rep_cols = 0
	#calculate trace
	for i in range(size):
		trace += li[i][i]
	#calculate cols
	for i in range(size):
		tmp = [el[i] for el in li]
		if len(tmp) != len(set(tmp)):
			rep_cols += 1
	for l in li:
		if len(l) != len(set(l)):
			rep_rows +=1
	return [trace, rep_rows, rep_cols]

num_cases = int(input())
row_sizes = []
cases = {}
ans = []

for i in range(num_cases):
    cases[i] = []
    size = int(input())
    row_sizes.append(size)
    for j in range(size):
        cases[i].append(list(map(lambda x: int(x), input().split(' '))))

for i in range(num_cases):
	ans.append(calculate(cases[i], row_sizes[i]))

for i in range(len(ans)):
	print("Case #" + str(i + 1) + ": " + str(ans[i][0]) + " " + str(ans[i][1]) + " " + str(ans[i][2]))
