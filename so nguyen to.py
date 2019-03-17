n = int(input('nhap n='))
if n == 1:
    print("không là số nguyên tố")
else:
        i = 2
        while n % i != 0:
            i = i + 1
        if n == i:
            print("là số nguyên tố")
        else:
            print("không là số ngyên tố")
