import re
from collections import defaultdict

config = {
    "R": 10,
    "S": 3,
    "V": 2,
}

pattern = re.compile(r'^(R|S|V)(\d+):\s')

def check_lines(filepath, cfg):
    found = defaultdict(set)
    with open(filepath, 'r', encoding="utf-8") as file:
        for line in file:
            match = pattern.match(line)
            if match:
                q_key = match.group(1)
                number = int(match.group(2))
                found[q_key].add(number)
    missing_entries = {}
    extra_entries = {}
    for q_key, max_count in cfg.items():
        expected_numbers = set(range(1, max_count+1))
        found_numbers = found[q_key]
        missing_numbers = expected_numbers - found_numbers
        extra_numbers = found_numbers - expected_numbers
        if extra_numbers:
            extra_entries[q_key] = sorted(extra_numbers)
        if missing_numbers:
            missing_entries[q_key] = sorted(missing_numbers)

    return missing_entries, extra_entries

if __name__ == "__main__":
    file_path = "README.md"
    (missing_questions, extra_questions) = check_lines(file_path, config)
    if len(extra_questions) != 0:
        print("\nExtra items found")
        for key, val in extra_questions.items():
            print(f"{key}: {', '.join(f"{key}{num}" for num in val)}")
    if len(missing_questions) == 0:
        print("\nNo missing items!")
    else:
        print("\nMissing items found")
        for key, val in missing_questions.items():
            print(f"{key}: {', '.join(f"{key}{num}" for num in val)}")

    print('\n')
