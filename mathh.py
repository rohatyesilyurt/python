while True:
    a = int(input("Number: "))

    step = 0
    while True:
        if a % 2 == 0:
            b = a
            a /= 2
            print(f"{step+1}. step:  divide {int(b)} by 2 --> {int(a)}")
        elif a == 1:
            print(f"It took {step} steps to get 1.")
            break
        else:
            b = a
            a =+ 1
            print(f"{step+1}. step:  multiply {int(b)} by 3 and add 1 --> {int(a)}")
        step += 1


