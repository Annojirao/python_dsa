class TwoSum:
    def two_sum(self, target, array):
        dict = {}
        for item in array:
            if item in dict:
                return item, target - item
            else:
                dict[target - item] = item
        return -1,-1


if __name__ == '__main__':
    target = 18
    array = [2, 7, 11,3, 15]
    print("two sum elements"+str(TwoSum().two_sum(target, array)))
