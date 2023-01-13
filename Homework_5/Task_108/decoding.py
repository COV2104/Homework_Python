# метод который будет декодировать наш текст

def decod(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

if __name__=='__main__':
    s = '10x'
    print(decod(s))