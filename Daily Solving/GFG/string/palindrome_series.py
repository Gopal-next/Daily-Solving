def pallan (n) : 
    #Complete the function
    dic = {
        '0':'a',
        '1':'b',
        '2':'c',
        '3':'d',
        '4':'e',
        '5':'f',
        '6':'g',
        '7':'h',
        '8':'i',
        '9':'j'
    }
    a = ''
    b = 0
    strr = str(n)
    for i in range(len(strr)):
        a += dic[strr[i]]
        b += int(strr[i])
    first = a * (b//len(strr))
    second = (b%len(strr))
    
    c =  first + a[:second]
    if c == c[::-1]:
        return True
    else:
        return False