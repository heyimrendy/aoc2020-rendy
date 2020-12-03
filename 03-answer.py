with open("./03-input.txt") as f:
    map_coor = [coor.strip() for coor in f.readlines()]

def part_one():
    n = 0
    max_n = len(map_coor) - 1
    x_coor = 0
    max_map = len(map_coor[0]) - 1
    found_tree = 0
    
    while n < max_n:
        x_coor += 3
        if x_coor > max_map:
            x_coor = x_coor - max_map - 1
        n += 1
        if map_coor[n][x_coor] == '#':
            found_tree += 1
    print("Part 1 answer: {}".format(found_tree))

def part_two(x_speed, y_speed):
    n = 0
    max_n = len(map_coor) - 1
    x_coor = 0
    max_map = len(map_coor[0]) - 1
    found_tree = 0
    
    while n < max_n:
        x_coor += x_speed
        if x_coor > max_map:
            x_coor = x_coor - max_map - 1
        n += y_speed
        if map_coor[n][x_coor] == '#':
            found_tree += 1
    return found_tree

def main():
    part_one()
    
    total_part_two = 1
    for i in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
        total_part_two *= part_two(i[0], i[1])
    
    print("Part 2 answer: {}".format(total_part_two))
if __name__ == "__main__":
    main()