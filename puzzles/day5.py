def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data_order = set()
    data_update = []
    data_dict: dict[str,list[str]] = {}

    start_update = False

    for line in input:
        line = line.strip()
        if line == "":
            start_update = True
            continue
        if start_update:
            data_update.append(line.split(","))
        else:
            data_order.add(line)
            pair = line.split("|")
            if pair[0] not in data_dict:
                # data_dict[pair[0]] = set()
                data_dict[pair[0]] = []
            # data_dict[pair[0]].add(pair[1])
            data_dict[pair[0]].append(pair[1])

    return data_order, data_update, data_dict
            
def generate_orders(update: list[str]):
    result = set()

    for i in range (0, len(update)):
        for j in range (i+1, len(update)):
            result.add(update[i] + "|" + update[j])

    # print(f"Generated set: {control}")
    return result

def check_order(order, data_order):
    result = order & data_order
    # print(f"Intersection: {result} len of {len(result)} compared to {len(order)}")
    return len(result) == len(order)

def select_middle(update):
    index = int((len(update) - 1) / 2)
    # print(f"Middle element of {update} is {update[index]}")
    return int(update[index])

def fix_order(update, data_order):
    return update


def execute_part_one(input: list[str]) -> None:
    count = 0

    data_order, data_update, data_dict = extract_data(input)
    
    # print(data_order)
    # print(data_update)

    for du in data_update:
        # print(f"\n===>>>> Checking update: {du}")
        order = generate_orders(du)
        if check_order(order, data_order):
            count += select_middle(du)

    print(f"Solved 1: {count}")


def build_nodes_dict(order, full_dict):
    result = full_dict.copy()

    for k in list(result.keys()):
        # print(f"Result {k} of value {result[k]} in order: {k in order}")
        if k not in order:
            del result[k]

    # print(f"Final result: {result}")

    for k in list(result.keys()):
        # print(f"i: {k}, j: {result[k]}")
        lista = []
        for item in result[k]:
            # print(f"item {item} in order? {item in order}")
            if item in order:
                lista.append(item)
        result[k] = lista
    #    result[i][:] = [x for x in i if x in order]

    print (f"Modified dict: {result}")
    return result

def calculate_middle(nodes_dict, lenght):
    for k in list(nodes_dict.keys()):
        print(f"Item: {k}")
        if len(nodes_dict[k]) == lenght:
            print(f"Item found! {k}")
            return int(k)
    return 0


def execute_part_two(input: list[str]) -> None:
    count = 0
    data_order, data_update, data_dict = extract_data(input)
    
    # print(data_order)
    # print(data_update)
    print(f"data_dict: {data_dict}")

    orders_to_fix = []

    for du in data_update:
        # print(f"\n===>>>> Checking update: {du}")
        order = generate_orders(du)
        if not check_order(order, data_order):
            orders_to_fix.append(du)

    print(f"Orders to fix: {orders_to_fix}")

    for o in orders_to_fix:
        # transform order from list to set
        to_set = set(o)
        print(f"\nFixing order: {to_set}")

        #create empty dictionary of pairs
        order_nodes = build_nodes_dict(o, data_dict)
        # print(f"Order nodes: {order_nodes}")

        mid_len = int((len(o) - 1) / 2)
        print(f"Searching {o} for len: {mid_len}")
        count += calculate_middle(order_nodes, mid_len)

        # #iterate over all numbers in set
        # for i in to_set:
        #     # if number exists in 
        #     if i in data_dict:
        #         for e in data_dict[i]:


    print(f"Solved 2: {count}")
