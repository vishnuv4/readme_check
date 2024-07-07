import os
import re
import logging
from collections import defaultdict
from datetime import datetime
from pathlib import Path

config = {
    "R": 10,
    "S": 3,
    "V": 2,
    "C": 3
}


#pylint: disable=logging-fstring-interpolation
#pylint: enable=logging-not-lazy

pattern = re.compile(r'^(R|S|V|C)(\d+):\s')

def check_lines(filepath, cfg):
    found = defaultdict(set)
    line_numbers_dict = defaultdict(int)
    with open(filepath, 'r', encoding="utf-8") as file:
        for line_number, line in enumerate(file):
            match = pattern.match(line)
            if match:
                q_key = match.group(1)
                number = int(match.group(2))
                line_numbers_dict[(q_key + str(number))] = "Line " + f"{line_number + 1}"
                found[q_key].add(number)
    missing_entries = defaultdict(int)
    extra_entries = defaultdict(int)
    for q_key, max_count in cfg.items():
        expected_numbers = set(range(1, max_count+1))
        found_numbers = found[q_key]
        missing_numbers = expected_numbers - found_numbers
        extra_numbers = found_numbers - expected_numbers
        if extra_numbers:
            extra_entries[q_key] = sorted(extra_numbers)
        if missing_numbers:
            missing_entries[q_key] = sorted(missing_numbers)

    return missing_entries, extra_entries, line_numbers_dict

if __name__ == "__main__":
    LOG_PATH = Path('readme-check-logs')
    if not os.path.exists(LOG_PATH):
        os.makedirs(LOG_PATH)
    CURRENT_LOG = Path(str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-readme-check.log")))
    FILE_PATH = "README.md"
    logging.basicConfig(level=logging.INFO,
                        format='%(message)s',
                        handlers=[
                            logging.FileHandler(LOG_PATH / CURRENT_LOG ),  # Log to a file
                            logging.StreamHandler()  # Log to the console
                        ])
    (missing_questions, extra_questions, line_no) = check_lines(FILE_PATH, config)
    logging.info("\nIncluded items:")
    for k,v in line_no.items():
        logging.info(f"{k}: \t{v}")
    if len(extra_questions) != 0:
        logging.info("\nExtra items:")
        for key, val in extra_questions.items():
            logging.info(f"{key}: {', '.join(f"{key}{num}" for num in val)}")
    if len(missing_questions) == 0:
        logging.info("\nNo missing items!")
    else:
        logging.info("\nMissing items:")
        for key, val in missing_questions.items():
            logging.info(f"{key}: {', '.join(f"{key}{num}" for num in val)}")

    logging.info('\n')
