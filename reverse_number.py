def reverse_number(number):
    reverse = 0
    while number:
        digit = number %10;
        number  = number //10
        reverse = reverse*10+digit
    return reverse

if __name__ == '__main__':
    number = 123442656
    print('original_nubmer '+str(number))
    print('reversed_number '+str(reverse_number(number)))
