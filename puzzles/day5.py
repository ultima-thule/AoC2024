def extract_data(input: list[str]):
    '''Extracts and transforms input text data'''
    ordering_rules = set()
    page_numbers: list[list[str]] = []
    ordering_rules_aggr: dict[str,list[str]] = {}

    start_page_numbers = False

    for line in input:
        line = line.strip()
        # section with page numbers starts
        if line == "":
            start_page_numbers = True
            continue

        if start_page_numbers:
            # turn each update into list of pages
            page_numbers.append(line.split(","))
        else: 
            # save ordering rules in a list of pages
            ordering_rules.add(line)
            
            # save ordering rules as dict of pages following the key page
            pair = line.split("|")
            if pair[0] not in ordering_rules_aggr:
                ordering_rules_aggr[pair[0]] = []
            ordering_rules_aggr[pair[0]].append(pair[1])

    return ordering_rules, page_numbers, ordering_rules_aggr
            
def generate_ordering_rules(pages: list[str]) -> set:
    '''Generates all possible ordering rules for a given list of pages'''
    all_rules = set()

    for i in range (0, len(pages)):
        for j in range (i+1, len(pages)):
            all_rules.add(pages[i] + "|" + pages[j])

    return all_rules

def check_rules(current_rules: set, all_ordering_rules: set, missing_only: bool) -> bool:
    '''Checks whether ordering rules for current update are present (or not, based on missing_only variable) in all rules set'''
    result = current_rules & all_ordering_rules
    all_present = (len(result) == len(current_rules))
    return all_present is False if missing_only else all_present is True

def select_middle_page(rules_subset: dict[str,list[str]], no_of_followers: int) -> int:
    '''Selects page in the middle of ordering rules subset based on number of pages that follow it'''
    for k in rules_subset:
        if len(rules_subset[k]) == no_of_followers:
            return int(k)
    return 0

def build_ordering_rules_subset(pages_update: list[str], ordering_rules_all: dict[str,list[str]]) -> dict[str,list[str]]:
    '''Selects only those ordering rules which consist of pages included in a single update '''
    ordering_rules_subset = ordering_rules_all.copy()

    # delete rules for all pages not present in the update
    for k in list(ordering_rules_subset.keys()):
        if k not in pages_update:
            del ordering_rules_subset[k]

    # delete all followers which are not pages present in the update
    for k in ordering_rules_subset:
        subset = []
        for item in ordering_rules_subset[k]:
            if item in pages_update:
                subset.append(item)
        ordering_rules_subset[k] = subset

    return ordering_rules_subset


def calculate_pages_sum(input: list[str], fix_invalid: bool) -> int:
    '''Calculates the sum of pages number which are valid (scenario 1) or needs fixing (scenario 2)'''
    page_numbers_sum = 0
    all_ordering_rules, pages_update, ordering_rules_aggr = extract_data(input)
    
    for pu in pages_update:
        current_rules = generate_ordering_rules(pu)
        if check_rules(current_rules, all_ordering_rules, fix_invalid):
            rules_subset = build_ordering_rules_subset(pu, ordering_rules_aggr)

            no_of_followers = int((len(pu) - 1) / 2)
            page_numbers_sum += select_middle_page(rules_subset, no_of_followers)

    return page_numbers_sum

def execute_part_one(input: list[str]) -> None:
    print(f"Solved 1: {calculate_pages_sum(input, False)}\n")

def execute_part_two(input: list[str]) -> None:
    print(f"Solved 2: {calculate_pages_sum(input, True)}\n")
