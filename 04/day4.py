import re
valid = 0
needed = set(["byr","iyr","eyr","hgt","hcl","ecl","pid"])
validFields = needed.copy()
validFields.add("cid")


def isValid_part1(fieldsNames):
    global valid
    if (fieldsNames==needed or fieldsNames==validFields):
        valid += 1

def isValid(fieldsNames, fields):
    global valid
    if (fieldsNames==needed or fieldsNames==validFields):
        byr=int(fields["byr"])
        iyr=int(fields["iyr"])
        eyr=int(fields["eyr"])

        cmCheck = re.compile("[0-9]{3}cm$")
        inCheck = re.compile("[0-9]{2}in$")
        if (cmCheck.match(fields["hgt"])):
            if (fields["hgt"]=="173in"):print("cm")
            hgt = int(fields["hgt"][:-2])
            if (hgt>193 or hgt<150):
                return
        elif (inCheck.match(fields["hgt"])):
            if (fields["hgt"]=="173in"):print("in")
            hgt = int(fields["hgt"][:-2])
            if (hgt>76 or hgt<59):
                return
        else:return
        
        hclCheck = re.compile("#[0-9a-f]{6}$")
        pidCheck = re.compile("[0-9]{9}$")  

        if ((len(str(byr))==4 and byr>=1920 and byr<=2002) and
        (len(str(iyr))==4 and iyr>=2010 and iyr<=2020) and
        (len(str(eyr))==4 and eyr>=2020 and eyr<=2030) and
        (hclCheck.match(fields["hcl"])) and
        (fields["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]) and
        (pidCheck.match(fields["pid"]))):
            valid += 1
            #print(fields)

with open("input") as file: 
    inp = file.readline()
    currentFieldNames=set()
    fields ={}
    while (inp!=""):
        info = inp.split()
        for f in info:
            field, value = f.split(":")
            currentFieldNames.add(field)
            fields[field]=value
        if (inp=="\n"):
            isValid(currentFieldNames, fields)
            currentFieldNames=set()
            fields ={}
            
        inp = file.readline()
    isValid(currentFieldNames, fields)
print(valid)