f = open("input.txt")

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14
result = 0
#print("RED_MAX " + str(RED_MAX))
#print("GREEN_MAX " + str(GREEN_MAX))
#print("BLUE_MAX " + str(BLUE_MAX))



for l in f.readlines():
    valid_game = True
    extractions = True
    ex = []

    game_id = int(l[4:l.index(":")])
    infos = l[l.index(":")+1:]

    while extractions:
        extractions = False
        extr = infos
        if ";" in infos:
            extractions = True
            extr = infos[:infos.index(";")]
            infos = infos[infos.index(";") + 1:]
        ex.append(extr)

    #print(ex)
    
    for e in ex:
        extraction = True
        while extraction:
            extraction = False
            s = e
            if "," in e:
                extraction = True
                s = e[:e.index(",")]
                e = e[e.index(",") + 1:]

            s = s.strip()
            val = ""
            for c in s:
                if c == " ":
                    break
                else:
                    val = val + c
            val = int(val)
            color = s[len(str(val))+1:].strip()
            #print("color " + color + " value: " + str(val))
            if color == "red" and val > RED_MAX or \
                    color == "green" and val > GREEN_MAX or \
                    color == "blue" and val > BLUE_MAX:
                valid_game = False
    if valid_game: 
        result = result + game_id
        #print("game " + str(game_id) + " valid")

print(result)
