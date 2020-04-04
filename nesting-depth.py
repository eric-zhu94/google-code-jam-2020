num_cases = int(input())
cases = []
ans = []


for i in range(num_cases):
    cases.append([int(d)for d in input()])

for case in cases:
    stack = list(case)[::-1]
    depth = 0
    tmp = []
    while len(stack) > 0:
        x = stack.pop()

        if len(tmp) == 0:
            for i in range(x):
                tmp.append('(')
        else:
            if x > depth:
                for i in range(x - depth):
                    tmp.append('(')
            elif x < depth:
                for i in range(depth - x):
                    tmp.append(')')
        depth = x
        tmp.append(str(x))
    while depth != 0:
        tmp.append(')')
        depth -= 1

    ans.append(''.join(tmp))





for i in range(len(ans)):
    print("Case #" + str(i + 1) + ": " + str(ans[i]))
