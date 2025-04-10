def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# گرفتن ورودی از کاربر
try:
    user_input = int(input("یک عدد وارد کنید: "))
    if is_prime(user_input):
        print(f"{user_input} یک عدد اول است.")
    else:
        print(f"{user_input} عدد اول نیست.")
except ValueError:
    print("لطفاً یک عدد صحیح وارد کنید.")