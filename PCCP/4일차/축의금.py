import re
text = "배근표10 권이혁5 강산30 승희엄마100"

answer = {}
for string in text.split():
    person = re.findall(r'\D+', string)[0]
    num = re.findall(r'\d+', string)[0]
    answer[person] = num

print(answer)


import re
text = "배근표10 권이혁5 강산30 승희엄마100"

answer = {}
for string in text.split():
    person, num = re.split(r'(\d+)', string)[:-1]
    answer[person] = num

print(answer)
