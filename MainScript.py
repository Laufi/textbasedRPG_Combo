import json
level = 0
exp = 0
MaxHP = 0
MaxMP = 0
Def = 0
MaxAttack = 0
MinAttack = 0


with open("savefile.json", "r+") as json_file:
    savefiledata = json.load(json_file)
    level = savefiledata["level"]


print(level)