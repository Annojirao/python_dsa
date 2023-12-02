class ReverseString:
    def reverse(self,str):
        return str[::-1]

    def reverse_string(self,str):
        data = [ x.strip() for x in str.split(' ')]
        data.reverse()
        return " ".join(data)


if __name__ == '__main__':
    print(ReverseString().reverse('annoji rao'))
    print(ReverseString().reverse_string('main hoo na'))