f = open("input.txt")
result = 0



for l in f.readlines():
    valid_game = True
    extractions = True
    ex = []

    game_id = int(l[4:l.index(":")])
    infos = l[l.index(":")+1:]

    RED_MAX = 0
    GREEN_MAX = 0
    BLUE_MAX = 0

    while extractions:
        extractions = False
        extr = infos
        if ";" in infos:
            extractions = True
            extr = infos[:infos.index(";")]
            infos = infos[infos.index(";") + 1:]
        ex.append(extr)

    
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
            if color == "red" and val > RED_MAX:
                RED_MAX = val
            elif color == "green" and val > GREEN_MAX:
                GREEN_MAX = val                

            elif color == "blue" and val > BLUE_MAX:
                BLUE_MAX = val

    result += BLUE_MAX * RED_MAX * GREEN_MAX

print(result)
