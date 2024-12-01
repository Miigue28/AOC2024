"""
    Advent of Code 2024 - Day 1
    Miguel Ángel Moreno Castro
"""

def parse_input():
    filename: str = "inputs/day01.txt"
    left_column = []
    right_column = []

    with open(filename, "r") as file:
        for line in file.readlines():
            chars = line.strip().split()

            if (len(chars) == 2):
                left_column.append(int(chars[0]))
                right_column.append(int(chars[1]))
            else:
                print(f"[!] Skipping malformed line: {line}")

    return left_column, right_column

def measure_distance(left: list, right: list):
    distance: int = 0

    for i in range(len(left)):
        distance += abs(left[i] - right[i])
    
    return distance

def similarity_score(left: list, right: list):
    score: int = 0

    for id in left:
        score += id * right.count(id)

    return score


def main():
    left_column, right_column = parse_input()

    total_distance = measure_distance(sorted(left_column), sorted(right_column))
    print(f"The total distance between both lists is {total_distance}")

    total_score = similarity_score(left_column, right_column)
    print(f"The similarity score between both lists is {total_score}")

if __name__ == "__main__":
    main()