with open("./input.txt") as f:
    txt_data = [data.strip() for data in f.readlines()]

def part_one():
    bag_list = []
    other_bag_list = dict()

    for data in txt_data:
        parent = data.split("contain")[0].strip()
        content = data.split("contain")[1].lstrip()
        if parent[:-5] not in other_bag_list:
            new_content = content.replace(" bag", "").replace(" bags", "").replace(".", "").replace(", ", ",").split(",")
            if len(new_content) > 1  or new_content[0] != "no others":
                for i, v in enumerate(new_content):
                    if int(v.split(" ", 1)[0]) > 1:
                        new_content[i] = v.split(" ", 1)[1][:-1]
                    else:
                        new_content[i] = v.split(" ", 1)[1]
            other_bag_list[parent[:-5]] = new_content
            bag_list.append(new_content)
    correct_bag = set()
    for i, k in enumerate(other_bag_list):
        if len(bag_list[i]) > 1 or bag_list[i][0] != "no others":
            if "shiny gold" in bag_list[i]:
                correct_bag.add(k)
                running = True
                while running:
                    for bags in other_bag_list:
                        if len(list(set(other_bag_list[bags]) & correct_bag)) > 0 and bags not in correct_bag:
                            correct_bag.add(bags)
                            break
                    else:
                        running = False
    print("Part 1 answer: {}".format(len(correct_bag)))

def part_two():
    bag_count = dict()
    other_bag_list = dict()

    for data in txt_data:
        parent = data.split("contain")[0].strip()
        content = data.split("contain")[1].lstrip()
        if parent[:-5] not in other_bag_list:
            new_content = content.replace(" bag", "").replace(" bags", "").replace(".", "").replace(", ", ",").split(",")
            new_count = content.replace(" bag", "").replace(" bags", "").replace(".", "").replace(", ", ",").split(",")
            
            if len(new_content) > 1  or new_content[0] != "no others":
                for i, v in enumerate(new_content):
                    if int(v.split(" ", 1)[0]) > 1:
                        new_content[i] = v.split(" ", 1)[1][:-1]
                    else:
                        new_content[i] = v.split(" ", 1)[1]

                for i, v in enumerate(new_count):
                    new_count[i] = int(v.split(" ", 1)[0])
            else:
                new_count[0] = 0

            other_bag_list[parent[:-5]] = new_content
            bag_count[parent[:-5]] = new_count

    map_count = dict()
    total_count = 0
    for v1, v2 in zip(other_bag_list["shiny gold"], bag_count["shiny gold"]):
        map_list = [v1]
        running = True
        curr = v1

        find_child(curr, other_bag_list, bag_count, map_list)
        ctr_final = dict()
        for data in reversed(map_list):
            if data not in ctr_final:
               
                if len(bag_count[data]) == 1:
                    
                    if other_bag_list[data][0] == "no others":
                        
                        ctr_final[data] = sum(bag_count[data])
                        # print(ctr_final)
                    else:
                        # print(ctr_final[other_bag_list[data][0]])
                        ctr_final[data] = sum(bag_count[data]) + (sum(bag_count[data]) * ctr_final[other_bag_list[data][0]] )
                else:
                    ctr_temp = 0
                    for v3, v4 in zip(other_bag_list[data], bag_count[data]):
                        ctr_temp += v4 + (v4 * ctr_final[v3])
                    ctr_final[data] = ctr_temp
        total_count += v2 + (v2 * ctr_final[v1])
    print("Part 2 answer: {}".format(total_count))

def find_child(curr, other_bag_list, bag_count, map_list):
    if bag_count[curr][0] > 0:
        if len(bag_count) > 1:
            for data in other_bag_list[curr]:
                map_list.append(data)
                find_child(data, other_bag_list, bag_count, map_list)

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()