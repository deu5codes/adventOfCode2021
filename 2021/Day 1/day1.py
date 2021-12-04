with open("./2021/Day 1/input.txt") as file:
   data = [int(i) for i in file.read().split("\n")]

increases = 0

last = None
for i in data:
   if last != None:
      if i > last:
         increases += 1
      
   last = i

print(increases)