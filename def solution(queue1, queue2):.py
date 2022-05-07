def solution(queue1, queue2):
    answer = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    print(sum1,sum2)

    if (sum1 + sum2)%2 == 1:
        answer = -1
        return answer
    a = 0
    q1 = len(queue1)
    q2 = len(queue2)
    
    a = q1 + q2
    i = 0
    j = 0
    while(sum1 != sum2):
        
        if sum1 > sum2:
            if i < q1:
                sum2 = sum2 + queue1[i]
                sum1 = sum1 - queue1[i]
            else:
                sum2 = sum2 + queue2[i- q1]
                sum1 = sum1 - queue2[i- q1]
            i = i + 1


        else:
            if j < q2:
                sum2 = sum2 - queue2[j]
                sum1 = sum1 + queue2[j]
            else:
                sum2 = sum2 - queue1[j- q2]
                sum1 = sum1 + queue1[j- q2]
            j = j + 1

        if answer > a+1:
            answer = -1
            break

        answer +=1
    

    return answer