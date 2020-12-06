import re
from utilities import get_data_as_csv
raw = get_data_as_csv('day4')

data = [str(row[0]) if len(row) > 0 else "" for row in raw]

sample = [
    "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
    "byr:1937 iyr:2017 cid:147 hgt:183cm",
    "",
    "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
    "hcl:#cfa07d byr:1929",
    "",
    "hcl:#ae17e1 iyr:2013",
    "eyr:2024",
    "ecl:brn pid:760753108 byr:1931",
    "hgt:179cm",
    "",
    "hcl:#cfa07d eyr:2025 pid:166559648",
    "iyr:2011 ecl:brn hgt:59in"
]

sample_invalid_2 = [
"eyr:1972 cid:100",
"hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
"",
"iyr:2019",
"hcl:#602927 eyr:1967 hgt:170cm",
"ecl:grn pid:012533040 byr:1946",
"",
"hcl:dab227 iyr:2012",
"ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
"",
"hgt:59cm ecl:zzz",
"eyr:2038 hcl:74454a iyr:2023",
"pid:3556412378 byr:2007"
]

sample_valid_2 = [
"pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
"hcl:#623a2f",
"",
"eyr:2029 ecl:blu cid:129 byr:1989",
"iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
"",
"hcl:#888785",
"hgt:164cm byr:2001 iyr:2015 cid:88",
"pid:545766238 ecl:hzl",
"eyr:2022",
"",
"iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"
]

def part1(data):
    # find the number of valid passports (\n separated) 
    # entry is valid if it has all 8 fields "byr, iyr, eyr, hgt, hcl, ecl, pid, cid"
    # cid is optional
    total_valid = 0

    data_to_string = ','.join(data).replace(' ', ',').replace(',,', "|") #now the only separater is |
    data_to_list = data_to_string.split('|')
    all_keys = []
    for passport in data_to_list:
        fields = passport.split(',')
        all_keys.append([key.split(':')[0] for key in fields])

    for keys in all_keys:
        if len(keys) < 7:
            continue
        if \
            "byr" in keys\
            and "iyr" in keys\
            and "eyr" in keys\
            and "hgt" in keys\
            and "hcl" in keys\
            and "ecl" in keys\
            and "pid" in keys:
            total_valid += 1
            # print(keys)
    print(total_valid) 

def part2(data, debug=False):
    # find the number of valid passports (\n separated) 
    # entry is valid if it has all 8 fields "byr, iyr, eyr, hgt, hcl, ecl, pid, cid"
    # cid is optional
    total_valid = 0

    data_to_string = ','.join(data).replace(' ', ',').replace(',,', "|") #now the only separater is |
    data_to_list = data_to_string.split('|')
    all_passports = []
    for passport in data_to_list:
        fields = passport.split(',')
        all_passports.append({key.split(':')[0]: key.split(':')[1] for key in fields})

    for passport in all_passports:
        if len(passport) < 7:
            if debug: print(f'failure on num_fields: {len(passport)}')
        byr = passport.get('byr', False)
        iyr = passport.get('iyr', False)
        eyr = passport.get('eyr', False)
        hgt = passport.get('hgt', False)
        hcl = passport.get('hcl', False)
        ecl = passport.get('ecl', False)
        pid = passport.get('pid', False)
        if not(byr and iyr and eyr and hgt and hcl and ecl and pid):
            if debug: print(f'failure on field availibility')
            continue
        if not (len(byr) == 4 and int(byr) >= 1920 and int(byr) <= 2002):
            if debug: print(f'failure on field "byr": {byr}')
            continue
        if not (len(iyr) == 4 and int(iyr) >= 2010 and int(iyr) <= 2020):
            if debug: print(f'failure on field "iyr": {iyr}')
            continue
        if not (len(eyr) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030):
            if debug: print(f'failure on field "eyr": {eyr}')
            continue
        if not(re.match("^(\d\d\dcm|\d\din)$", hgt)):
            if debug: print(f'failure on field "hgt": {hgt}')
            continue
        if not (('cm' in hgt and int(hgt[:-2]) >= 150 and int(hgt[:-2]) <=193) or ('in' in hgt and int(hgt[:-2]) >= 59 and int(hgt[:-2]) <= 76)):
            if debug: print(f'failure on field "hgt": {hgt}')
            if debug: print(int(hgt[:-2]))
            continue
        if not (re.match("^#[0-9a-f]{6}$", hcl)):
            if debug: print(f'failure on field "hcl": {hcl}')
            continue
        if not (re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", ecl)):
            if debug: print(f'failure on field "ecl": {ecl}')
            continue
        if not (re.match('^\d{9}$', pid)):
            if debug: print(f'failure on field "pid": {pid}')
            continue

        total_valid += 1
        for k,v in passport.items():
            if k == "pid":
                print(f'{k}: {v}')
    print(f'total valid: {total_valid}') 

# part1(data)
part2(data, False)
