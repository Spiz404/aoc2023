f = open('input.txt')

lines = f.readlines()

nstrings = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
total = 0
for l in lines:
    fi = 10
    li = -1 
    fv = 0
    lv = 0 
    for k,v in nstrings.items():
        s = l 
        s = s.replace(k,str(v))
        print(s)
        print("replacing " + k)
        nums = [c for c in s if c.isdigit()]
        print(nums)
        if len(nums) != 0:
            if s.index(nums[0]) < fi:
                fi = s.index(nums[0])            
                fv = int(nums[0])
            if s.index(nums[-1]) > li:
                fi = s.index(nums[-1])
                fv = int(nums[-1])
    number = 10 * fv + lv 
    print(number)
    total = total + number
print(total)   
