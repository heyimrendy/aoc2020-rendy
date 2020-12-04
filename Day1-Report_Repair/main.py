with open("./input.txt") as f:
    txt_file = f.readlines()

def part_one():
    done = False
    final_anwer = 0
    for i, content in enumerate(txt_file):
        for l, content2 in enumerate(txt_file):
            if i == l:
                continue

            if int(content.strip()) + int(content2.strip()) == 2020:
                final_anwer = int(content.strip()) * int(content2.strip())
                done = True
                break
        
        if done:
            break

    print('Part 1 final answer: {}'.format(final_anwer))

def part_two():
    done_root = False
    done_child = False
    final_anwer = 0
    for i, content in enumerate(txt_file):
        for l, content2 in enumerate(txt_file):
            if i == l:
                continue

            for m, content3 in enumerate(txt_file):
                if i == m or l == m:
                    continue

                if int(content.strip()) + int(content2.strip()) + int(content3.strip()) == 2020:
                    final_anwer = int(content.strip()) * int(content2.strip()) * int(content3.strip())
                    done_root = True
                    done_child = True
                    break
            
            if done_child:
                break
        
        if done_root:
            break

    print('Part 2 final answer: {}'.format(final_anwer))

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()