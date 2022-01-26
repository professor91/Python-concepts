nums= []

for num in open('1_input.txt'):
    nums.append(int(num))

count= 0

for i in range(1999):
    if(nums[i+1] > nums[i]):
        count += 1

print(count)