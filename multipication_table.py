# تولید جدول ضرب اعداد 1 تا 10
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("-" * 20)  # جداکننده بین جداول