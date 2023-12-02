class MoveZero:
    def move_zero_beginning_with_place(self,num):
        if num and len(num) == 0:
            raise Exception("length of array is 0")
        else:
            src_index = len(num) -1
            dest_index = len(num) -1
            length = len(num) -1
            while length> -1:
                if num[length] != 0:
                    num[dest_index] = num[src_index]
                    src_index = src_index -1
                    dest_index = dest_index -1
                    length = length -1
                else:
                    length = length - 1
                    src_index = src_index -1
            if dest_index >-1:
                while(dest_index > -1):
                    num[dest_index] = 0
                    dest_index = dest_index -1
            return num

if __name__ == "__main__":
    num = number = [2,9,8, 0,7,1,0,3,4,0]
    print("original"+str(number))
    # print(move_zero_beginning(number))
    # print("beg_in_place"+ str(move_zero_beginning_with_place(number)))
    # number = [2,9,8, 0,7,1,0,3,4,0]
    # print("original"+str(number))
    # print("end_in_place"+ str(move_zero_end_with_place(number)))
    move_zero = MoveZero()
    print("beg_in_place"+ str(move_zero.move_zero_beginning_with_place(num)))
