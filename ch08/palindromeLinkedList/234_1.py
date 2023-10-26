# 연결 리스트가 팰린드롬 구조인지 판별하라

# 입력 : 1 -> 2 
# 출력 : false

# 입력 : 1->2->2->1
# 출력 : true
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        half = len(stack) // 2
        left = stack[:half]
        right = stack[len(stack)-1 : half - 1: -1]
        if len(left) < len(right) :
            right.pop()
        print(left , right)
        return left == right