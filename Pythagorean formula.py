#A = Ghaede B = Ertefa C = Vatar
print("فرمول فیثاقورس")
print("ضلع مجهول شما کدام است؟")
print("1. ضلع وتر")
print("2. ضلع ارتفاع")
print("3. ضلع قاعده")

while True:
    choice = input("انتخاب شما (1/2/3): ")

    if choice in ['1', '2', '3']:

        if choice == '1':
          A = float(input("ضلع قاعده را وارد کنید: "))
          B =  float(input("ضلع ارتفاع را وارد کنید"))
          C = (A**2 + B**2)**0.5
          print(f"ضلع وتر شما: {C}")

        elif choice == '2':
          C = float(input("ضلع وتر را وارد کنید: "))
          A =  float(input("ضلع قاعده را وارد کنید"))
          B = (C**2 - A**2)**0.5
          print(f"ضلع ارتفاع شما: {B}")
        
        elif choice == '3':
          C = float(input("ضلع وتر را وارد کنید: "))
          B =  float(input("ضلع ارتقاع را وارد کنید"))
          A = (C**2 - B**2)**0.5
          print(f"ضلع قاعده شما: {A}")
        
        
        next_calculation = input("آیا می‌خواهید محاسبه دیگری انجام دهید؟ (بله/خیر): ")
        if next_calculation.lower() != 'بله':
          break