def main ():
    s = input()
    sN = convert(s)
    print (sN)

def convert(s):
    """функция заменяет символ :) на эмодзи"""
    sN = s.replace(":)", "\N{Slightly Smiling Face}")
    sN2 = sN.replace(":(", "\N{Slightly Frowning Face}")
    return sN2

main()