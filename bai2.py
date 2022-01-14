x = input("Nhap ten dem: ");
print(x);
def tongchuso(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;
 
n = int(input("Nhập số nguyên dương n = "));
print("Tổng các chữ số của", n , "là", tongchuso(n));
