class Solution(object):
    def findDuplicate(self, nums):
        length = len(nums)
        length = length -1
        difference = sum(nums) - (length * (length +1))/2
        return difference

    def findDuplicate2(self, nums):
        # when iterrating slow pointer and fast pointer will collide, once collides, breadk it 
        # start from 0 for slow and while slow != fast pick and store element return slow
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

if __name__ == "__main__":
    print(Solution().findDuplicate([1,3,4,2,2]))
    print(Solution().findDuplicate2([3,1,3,4,2,2]))