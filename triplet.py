class Triplet:
    def find_pair(self, target, array):
        dict = {}
        for item in array:
            if item in dict:
                return [item, target - item]
            else:
                dict[target - item] = item
        return [-1,-1]

    def triplet(self, target, array):
        for ind, item in enumerate(array):
            new_list = array[:ind-1] + array[ind+1:]
            result = self.find_pair(target - array[ind], new_list)
            if result and result[0] != -1:
                return [item, result[0], result[1]] 
        return [-1,-1,-1]

if __name__ == '__main__':
    array = [0, 2, 3, 15 , 7, 11 ]
    target = 18
    print("triplet"+str(Triplet().triplet(target, array)))