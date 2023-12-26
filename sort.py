def selection_sort():
    a = [13, 46,24, 52, 20,9]
    length = len(a)
    for i in range(length):
        cur_low = a[i]
        low_ind = i
        for j in range(i+1, length):
            if a[j] < cur_low:
                cur_low = a[j]
                swap_index = j
        a[swap_index] =a[i]
        a[i] = cur_low
        a[low_ind] = a[i]
        
    print(a)
    
def bubble_sort():
    a = [13, 46,24, 52, 20,9]
    print(a)
    length = len(a)
    for i in range(length):
        for j in range(i+1, length):
            if a[i] > a[j]:
                temp =a[i]
                a[i] = a[j]
                a[j] = temp
        
    print(a)

def insertion_sort():
    a = [13, 46,24, 52, 20,9]
    print(a)
    length = len(a)
    for i in range(length):
        j = i
        while (j > 0 and a[j-1] > a[j] ):
            temp =a[j-1]
            a[j-1] = a[j]
            a[j] = temp
            j = j-1
        
    print(a)

if __name__ == '__main__':
    insertion_sort()
