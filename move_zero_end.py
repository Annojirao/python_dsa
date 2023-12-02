class MoveZero:
    def move_zero_end_with_place(self, num):
        if num and len(num) == 0:
            raise Exception("length of array is 0")
        else:
            src_index = 0
            dest_index = 0
            length = len(num) -1
            arr_len = len(num)
            count_of_zero = 0
            while length> -1:
                if num[src_index] != 0:
                    num[dest_index] = num[src_index]
                    src_index = src_index + 1
                    dest_index = dest_index +1
                    length = length -1
                else:
                    length = length - 1
                    src_index = src_index +1
                    count_of_zero = count_of_zero + 1
            
            while(count_of_zero > 0):
                num[arr_len-(count_of_zero)] = 0
                count_of_zero = count_of_zero -1
            return num

if __name__ == "__main__":
    num = number = [2,9,8, 0,7,1,0,3,4,0]
    print("original"+str(number))
    move_zero = MoveZero()
    print("beg_in_place"+ str(move_zero.move_zero_end_with_place(num)))