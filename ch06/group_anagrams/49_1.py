strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# 각 문자열을 알파벳 빈도 수로 변환
def encode(s):
    alpha = [0] * 26
    for char in s:
        alpha[ord(char) - 97] += 1
    return tuple(alpha)

# 문자열을 빈도 수로 변환하고 동일한 빈도를 가진 문자열끼리 그룹화
encoded_strs = {}
for s in strs:
    encoded = encode(s)
    print(encoded)
    if encoded not in encoded_strs:
        encoded_strs[encoded] = [s]
    else:
        encoded_strs[encoded].append(s)

# 결과 출력
result = list(encoded_strs.values())
print(result)
