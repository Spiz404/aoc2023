
f = open("input.txt")

d = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e"
    }
total = 0
for l in f.readlines():

    for k,v in d.items():
        l = l.replace(k,v)
    
    digits = [c for c in l if c.isdigit()]
    n = int(digits[0]) * 10 + int(digits[-1]) 
    total = total + n

print(total)
