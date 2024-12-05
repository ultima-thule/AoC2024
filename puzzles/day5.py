def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data_order = set()
    data_update = []

    start_update = False

    for l in input:
        l = l.strip()
        if l == "":
            start_update = True
            continue
        if start_update:
            data_update.append(l.split(","))
        else:
            data_order.add(l)

    return data_order, data_update
            
def generate_orders(update: list[str]):
    result = set()
    control = []
    for i in range (0, len(update)):
        for j in range (i+1, len(update)):
            result.add(update[i] + "|" + update[j])
            control.append(update[i] + "|" + update[j])

    print(f"Generated set: {control}")
    return result

def check_order(order, data_order):
    result = order & data_order
    print(f"Intersection: {result} len of {len(result)} compared to {len(order)}")
    return len(result) == len(order)

def select_middle(update):
    index = int((len(update) - 1) / 2)
    print(f"Middle element of {update} is {update[index]}")
    return int(update[index])

def execute_part_one(input: list[str]) -> None:
    count = 0

    data_order, data_update = extract_data(input)
    
    print(data_order)
    print(data_update)

    for du in data_update:
        print(f"\n===>>>> Checking update: {du}")
        order = generate_orders(du)
        if check_order(order, data_order):
            count += select_middle(du)

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    # for l in extract_data(input):
    #     pass

    print(f"Solved 2: {count}")
