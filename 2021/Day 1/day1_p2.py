with open("./2021/Day 1/input.txt") as file:
   data = [int(i) for i in file.read().split("\n")]

increases = 0

last = None
for i, measurement in enumerate(data):
   if i + 2 >= len(data):
      break

   current = data[i] + data[i+1] + data[i+2]

   if last != None:
      if current > last:
         increases += 1

   last = current


print(increases)