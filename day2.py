def is_safe(report):
    diffs = [report[i+1] - report[i] for i in range(len(report) - 1)]

    if all(1 <= d <= 3 for d in diffs):
        return True

    if all(-3 <= d <= -1 for d in diffs):
        return True


def is_safe_with_dampner(report):
    if is_safe(report):
        return True

    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if is_safe(new_report):
            return True
    
    return False



with open("input.txt", "r") as file:
    reports = []
    for line in file:
        line = [int(x) for x in line.strip().split()]
        reports.append(line)

    safe_count = 0
    for report in reports:
        if is_safe_with_dampner(report):
            safe_count += 1

    print(safe_count)
            

