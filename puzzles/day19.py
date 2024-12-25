from collections import defaultdict
import functools

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

    # print(f"Grammar: {grammar}")
    # print(f"Words: {words}")
    # print(f"Max len: {max_len}")

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

def execute_part_one(input: list[str]) -> None:
    count = 0

    grammar, words, max_len = extract_data(input)

    results = defaultdict(bool)
    saved = {}

    @functools.cache
    def is_valid(word) -> bool:
        return word in grammar[len(word)] or any(is_valid(word[0:i]) and is_valid(word[i:]) for i in range(1, len(word)))

    for w in words:
        if is_valid(w):
            count += 1
        # print(f"\n => Checking word {w}: {ret}")

    # print(f"Results size: {len(results)}")
    # print(f"Results: {results}")
    # print(f"Saved: {saved}")

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    grammar, words, max_len = extract_data(input)

    print(f"Solved 2: {count}")
