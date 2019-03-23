
def giaithua(n):
    if n==0:
        print("giai thua cua 0= 1")
    else:
        i=1;
        gt=1;
        while i<= n:
            gt=gt*i
            i=i+1
        print("giai thua cua "+str(n)+"=",gt)