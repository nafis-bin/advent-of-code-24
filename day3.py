import re



pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

pattern2 = r"don't\(\).*?do\(\)"

pattern3 = r"don't\(\).*"

with open("input.txt", "r") as file:

    total = 0

    content = file.read()

    content = re.sub(pattern2, "", content, flags=re.DOTALL)
    content = re.sub(pattern3, "", content, flags=re.DOTALL)

    matched = re.findall(pattern, content)
    matched_results = [int(x) * int(y) for x, y in matched]

    total += sum(matched_results)


    print(total)
            


