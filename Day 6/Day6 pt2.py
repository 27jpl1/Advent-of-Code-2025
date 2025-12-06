file = open("Math", "r").readlines()

problems = []
for line in file:
    problems.append(line.strip("\n"))

final_problems =[]
for i in range(len(problems)):
    line = []
    for j in range(len(problems[i])):
        if j >= len(problems[i]) - 1:
            pass
        else:
            line.append(problems[i][j])
    line.append(problems[i][j])
    final_problems.append(line)

longest_length = 0
for line in final_problems:
    if len(line) > longest_length:
        longest_length = len(line)

for i, line in enumerate(final_problems):
    while len(line) < longest_length:
        final_problems[i].append(" ")

final_problems[len(final_problems) - 1].append(" ")
final_problems[len(final_problems) - 1].append("+")

total = 0
i = 0
while i < (len(final_problems[0]) - 1):
    if final_problems[len(final_problems) - 1][i] == "*":
        problem_total = 1
        while final_problems[len(final_problems) - 1][i + 1] != "*" and final_problems[len(final_problems) - 1][i + 1] != "+":
            numb = ""
            for j in range(len(final_problems) - 1):
                numb += final_problems[j][i]
            problem_total *= int(numb)
            i += 1
    if final_problems[len(final_problems) - 1][i] == "+":
        problem_total = 0
        while final_problems[len(final_problems) - 1][i + 1] != "*" and final_problems[len(final_problems) - 1][i + 1] != "+":
            numb = ""
            for j in range(len(final_problems) - 1):
                numb += final_problems[j][i]
            problem_total += int(numb)
            i += 1
    total += problem_total
    i += 1

print(total)