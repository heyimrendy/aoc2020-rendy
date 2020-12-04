with open("./input.txt") as f:
    text_list = [ text.strip() for text in f.readlines()]

def part_one():
    total_correct = 0
    for task in text_list:
        task_rules = task.split(' ')
        min_pass = int(task_rules[0].split('-')[0])
        max_pass = int(task_rules[0].split('-')[1])
        target_char = task_rules[1].split(':')[0]
        password = task_rules[2]
        
        if password.count(target_char) < min_pass or password.count(target_char) > max_pass:
            continue
        
        total_correct += 1

    print("Part 1 total password: {}".format(total_correct))

def part_two():
    total_correct = 0
    for task in text_list:
        task_rules = task.split(' ')
        first_index = int(task_rules[0].split('-')[0]) - 1
        second_index = int(task_rules[0].split('-')[1]) - 1
        target_char = task_rules[1].split(':')[0]
        password = task_rules[2]

        if (password[first_index] == target_char and password[second_index] != target_char) or (password[first_index] != target_char and password[second_index] == target_char):
            total_correct += 1
    print("Part 2 total password: {}".format(total_correct))

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()