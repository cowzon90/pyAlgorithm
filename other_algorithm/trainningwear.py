
def solution(n:int, lost:list, reserve:list):

    vector = [1] * n

    for index in lost:
        vector[index-1] -= 1

    for index in reserve:
        vector[index-1] += 1

    count = 0

    # index 0
    if vector[0] == 0:
        if vector[1] == 2:
            vector[0] = 1
            vector[1] = 1
            count += 1
    else:
        count += 1

    # index last
    if vector[n-1] == 0:
        if vector[n-2] == 2:
            vector[n-1] = 1
            vector[n-2] = 1
            count += 1
    else:
        count += 1

    for index in range(1, len(vector) - 1):
        if vector[index] == 0:
            if vector[index - 1] == 2:
                vector[index] += 1
                vector[index - 1] -= 1
                count += 1
            elif vector[index + 1] == 2:
                vector[index] += 1
                vector[index + 1] -= 1
                count += 1
            else:
                pass
        else:
            count += 1

    return count

n = 3
lost = [3]
reserve = [1]

print(solution(n, lost, reserve))
