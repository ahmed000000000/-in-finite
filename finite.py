num = 1
loop = 1

while loop < 3:
        while num < 10000:
            print(num)
            num += 1

        while num >1:
            print(num)
            num -=1
        loop += 1


        if loop == 3:
            req = int(input("Reset loop? (1/0)\n"))
            if req == 1:
                loop = 1
            else:
                loop = 3


exit = input("---")
