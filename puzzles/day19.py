from collections import defaultdict
import functools

def extract_data(input: list[str]):
    words = []
    grammar = defaultdict(defaultdict)
    
    for i in range(0, len(input)):
        line = input[i].strip()
        if i == 0:
            max_len = parse_grammar(line, grammar)
        elif len(line) > 0:
            words.append(line)

    return grammar, words

def parse_grammar(line, grammar):
    spl = line.split(", ")
    for i in spl:
        l = len(i)
        if l not in grammar:
            grammar[l] = {}
        grammar[l][i] = True

def execute_part_one(input: list[str]) -> None:
    count = 0

    grammar, words = extract_data(input)

    @functools.cache
    def is_valid(word) -> bool:
        return word in grammar[len(word)] or any(is_valid(word[0:i]) and is_valid(word[i:]) for i in range(1, len(word)))

    for w in words:
        count += 1 if is_valid(w) else 0

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    grammar, words = extract_data(input)

    @functools.cache
    def count_possibilities(word) -> int:
        return (word in grammar[len(word)]) + sum(count_possibilities(word[i:]) for i in range(1, len(word)) if word[0:i] in grammar[len( word[0:i])])

    for w in words:
        count += count_possibilities(w)

    print(f"Solved 2: {count}")
