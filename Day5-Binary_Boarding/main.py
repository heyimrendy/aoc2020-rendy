with open("./input.txt") as f:
    seat_data = [txt.strip() for txt in f.readlines()]

def part_one():
    lowest_id = None
    for data in seat_data:
        n_low = 0
        n_high = 127
        for char in data[:7]:
            if char == 'F':
                n_high = n_low + ((n_high - n_low + 1) / 2) - 1
            else:
                n_low = n_low + ((n_high - n_low + 1) / 2)
        column_low = 0
        column_high = 7
        for char in data[7:]:
            if char == 'L':
                column_high = column_low + ((column_high - column_low + 1) / 2) - 1
            else:
                column_low = column_low + ((column_high - column_low + 1) / 2)
        seat_id = int(n_high) * 8 + int(column_high)
        if lowest_id is None or lowest_id < seat_id:
            lowest_id = seat_id

    print("Part 1 answer: {}".format(lowest_id))

def part_two():
    seat_list = []
    for data in seat_data:
        n_low = 0
        n_high = 127
        for char in data[:7]:
            if char == 'F':
                n_high = n_low + ((n_high - n_low + 1) / 2) - 1
            else:
                n_low = n_low + ((n_high - n_low + 1) / 2)
        column_low = 0
        column_high = 7
        for char in data[7:]:
            if char == 'L':
                column_high = column_low + ((column_high - column_low + 1) / 2) - 1
            else:
                column_low = column_low + ((column_high - column_low + 1) / 2)
        seat_id = int(n_high) * 8 + int(column_high)
        seat_list.append(seat_id)
    seat_list = sorted(seat_list)

    for i in range(seat_list[0], seat_list[-1] + 1):
        if i not in seat_list and (i - 1) in seat_list and (i + 1) in seat_list:
            print("Part 2 answer: {}".format(i))

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()