with open("./input.txt") as f:
    txt = []
    txt_list = []
    for data in f.readlines():
        if data.strip() == '':
            txt_list.append(txt)
            txt = []
            continue
        txt.append(data.strip())
    txt_list.append(txt)

def part_one():
    total = 0
    for quest in txt_list:
        total += len(set("".join(quest)))

    print("Part 1 answer: {}".format(total))

def part_two():
    total = 0
    for quest in txt_list:
        total += len(set.intersection(*map(set,quest)))

    print("Part 2 answer: {}".format(total))

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()