counter = 0
int_list = []



f = open(r"C:\Users\Danell\Desktop\Advent of code\2021\demo.txt", "r")
for line in f.readlines():
   int_list.append(int(line))

#for i in range(1, len(int_list)):
#   if int_list[i - 1] < int_list[i]:
#      counter += 1


#print("Counter states:" + str(counter))

n = 3
for i in range(0, len(int_list)-n+1):
   batch = int_list[i:i+n]
   old_batch = int_list[i-n:i]
   total_batch = sum(batch)
   total_old = sum(old_batch)
   if total_batch > total_old and total_old != 0:
      counter += 1
   old_batch = batch
   print(batch, old_batch)
   print(total_batch, total_old)


print(counter)