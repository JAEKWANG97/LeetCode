# 가장긴 팰린드롬 부분 문자열을 출력하라
s = "aa"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# 윈도우 스케일링


# 모든 경우의 수를 확인하는 방법 밖에 없을까
# 이걸 거꾸로 해도 되잖아
def isPalindreom(s : str):
    if len(s) == 1: return s
    length = [i+1 for i in range(len(s)-1 ,-1 , -1)]
    for size in length:
        for i in range(len(s) - size + 1):
            j = i + size
            word = s[i:j]
            if word == word[::-1]:
                return word
