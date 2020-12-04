with open("./input.txt") as f:
    passport_data = []
    str_builder = [] # type: ignore
    for data in f.readlines():
        if data.strip() == '':
            passport_data.append(" ".join(str_builder))
            str_builder = []
        else:
            str_builder.append(data.strip())
    
    passport_data.append(" ".join(str_builder))

def part_one():
    code = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    total = 0
    for data in passport_data:
        ctr = 0
        cid_missing = 0
        for word in data.split(' '):
            if word[:3] in code:
                ctr += 1
                if word[:3] == 'cid':
                    cid_missing = 1
        if ctr == 8 or (ctr == 7 and cid_missing == 0):
            total += 1
    
    print("Part 1 answer: {}".format(total))

def part_two():
    code = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    ecl_code = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    total = 0
    for data in passport_data:
        ctr = 0
        cid_missing = 0
        for word in data.split(' '):
            if word[:3] in code:
                if word[:3] == 'byr' and len(word[4:]) == 4 and (1920 <= int(word[4:]) <= 2002):
                    ctr += 1
                elif word[:3] == 'iyr' and len(word[4:]) == 4 and (2010 <= int(word[4:]) <= 2020):
                    ctr += 1
                elif word[:3] == 'eyr' and len(word[4:]) == 4 and (2020 <= int(word[4:]) <= 2030):
                    ctr += 1
                elif word[:3] == 'hcl' and word[4:][0] == '#' and len(word[4:][1:]) == 6:
                    for temp_word in word[4:][1:]:
                        if not (ord(temp_word) in range(ord('0'), ord('9') + 1) or ord(temp_word) in range(ord('a'), ord('f') + 1)):
                            break
                    ctr += 1
                elif word[:3] == 'ecl' and word[4:] in ecl_code:
                    ctr += 1
                elif word[:3] == 'pid' and len(word[4:]) == 9:
                    for temp_word in word[4:][1:]:
                        if not (ord(temp_word) in range(ord('0'), ord('9') + 1)):
                            break
                    ctr += 1
                elif word[:3] == 'hgt' and word[4:][-2:] in ['cm', 'in']:
                    if word[4:][-2:] == 'cm':
                        if 150 <= int(word[4:][:-2]) <= 193:
                            ctr += 1
                    else:
                        if 59 <= int(word[4:][:-2]) <= 76:
                            ctr += 1
                elif word[:3] == 'cid':
                    ctr += 1
                    cid_missing = 1

        if ctr == 8 or (ctr == 7 and cid_missing == 0):
            total += 1
    print("Part 2 answer: {}".format(total))

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()