class Solution:
    def isHappy(self, n: int) -> bool:
        
        n_list = set()
        n_list.add(n)
        
        while 1:
            sum = 0
            for s in str(n):
                sum += int(s) * int(s)
            
            if sum == 1:
                return True

            if sum in n_list:
                return False

            n = sum
            n_list.add(n)
            
    def get_sum(self,n: int) -> int: 
        new_num = 0
        while n:
            n, r = divmod(n, 10)
            new_num += r ** 2
        return new_num