import re

paragraph = "Bob hit a ball, the hit BALL flew far after"
banned = ["hit"]
result = re.sub(r"[^a-zA-Z]", " ", paragraph)

result_dict = dict()

for x in list(result.split(' ')):
    if x in banned:
            continue
    if len(x) > 0:
        if x.lower() not in result_dict:
            result_dict[x.lower()] = 0
        result_dict[x.lower()] += 1

print(result_dict)
max_value = 0
max_key = ''

for key, value in result_dict.items():
    print(key , value)
    if max_value <= value:
        max_value = value
        max_key = key

print(max_key)