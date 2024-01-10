input1 = open('./input.txt')
lines = input1.readlines()
total = 0

for s in lines:
    nums = [c for c in s if c.isdigit()]
    num = int(nums[0])*10 + int(nums[-1])
    print(num)
    total = total + num

print("total sum: " + str(total))
