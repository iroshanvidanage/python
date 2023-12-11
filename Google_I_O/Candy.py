def candy(N, M, C):
    total_candy = sum(C)
    return total_candy % M


answer = []

for _ in range(int(input())):
    (N, M) = map(int, input().split())
    C = [int(x) for x in input().split()]

    answer.append(candy(N, M, C))

for _ in range(len(answer)):
    print('Case #' + str(_+1) + ': ' + str(answer[_]))
