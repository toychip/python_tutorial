# print("helloworld")

def isPalindrome(self, head: ListNode ) -> bool:
    rev = None
    
    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
        if fast :
            slow = slow.next
        
        #랠린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev

