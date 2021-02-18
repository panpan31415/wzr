def nine_nine_table():
    a = 1
    b = 1
    while a <= 9:
        b = 1
        while b <= a:
            result = "{}*{}={} "
            print(result.format(a, b, a*b), end="")
            b += 1
        a += 1
        print("", end="\n")


nine_nine_table()
