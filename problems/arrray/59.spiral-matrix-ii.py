from typing import List

# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result_arr = [ [0] * n for _ in range(n)]
        
        startx, starty = 0, 0
        loop = n // 2
        mid = n // 2
        offset = 1
        
        count = 1
        
        while loop >= 1:
            # (0, 0) (0, 1)
            for i in range(starty, n - offset):
                result_arr[startx][i] = count
                count += 1
            
            # (0, 2) (1, 2)
            for i in range(startx, n - offset):
                result_arr[i][n - offset] = count
                count += 1
            
            # (2, 2) (2, 1)
            for i in range(n - offset, starty, -1):
                result_arr[n - offset][i] = count
                count += 1
            
            # (2, 0) (1, 0)   
            for i in range(n - offset, startx, -1):
                result_arr[i][starty] = count
                count += 1
                
            loop -= 1
            startx += 1
            starty += 1
            offset += 1
        
        if n % 2 != 0:
            result_arr[mid][mid] = count 
        
        return result_arr

if __name__ == '__main__':
    print(Solution().generateMatrix(4))