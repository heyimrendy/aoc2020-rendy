import copy
from itertools import permutations  

with open("./input.txt") as f:
    txt_list = [int(data) for data in f.read().splitlines()]
txt_list.sort()

def part_one():
    txt_data = copy.deepcopy(txt_list)
    txt_data.sort()
    n_one = 0
    n_three = 1
    if txt_list[0] - 1 == 0:
        n_one += 1
    elif txt_list[0] - 3 == 0:
        n_three += 1

    for data in txt_list:
        txt_data.pop(0)
        if len(txt_data) > 0:
            curr_data = txt_data[0]
            if curr_data - data == 1:
                n_one += 1
            elif curr_data - data == 2:
                pass
            elif curr_data - data == 3:
                n_three += 1
            else:
                print("Something wrong")
                break

    print("Part 1 answer: {}".format(n_one * n_three))

def part_two():
    cost = dict()
    cost[0] = 1
    if min(txt_list) <= 3:
        for i, data in enumerate(txt_list):
            if data not in cost:
                cost_1 = 0 if (data - 1) not in cost else cost[data - 1]
                cost_2 = 0 if (data - 2) not in cost else cost[data - 2]
                cost_3 = 0 if (data - 3) not in cost else cost[data - 3]
                sum_cost = cost_1 + cost_2 + cost_3
                cost[data] = sum_cost
        print("Part 2 answer: {}".format(cost[max(txt_list)]))
    else:
        print("Part 2 answer: 0")

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()