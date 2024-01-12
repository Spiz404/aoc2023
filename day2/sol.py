f = open("input.txt")

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14
res = 0
for l in f.readlines():
  
    # extracting game id
    game_id = int(l[4:l.index(":")])
    infos = l[l.index(":")+1:]
    extractions = True 
    print(20 * "_")
    print(l)
    valid = True
    while extractions and valid:
        valid = True
        # for each game, get single extractions
        extractions = False 
        if ";" in infos:  
            extractions = True
            g = infos[0: infos.index(";")]
            infos = infos[infos.index(";") +1:]
        else:
            g = infos
        
        comma = True
        while comma and valid:
            valid = True
            comma = False
            cg = g.strip()
            if "," in g:
                comma = True
                cg = g[0:g.index(",")]
                cg = cg.strip()
                g = g[g.index(",") + 1:]

            value = int(cg[0])
            color = (cg[1:].strip())
            print("color: " + color + " value: " + str(value))
            if color == "red" and value > RED_MAX or \
                color == "green" and value > GREEN_MAX or \
                color == "blue" and value > BLUE_MAX:
                   valid = False

            if "," not in cg: 
                break
    if valid:
        res = res + 1


print(res)
