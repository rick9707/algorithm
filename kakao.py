def solution(alp, cop, problems):
    answer = 0
    b = 0
    c = 0
    lenP = len(problems)
    for i in range(len(problems)):
        if problems[i][0] > b:
            b = problems[i][0]

    for i in range(len(problems)):
        if problems[i][1] > c:
            c = problems[i][1]
    alpFin = b
    copFin = c

    s =0
    al = 0
    ali = 0
    alii = 0
    num = -1
    mi = 301
    minum = 0
    mintime = 900
    for i in range(lenP):
        if (problems[i][0] + problems[i][1])< mi:
            mi = problems[i][0] + problems[i][1]
            minum = i
    print(problems[minum][0],problems[minum][1],answer,minum)

    alp1 = problems[minum][0]
    cop1 = problems[minum][1]
    answer = alp1 + cop1 - alp - cop
    print(problems[minum][0],problems[minum][1],answer,minum)

    while(True):
        if alp1 >= alpFin:
            if problems[num][3] > (copFin-cop1):
                for j in range(lenP):
                    if problems[j][3] > (copFin-cop1): 
                        if problems[j][4] < mintime:
                            mintime = problems[j][4] 
                            s = j
                if (copFin-cop1) == 1:
                    answer = answer + 1
                    return answer
                    
                answer = answer + mintime
                return answer

            for i in range(lenP):
                if problems[i][0] <= alp1 and problems[i][1] <=cop1:
                    if (problems[i][3]/problems[i][4] > ali and (problems[i][3])/problems[i][4]) > 1:
                        ali = (problems[i][3])/problems[i][4]
                        num = i
                        
        elif cop1 >= copFin:
            if problems[num][2] > (alpFin-alp1):
                for j in range(lenP):
                    if problems[j][2] > (alpFin-alp1):
                        if problems[j][4] < mintime:
                            mintime = problems[j][4] 
                answer = answer + mintime
                return answer

            for i in range(lenP):
                if problems[i][0] <= alp1 and problems[i][1] <=cop1:
                    if (problems[i][2]/problems[i][4] > ali and (problems[i][2])/problems[i][4]) > 1:
                        alii = (problems[i][2])/problems[i][4]
                        num = i

        else:
            for i in range(lenP):
                if problems[i][0] <= alp1 and problems[i][1] <=cop1:
                    if (problems[i][2] + problems[i][3])/problems[i][4] > al and (problems[i][2] + problems[i][3])/problems[i][4] > 1:
                        al = (problems[i][2] + problems[i][3])/problems[i][4]
                        num = i

        alp1 = alp1 + problems[num][2]
        cop1 = cop1 + problems[num][3]
        answer = answer + problems[num][4]

        if alp1 >= alpFin and cop1 >=copFin:
            return answer

    return answer