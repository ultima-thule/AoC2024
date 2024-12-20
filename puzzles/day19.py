from collections import defaultdict

def extract_data(input: list[str]):
    words = []
    grammar = defaultdict(defaultdict)
    max_len = 0
    
    for i in range(0, len(input)):
        line = input[i].strip()
        if i == 0:
            max_len = parse_grammar(line, grammar)
        elif len(line) > 0:
            words.append(line)

    print(f"Grammar: {grammar}")
    print(f"Words: {words}")
    print(f"Max len: {max_len}")

    return grammar, words, max_len

def parse_grammar(line, grammar):
    max_len = 0
    spl = line.split(", ")
    for i in spl:
        l = len(i)
        max_len = max(max_len, l)
        if l not in grammar:
            grammar[l] = {}
        grammar[l][i] = True
    return max_len

def check_grammar(word, grammar, max_len):
    found = False
    idx = 0

    print(f"Checking word {word} of len {len(word)}")

    for i in range(1, max_len + 1):
        print(f"Checking {word[:i]} in grammar {grammar[i]}: {word[:i] in grammar[i]} len check: {len(word) >= i}", end="")
        if len(word) >= i and word[:i] in grammar[i]:
            print(f"... found")
            idx = i
            break
        else:
            print(f"... not found")

    return idx


def execute_part_one(input: list[str]) -> None:
    count = 0

    grammar, words, max_len = extract_data(input)
    for w in words:
        pointer = 0
        print(f"\n => Checking word {w}")
        len_found = check_grammar(w[pointer:], grammar, max_len)
        print(f"Len found: {len_found}, pointer: {pointer}")
        while len_found > 0:
            pointer += len_found
            len_found = check_grammar(w[pointer:], grammar, max_len)
            print(f"Len found: {len_found}, pointer: {pointer}")

        if pointer == len(w) - 1 or pointer:
            print(f"=> Found a word: {w}")

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    grammar, words, max_len = extract_data(input)

    print(f"Solved 2: {count}")
