num = int(input("Enter five digit number:\n"))

num1 = num // 10000;
num2 = (num % 10000) // 1000;
num3 = (num % 1000) // 100;
num4 = (num % 100) // 10;
num5 = num % 10;

print(num1,   num2,   num3,   num4,   num5)
