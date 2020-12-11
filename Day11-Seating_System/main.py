import copy

with open("./input.txt") as f:
    txt_data = [data for data in f.read().splitlines()]
width_len = len(txt_data[0])
height_len = len(txt_data)

def part_one():
    txt_data_one = copy.deepcopy(txt_data)
    mode = 1
    running = True
    map_seat = {"L": 0, ".": 0, "#": 0}
    while running:
        new_seat = []
        people_move = False
        for i, el in enumerate(txt_data_one):
            new_seat.append([])
            for j, data in enumerate(el):
                if data == 'L' or data == '#':
                    map_seat["L"] = 0
                    map_seat["."] = 0
                    map_seat["#"] = 0
                    if i-1 > -1:
                        # Center top
                        map_seat[txt_data_one[i-1][j]] += 1

                    if i+1 < height_len:
                        # Center bot
                        map_seat[txt_data_one[i+1][j]] += 1

                    if j-1 > -1:
                        # Left mid
                        map_seat[txt_data_one[i][j-1]] += 1
                        if i-1 > -1:
                            # Left top
                            map_seat[txt_data_one[i-1][j-1]] += 1
                        if i+1 < height_len:
                            # Left bot
                            map_seat[txt_data_one[i+1][j-1]] += 1
                    
                    if j+1 < width_len:
                        # Right mid
                        map_seat[txt_data_one[i][j+1]] += 1
                        if i-1 > -1:
                            # Right top
                            map_seat[txt_data_one[i-1][j+1]] += 1
                        if i+1 < height_len:
                            # Right bot
                            map_seat[txt_data_one[i+1][j+1]] += 1
                    
                    if mode == 1 and data == 'L' and map_seat['#'] < 1:
                        new_seat[i].append('#')
                        people_move = True
                    elif mode == 2 and data == '#' and map_seat['#'] >= 4:
                        new_seat[i].append('L')
                        people_move = True
                    else:
                        new_seat[i].append(data)
                else:
                    new_seat[i].append(data)
            new_seat[i] = "".join(new_seat[i])

        # Swap seats
        for i, val in enumerate(new_seat):
            txt_data_one[i] = val
        
        # Swap mode
        if mode == 1:
            mode = 2
        else:
            mode = 1
        
        if not people_move:
            running = False
        
        del new_seat
    
    count_occupied = 0
    for v in txt_data_one:
        count_occupied += v.count("#") 
    print("Part 1 answer: {}".format(count_occupied))

def part_two():
    move_data = []
    for i, val in enumerate(txt_data):
        move_data.append([])
        for j, data in enumerate(val):
            move_data[i].append([])
            if data != ".":
                # Center top
                n = i - 1
                while n > -1:
                    if txt_data[n][j] == "L" or txt_data[n][j] == "#":
                        move_data[i][j].append((n, j))
                        break
                    n -= 1

                # Center bot
                n = i + 1
                while n < height_len:
                    if txt_data[n][j] == "L" or txt_data[n][j] == "#":
                        move_data[i][j].append((n, j))
                        break
                    n += 1

                # Left mid
                n = j - 1
                while n > -1:
                    if txt_data[i][n] == "L" or txt_data[i][n] == "#":
                        move_data[i][j].append((i, n))
                        break
                    n -= 1

                # Right mid
                n = j + 1
                while n < width_len:
                    if txt_data[i][n] == "L" or txt_data[i][n] == "#":
                        move_data[i][j].append((i, n))
                        break
                    n += 1

                # Left top
                n = i - 1
                m = j - 1
                while n > -1 and m > -1:
                    if txt_data[n][m] == "L" or txt_data[n][m] == "#":
                        move_data[i][j].append((n, m))
                        break
                    n -= 1
                    m -= 1

                # Left bot
                n = i + 1
                m = j - 1
                while n < height_len and m > -1:
                    if txt_data[n][m] == "L" or txt_data[n][m] == "#":
                        move_data[i][j].append((n, m))
                        break
                    n += 1
                    m -= 1

                # Right top
                n = i - 1
                m = j + 1
                while n > -1 and m < width_len:
                    if txt_data[n][m] == "L" or txt_data[n][m] == "#":
                        move_data[i][j].append((n, m))
                        break
                    n -= 1
                    m += 1

                # Right bot
                n = i + 1
                m = j + 1
                while n < height_len and m < width_len:
                    if txt_data[n][m] == "L" or txt_data[n][m] == "#":
                        move_data[i][j].append((n, m))
                        break
                    n += 1
                    m += 1

    running = True
    mode = 1
    map_seat = {"L": 0, "#": 0}
    while running:
        new_seat = []
        people_move = False
        for i, val in enumerate(txt_data):
            new_seat.append([])
            for j, data in enumerate(val):
                map_seat["L"] = 0
                map_seat["#"] = 0
                for move_v in move_data[i][j]:
                    map_seat[txt_data[move_v[0]][move_v[1]]] += 1

                if mode == 1 and data == 'L' and map_seat['#'] < 1:
                    new_seat[i].append("#")
                    people_move = True
                elif mode == 2 and data == '#' and map_seat['#'] >= 5:
                    new_seat[i].append("L")
                    people_move = True
                else:
                    new_seat[i].append(data)
            new_seat[i] = "".join(new_seat[i])

        # Swap seats
        for i, val in enumerate(new_seat):
            txt_data[i] = val
        
        # Swap mode
        if mode == 1:
            mode = 2
        else:
            mode = 1
        
        if not people_move:
            running = False
        
        del new_seat

    count_occupied = 0
    for v in txt_data:
        count_occupied += v.count("#") 
    print("Part 2 answer: {}".format(count_occupied))

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()