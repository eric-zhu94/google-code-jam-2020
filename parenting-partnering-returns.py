def calculate(li, size):
	ans = []
	time = [0] * 1440
	for tup in li:
		for i in range(tup[0], tup[1]):
			time[i] += 1
	for m in time:
		if m > 2:
			return "IMPOSSIBLE"
	posn = []

	order = sorted(li, key = lambda x:x[0], reverse=True)
	order_sort = order[::-1]
	for act in order_sort:
		posn.append(li.index(act))
	C = 0
	J = 0
	while len(order) != 0:
		task = order.pop()
		if C <= task[0]:
			ans.append('C')
			C = task[1]
		else:
			ans.append('J')
			J = task[1]
	ans = list(zip(*sorted(zip(posn, ans))))[1]
	return ans




num_cases = int(input())
num_acts = []
sched = {}
ans = []
for i in range(num_cases):
	x = int(input())
	sched[i] = []
	num_acts.append(x)
	for j in range(x):
		sched[i].append(list(map(lambda x: int(x), input().split(' '))))





for i in range(num_cases):
	ans.append(calculate(sched[i], num_acts[i]))

for i in range(len(ans)):
	print("Case #" + str(i + 1) + ": " + str(''.join(ans[i])))
