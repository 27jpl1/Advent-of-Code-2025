file = open("Math", "r").readlines()

problems = []
for line in file:
    line = line.strip().split()
    problems.append(line)

total = 0
for i in range(len(problems[0])):
    if problems[len(problems) - 1][i] == "*":
        problem_total = 1
        for j in range(len(problems) - 1):
            problem_total *= int(problems[j][i])
    elif problems[len(problems) - 1][i] == "+":
        problem_total = 0
        for j in range(len(problems) - 1):
            problem_total += int(problems[j][i])
    total += problem_total

print(total)