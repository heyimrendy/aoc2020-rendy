import copy

with open('./input.txt') as f:
    data_txt = [data.strip() for data in f.readlines()]

def part_one():
    map_ins = [[data, 0] for data in data_txt]
    running = True
    curr_pos = 0
    total = 0
    while running:
        if map_ins[curr_pos][1] == 1:
            break
        operation = map_ins[curr_pos][0].split(" ")[0]
        argument = int(map_ins[curr_pos][0].split(" ")[1])
        if operation == "nop":
            map_ins[curr_pos][1] += 1
            curr_pos += 1
        elif operation == "acc":
            map_ins[curr_pos][1] += 1
            total += argument
            curr_pos += 1
        else:
            if argument == 0:
                map_ins[curr_pos][1] += 1
                curr_pos += 1
            else:
                map_ins[curr_pos][1] += 1
                curr_pos += argument

    print("Part 1 answer: {}".format(total))

def part_two():
    map_ins = [[data, 0] for data in data_txt]
    for i, data in enumerate(map_ins):
        operation = map_ins[i][0].split(" ")[0]
        argument = int(map_ins[i][0].split(" ")[1])
        if operation == "nop" and argument != 0:
            map_temp = copy.deepcopy(map_ins)
            map_temp[i][0] = map_temp[i][0].replace('nop', 'jmp')
            found, total = search_opr(map_temp)
            if found:
                print("Part 2 answer: {}".format(total))
                break
        elif operation == "jmp":
            map_temp = copy.deepcopy(map_ins)
            map_temp[i][0] = map_temp[i][0].replace('jmp', 'nop')
            found, total = search_opr(map_temp)
            if found:
                print("Part 2 answer: {}".format(total))
                break
            
def search_opr(map_temp):
    running = True
    curr_pos = 0
    total = 0
    found = False
    while running:
        if curr_pos == len(map_temp):
            running = False
            found = True
            break

        if map_temp[curr_pos][1] == 1:
            running = False
            found = False
            break

        operation = map_temp[curr_pos][0].split(" ")[0]
        argument = int(map_temp[curr_pos][0].split(" ")[1])
        
        if operation == "nop":
            map_temp[curr_pos][1] += 1
            curr_pos += 1
        elif operation == "acc":
            map_temp[curr_pos][1] += 1
            total += argument
            curr_pos += 1
        else:
            map_temp[curr_pos][1] += 1
            curr_pos += argument
    
    return found, total

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()