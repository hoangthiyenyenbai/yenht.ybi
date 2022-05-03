print("Bài 1: Kiểm tra số âm dương")
n = int(input("Nhap vao mot so: "))
if n > 0 :
	print(n," la so nguyen duong")
elif n < 0 :
	print(n," la so nguyen am")
else :
	print(n," la so 0")
print("*******************************************************")
print("Bai 2: Kiem tra tinh chan le")
n = int(input("Nhap so nguyen can kiem tra: "))
if n%2 == 0 :
	print(f"{n} la so chan")
else :
	print(f"{n} la so le")
print("*******************************************************")
print("Bai 3: Kiem tra so")
n = int(input("Nhap vao mot so nguyen: "))
if n >= 0 :
	if n%2 == 0 :
		print(f"{n} la so chan, nguyen duong")
	else :
		print(f"{n} la so le, nguyen duong")
else :
	if n%2 == 0 :
		print(f"{n} la so chan, nguyen am")
	else :
		print(f"{n} la so le, nguyen am")	
if 22 <= n <= 44 :
	print(f"{n} nam trong khoang tu 22 den 44")
else :
	print(f"{n} khong nam trong khoang tu 22 den 44")

print("*******************************************************")
print("Bai 4: Kiem tra ky tu")
c = input("Nhap vao mot ky tu: ")
if ord(c)==13 :
	print(f"{c} la dau enter")
	print(f"{c} khong phai la chu so")
	print(f"{c} khong phai la chu in hoa")
	print(f"{c} khong phai la chu in thuong")
	print(f"{c} khong phai la ky tu dac biet")
elif 48 <= ord(c) <= 57 :
	print(f"{c} la chu so")
	print(f"{c} khong phai la dau enter")
	print(f"{c} khong phai la chu in hoa")
	print(f"{c} khong phai la chu in thuong")
	print(f"{c} khong phai la ky tu dac biet")
elif 65 <= ord(c) <= 90 :
	print(f"{c} la chu in hoa")
	print(f"{c} khong phaila dau enter")
	print(f"{c} khong phai la chu so")
	print(f"{c} khong phai la chu in thuong")
	print(f"{c} khong phai la ky tu dac biet")
elif 97 <= ord(c) <= 122 :
	print(f"{c} la chu in thuong")
	print(f"{c} khong phai la dau enter")
	print(f"{c} khong phai la chu in hoa")
	print(f"{c} khong phai la chu so")
	print(f"{c} khong phai la ky tu dac biet")
	
elif (33 <= ord(c) <= 46) or (58 <= ord(c) <= 64):
	print(f"{c} la ky tu dac biet")
	print(f"{c} khong phai la chu so")
	print(f"{c} khong phai la dau enter")
	print(f"{c} khong phai la chu in hoa")
	print(f"{c} khong phai la chu in thuong")

print("*******************************************************")
print("Bai 5: Kiem tra nam nhuan")
nam = int(input("Nhap vao nam can kiem tra: "))
if nam%400 == 0 :
	print(f"Nam {nam} la nam nhuan")
else :
	if nam%4 ==0 :
		print(f"Nam {nam} la nam nhuan")
	else :
		print(f"Nam {nam} khong phai la nam nhuan")
print("*******************************************************")
print("Bai 6: Giai phuong trinh bac hai")
import math
print("Nhap phuong trinh bac 2: ")
a = float(input("Nhap tham so a (a khac 0): "))
b = float(input("Nhap tham so b: "))
c = float(input("Nhap tham so c: "))
if a==0: 
	print("Khong dung dieu kien yeu cau.")
else :
	delta = b*b - 4*a*c
	x = math.sqrt(delta)
	if delta < 0 :
		print("Phuong trinh vo nghiem.")
	elif delta == 0 :
		print("Phuong trinh co nghiem: x = ", -b/(2*a))
	elif delta > 0:
		print("Phuong trinh co 2 nghiem là: x1 = ", float((-b+x)/(2*a))," va x2 = ",(-b-x)/(2*a))	
		

print("*******************************************************")
print("Bai 7: Tinh cuoc taxi")
km = float(input("Nhap so km da di taxi: "))
if km <= 1 :
	print("Số tien can tra la: 15.000 (Muoi lam nghin dong")
elif km <= 20 :
	print("So tien can tra la: ", 15.000 + (km - 1)*12.000)
else :
	print("So tien can tra la : ", 15.000 + 19*12.000 + (km - 20)*10.000)

input()