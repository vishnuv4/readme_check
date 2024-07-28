import os
import re
import logging
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from colorama import Fore,Style

config = {
    "R": 10,
    "I": 3,
    "S": 2,
    "C": 3,
    "V": 1
}

#pylint: disable=logging-fstring-interpolation
#pylint: enable=logging-not-lazy

pattern = re.compile(r'.*\((R|I|S|C|V)(\d+)\).*')

def print_red(string):
    print(f"{Fore.RED}{string}{Style.RESET_ALL}")

def print_green(string):
    print(f"{Fore.GREEN}{string}{Style.RESET_ALL}")

def print_yellow(string):
    print(f"{Fore.YELLOW}{string}{Style.RESET_ALL}")

def check_lines(filepath, cfg):
    found = defaultdict(set)
    duplicate_dict = defaultdict(str)
    line_numbers_dict = defaultdict(int)
    with open(filepath, 'r', encoding="utf-8") as file:
        for line_number, line in enumerate(file):
            match = pattern.search(line)
            if match:
                q_key = match.group(1)
                number = int(match.group(2))
                if number not in found[q_key]:
                    line_numbers_dict[(q_key + str(number))] = "Line " + f"{line_number + 1}"
                    found[q_key].add(number)
                else:
                    duplicate_dict["Line " + f"{line_number + 1}"] = q_key + str(number)
    missing_entries = defaultdict(set)
    extra_entries = defaultdict(set)
    for q_key, max_count in cfg.items():
        expected_numbers = set(range(1, max_count+1))
        found_numbers = found[q_key]
        missing_numbers = expected_numbers - found_numbers
        extra_numbers = found_numbers - expected_numbers
        if extra_numbers:
            extra_entries[q_key] = sorted(extra_numbers)
        if missing_numbers:
            missing_entries[q_key] = sorted(missing_numbers)

    extra_entries_tags = []
    for k,v in extra_entries.items():
        for num in v:
            extra_entries_tags.append(k + str(num))

    extra_entries_lines = defaultdict(str)
    with open(filepath, 'r', encoding="utf-8") as file:
        for line_number, line in enumerate(file):
            match = pattern.search(line)
            if match:
                q_key = match.group(1)
                number = int(match.group(2))
                if (q_key + str(number)) in extra_entries_tags:
                    extra_entries_lines["Line " + f"{line_number + 1}"] = q_key + str(number)

    return (missing_entries, extra_entries_lines, line_numbers_dict, duplicate_dict)

if __name__ == "__main__":
    LOG_PATH = Path('readme-check-logs')
    if not os.path.exists(LOG_PATH):
        os.makedirs(LOG_PATH)
    CURRENT_LOG = Path(str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-readme-check.txt")))
    FILE_PATH = "README.md"
    logging.basicConfig(level=logging.INFO,
                        format='%(message)s',
                        handlers=[
                            logging.FileHandler(LOG_PATH / CURRENT_LOG),
                            logging.StreamHandler()
                        ])
    (missing_questions, extra_questions, included_items, duplicates) = check_lines(FILE_PATH, config)

    incomplete_flag = False
    warning_flag = False

    logging.info("\nINCLUDED:")
    if len(included_items) != 0:
        for key,val in included_items.items():
            logging.info(f"{key}\t{val}")
    else:
        logging.info("NONE")

    logging.info("\nDUPLICATE:")
    if len(duplicates) != 0:
        incomplete_flag = True
        warning_flag = True
        for key, val in duplicates.items():
            logging.info(f"{val}\t{key}")
    else:
        logging.info("NONE")

    logging.info("\nEXTRA:")
    if len(extra_questions) != 0:
        incomplete_flag = True
        warning_flag = True
        for key, val in extra_questions.items():
            logging.info(f"{val}\t{key}")
    else:
        logging.info("NONE")
    
    logging.info("\nMISSING:")
    if len(missing_questions) != 0:
        incomplete_flag = True
        warning_flag = False
        for key, val in missing_questions.items():
            logging.info(f"{key}: {', '.join(f"{key}{num}" for num in val)}")
    else:
        logging.info("NONE")

    if incomplete_flag == False:
        print_green('\n')
        print_green("=============")
        print_green("You are done!")
        print_green("=============")
    else:
        if warning_flag == True:
            print_yellow('\n')
            print_yellow("====================")
            print_yellow("You are almost done!")
            print_yellow("====================")
        else:
            print_red('\n')
            print_red("=================")
            print_red("You are not done!")
            print_red("=================")
    logging.info('\n')
