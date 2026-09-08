class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = r = total = elevated = 0
        maxSeen = (None, float('-inf'), None)

        while l < len(height):
            while l < len(height) and height[l] == 0:
                l += 1
            
            if l >= len(height) -1: 
                break

            r = l + 1
            maxSeen = (None, float('-inf'), None)
            elevated = 0

            while r < len(height) and height[r] < height[l]:
                if maxSeen[0] is None or height[r] > maxSeen[1]:
                    maxSeen = (r, height[r], elevated)
                elevated += height[r]
                r += 1


            if r < len(height):
                total += ((height[l] * (r-l-1)) - elevated)
                l = r
            else:
                total += ((maxSeen[1] * (maxSeen[0]-l-1)) - maxSeen[2])
                l = maxSeen[0]        

        return total
