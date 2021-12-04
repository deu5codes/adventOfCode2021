
with open("./2021/Day 3/input.txt") as file:
   data = file.read().split("\n")

columns = []

for column in range(len(max(data, key=len))):
   columns.append([n[column] for n in data])

gamma = ""
epsilon = ""

for column in columns:
   gamma += max(set(column), key = column.count)
   epsilon += min(set(column), key = column.count)

gamma = int(gamma, base=2)
epsilon = int(epsilon, base=2)

print(f"Gamma rate: {gamma}")
print(f"Epsilon rate {epsilon}")
print(f"Final result (multiplied): {gamma * epsilon}")