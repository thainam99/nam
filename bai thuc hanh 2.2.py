#viet chuong trinh nhap vao 2 diem va tinh khoang cach
import math;
x1=int(input("enter x1--->"))
y1=int(input("enter x2--->"))
x2=int(input("enter x1--->"))
y2=int(input("enter x2--->"))
d1=(x2-x1)*(x2-x1)
d2=(y2-y1)*(y2-y1)
res = math.sqrt(d1+d2)
print("distance between two points:")
