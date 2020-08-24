print("ввод End завершит работку программы")
while True:
    s = ("end")
    if s == 'end':
        break
while True:
    try:         
            a1 = int(input("введите 1й операнд "))
            a2 = int(input("введите 2й операнд "))
            a3 = int(input("введите 3й операнд "))
            a4 = int(input("введите 4й операнд "))
            a5 = int(input("введите 5й операнд "))
            a6 = int(input("введите 6й операнд "))
            a7 = int(input("введите 7й операнд "))
            a8 = int(input("введите 8й операнд "))
            a9 = int(input("введите 9й операнд "))
            a10 = int(input("введите 10й операнд "))
            a11 = int(input("введите 11й операнд "))
            a12 = int(input("введите 12й операнд "))
            b1 = a1
            b2 = a2
            b3 = a3
            b4 = a4^b1
            b5 = a5^b2
            b6 = a6^b3^b1
            b7 = a7^b4^b2
            b8 = a8^b5^b3
            b9 = a9^b6^b4
            b10 = a10^b7^b5
            b11 = a11^b8^b6
            b12 = a12^b9^b7
            c1 = b1
            c2 = b2
            c3 = b3
            c4 = b4^b1
            c5 = b5^b2
            c6 = b6^b3^b1
            c7 = b7^b4^b2
            c8 = b8^b5^b3
            c9 = b9^b6^b4
            c10 = b10^b7^b5
            c11 = b11^b8^b6
            c12 = b12^b9^b7
            print("Скремблирование")
            print(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12)
            print("дескремблирование")
            print(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12)      
    except ValueError:
       pass











