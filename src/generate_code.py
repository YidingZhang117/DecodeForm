import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

f = open("provide_text.txt", "r", encoding="utf-8")
lines = f.read().split("\n")
f.close()

temp_result = []
for l in lines:
    con = l.split(";")
    temp = "{\n"
    temp += "    \"key\": \"" + con[0] + "\",\n"    

    if con[1] == "1":
        temp += "    \"type\": \"choice\",\n"
        temp += "    \"value\": ["
        choice_result = []
        for s in con[2].split(" "):
            choice_result.append("\"" + s + "\"")
        temp += ",".join(choice_result)
        temp += "]\n"
    elif con[1] == "2":
        temp += "    \"type\": \"input\"\n"
    
    temp += "}"
    temp_result.append(temp)
print(",\n".join(temp_result))