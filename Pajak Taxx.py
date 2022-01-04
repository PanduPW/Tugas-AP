brackets = {       0:0,
             1000000:5,
             3000000:10,
             6000000:15,
            10000000:20,
            20000000:25,
            35000000:30,
            55000000:35,
            80000000:40,
          }


def taxMaker(param):
    lastI = 0
    lastPercent = 0
    totalPajak = 0
    duit = param
    for x,i in brackets.items():
        loc = x - lastI
        lastI = x
        if loc > 0 and duit != 0 :
            if duit > loc:
                bebanPajak = loc * lastPercent / 100
                totalPajak += bebanPajak
                duit = duit - loc
            else:
                bebanPajak = duit * lastPercent / 100
                totalPajak += bebanPajak
                duit = 0
        lastPercent = i
    return int(totalPajak)
