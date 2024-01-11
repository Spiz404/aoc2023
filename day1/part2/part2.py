import math
f = open('input.txt')

lines = f.readlines()

nstrings = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
total = 0
for l in lines:
    fi = math.inf
    li = -1 
    fv = 0
    lv = 0 
    for k,v in nstrings.items():
        s = l 
        if k in s:
            i = s.index(k)
            ir = s.rindex(k)
            if i < fi:
                fi = i
                fv = v
            if ir > li:
                li = ir
                lv = v
    
    nums = [c for c in l if c.isdigit()]
    if len(nums) > 0:
        if s.index(nums[0]) < fi:
            fv = int(nums[0])
        if s.index(nums[-1]) > li:
            lv = int(nums[-1])

    number = fv * 10 + lv
    total = total + number
print(total)
