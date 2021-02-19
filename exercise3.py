def nine_nine_table():
    a = 9
    while a > 0:
        b = 1
        while b <= a:
            result = "{1}*{0}={2} "
            print(result.format(a, b, a*b), end="")
            b += 1
        a -= 1
        print("", end="\n")

nine_nine_table()
