from typing import List
class Solution:
    def sort_by_frequency_int(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: (nums.count(x), -x), reverse=True)


    def sort_by_frequency_str(self, str) -> str:
        map = {}
        for element in str:
            map[element] = map.get(element,0) +1
        map = dict(sorted(map.items(), key=lambda item: item[1],reverse=True))
        result = ''
        for key, value in map.items():
            result += key*value
        return result

if __name__ == '__main__':
    str = 'tree'
    print(Solution().sort_by_frequency_str(str))
    array = [2, 7,2, 11,3,3 ,15,3]
    print(Solution().sort_by_frequency_int(array))