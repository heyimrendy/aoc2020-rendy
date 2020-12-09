with open("./input.txt") as f:
    txt_list = f.read().splitlines()

txt_list = [int(data) for data in txt_list]

def part_one():
    n_low = 0
    n_max = 25
    running = True

    while running:
        curr_list = txt_list[n_low:n_max]
        val = txt_list[n_max]
        found = False

        for data in curr_list:
            target_n = val - data
            if target_n != val and target_n in curr_list:
                found = True
                break

        if not found:
            print("Part 1 answer: {}".format(val))
            running = False
            break
        n_low += 1
        n_max += 1
        
        if n_max >= len(txt_list):
            running = False

def part_two():
    n_low = 0
    n_max = 25
    running = True

    while running:
        curr_list = txt_list[n_low:n_max]
        val = txt_list[n_max]
        found = False

        for data in curr_list:
            target_n = val - data
            if target_n != val and target_n in curr_list:
                found = True
                break

        if not found:
            curr_list = txt_list[0:n_max]

            for i in range(len(curr_list)):
                stop_loop = False
                for j in range(i, len(curr_list)):
                    target_list = curr_list[i+1:j]
                    sum_target = sum(target_list)
                    if sum_target == val:
                        sum_total = min(target_list) + max(target_list)
                        print("Part 2 answer: {}".format(sum_total))
                        stop_loop = True
                        break
                if stop_loop:
                    running = False
                    break
        n_low += 1
        n_max += 1
        
        if n_max >= len(txt_list):
            running = False

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()