import re

pattern = r"XMAS"


# horizontal works 
def search_word(text):
    matches = re.findall(pattern, text)
    return len(matches)


with open("problem.txt", "r") as file:
    counter = 0
    line_stack = []
    for line in file:
        line = line.strip()
        counter += search_word(line)
        counter += search_word(line[::-1])

        if not line_stack:
            line_stack = [[] for _ in range(len(line))]

        for i, char in enumerate(line):
            line_stack[i].append(char)



    vertical_lines = ["".join(col) for col in line_stack]

    counter += sum([search_word(line) for line in vertical_lines])
    counter += sum([search_word(line[::-1]) for line in vertical_lines])

    print(counter)

    # print(line_stack)
