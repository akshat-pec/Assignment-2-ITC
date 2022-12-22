a = float(input("Enter length of side A: "))
b = float(input("Enter length of side B: "))
c = float(input("Enter length of side C: "))
if a + b > c and b + c > a and a + c > b:
    print("Yes")
else:
    print("No")