# 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라

arr = [1,2,3,4]
output = [24,12,8,6]

# 나눗셈을 하지 않고 O(n)에 풀이하라

# 나눗셈을 하지 않고 O(n)에 풀이라...잘 모르겠는뎅
# 모든 수를 곱하고 해당 값 만 나눠주면 되긴하는데
# 이건 나눗셈이 들어감
# 인폿이 길이가 4니까 ...
# 나눗셈 안하려면 그냥 for문 돌리면 되는거 아님?

# 몰라서 책 봄 ㅎㅎ
# 이 문제에는 중요한 제약사항이 있다. 
# 당장 머릿속에 떠오르는 풀이법은 미리 전체 곱셈값을 구해놓고 각 항목별로 자기 자신을 나눠서 풀이하는 방법은 안된다는 것이다.
# 그렇다면 풀이 방법은 한 가지 뿐이다. 자기 자신을 제외하고 왼쪽의 곱셈 결과와 오른쪽의 곱셈 결과를 곱해야한다.

in_order_mul_arr = []
reversed_mul_arr = []
temp = 1
for i in range(len(arr)):
    in_order_mul_arr.append(temp)
    temp *= arr[i]

temp = 1
for i in range(len(arr)-1 , 0-1, -1):
    temp = in_order_mul_arr[i] * arr[i]
    reversed_mul_arr.append(temp)
    print(in_order_mul_arr[i])
    
answer = []
for i in range(len(arr)):
    temp = in_order_mul_arr[i] * reversed_mul_arr[i]
    answer.append(temp)
    
print(answer)