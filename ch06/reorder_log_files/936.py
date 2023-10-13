# 1. 로그의 가장 앞 부분은 식별자다
# 2. 문자열로 구성된 로그가 숫자 로그보다 앞에 온다.
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 한다.
# 4. 숫자 로그는 입력 순서대로 한다. 


log = ["t kvr", "r 3 1", "i 403", "7 so", "t 54"]

#     ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]


# 그럼 우선 문자열 로그와 숫자 로그 나누기

str_log = []
dig_log =[]

for str in log:
    temp = list(str.split(' '))
    if temp[1].isdecimal():
        dig_log.append(str)
    else:
        str_log.append(str)



def len_alpha_str(s : str) -> int :
    s = list(s)
    count = 0
    for x in s:
        if x.isdecimal():
           pass
        else:
            count += 1
    return count
        
def compare_alpha(s: str) -> int:
    s = list(s)
    value = 0
    for x in s:
        if x.isdecimal():
           pass
        else:
            value += ord

str_log.sort(key=lambda x : (x.split()[1:], x.split()[0] ))

str_log.extend(dig_log)

print(str_log)