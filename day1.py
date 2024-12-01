def part1():
    left = []
    right = []

    with open('input/day1.txt', 'r') as file:
        for line in file:
            lineData = line.split()
            left.append(int(lineData[0]))
            right.append(int(lineData[1]))

    left.sort()
    right.sort()

    totalDistance = 0

    for i in range(len(left)):
        totalDistance += abs(left[i] - right[i])

    print(totalDistance)

    return

def part2():
    left = []
    right = []

    with open('input/day1.txt', 'r') as file:
        for line in file:
            lineData = line.split()
            left.append(int(lineData[0]))
            right.append(int(lineData[1]))

    similarityScore = 0

    for i in range(len(left)):
        multiplier = right.count(left[i])
        similarityScore += left[i] * multiplier

    print(similarityScore)

    return


#part1()
#part2()