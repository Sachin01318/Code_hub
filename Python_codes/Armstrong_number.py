
if __name__ == '__main__':
    num = int(input("Enter number : "))
    armstrong_num(num)


def armstrong_num(num):
    try:

        count = 0
        mod = 0

        temp = num
        while temp > 0:
            count += 1
            temp = temp // 10

        sum_v = 0
        temp = num
        while num > 0:
            mod = num % 10
            sum_v = mod ** count + sum_v
            num = num // 10

        if sum_v == temp:
            print(f"{temp} is armstrong number")
        else:
            print(f"{temp} is not armstrong number")

    except ValueError:
        print("You have Entered invalid number , Please Enter Integer number")








