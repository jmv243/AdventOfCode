import re
input_file = "input/day3.txt"

def clean_file(input_file, pattern):
    with open(input_file, 'r') as file:
        content = file.read()
    
    # Find all matches that fit the 'mul(int,int)' format
    matches = re.findall(pattern, content)

    return matches

def part1():     
    matches = clean_file(input_file, r"mul\(\d+,\d+\)")
    total = 0
    for match in matches:
        num1 = int(match.split(',')[0].split('(')[1])
        num2 = int(match.split(',')[1].split(')')[0])
        total += num1 * num2
    
    print("Part1:", total)

def part2():
    matches = clean_file(input_file, r"(mul\(\d+,\d+\)|do\(\)|don't\(\))")
    total = 0
    enabled = True
    for match in matches:
        if match == "do()":
            enabled = True
            continue

        if match == "don't()":
            enabled = False
            continue

        if enabled:
            num1 = int(match.split(',')[0].split('(')[1])
            num2 = int(match.split(',')[1].split(')')[0])
            total += num1 * num2

    print("Part2:", total)


part1()
part2()