#addition function
def addition():
    addend1=float(input("Please enter the first addend:"))
    addend2=float(input("Please enter the second addend:"))
    print(f"The answer is {addend1+addend2}")


#subtraction function
def subtraction():
    minuend=float(input("Please enter the minuend:"))
    subtrahend=float(input("Please enter the subtrahend:"))
    print(f"The answer is {minuend-subtrahend}")


#multiplication function
def multiplication():
    multiply1=float(input("Please enter the first multiplication:"))
    multiply2=float(input("Please enter the second multiplication:"))
    print(f"The answer is {multiply1*multiply2}")


#division function
def division():
    dividend=float(input("Please enter the dividend:"))
    divisor=float(input("Please enter the divisor:"))
    print(f"The answer is {dividend/divisor}")


#exponentiation function
def exponentiation_function():
    base_number=float(input("Please enter the base number:"))
    exponent=float(input("Please enter the exponent:"))
    print(f"The answer is {base_number**exponent}")


#square root
def square_root():
    root=float(input("Please enter the root of the number:"))
    if root < 0:
        print("Negative numbers cannot be squared")
    else:
        print(f"The answer is {root**0.5}")


#administration list
def management_list():
    numbers = []  # 创建一个空列表

    print("Please enter the number(Click enter to end):")

    while True:
        user_input = input(">>> ")

        # 退出条件：用户输入为空字符串
        if user_input == "":
            print("input ends")
            break

        try:
            # 尝试将输入转换为数字（支持整数和小数）
            num = float(user_input)
            numbers.append(num)  # 将数字存入列表
            print(f"Added {num},The current list is:{numbers}")
        except ValueError:
            print("Please enter a number")

    print(f"\n最终列表为：{numbers}")
    while True:
        user_require=input("Please chose the service(summation,average,maximum,minimum,median,variance)(Click enter to end):")
        if user_require == "":
            print("input ends")
            break
        elif user_require == "summation":
            print(sum(numbers))
        elif user_require == "average":
            print(sum(numbers)/len(numbers))
        elif user_require == "maximum":
            print(max(numbers))
        elif user_require == "minimum":
            print(min(numbers))
        elif user_require == "median":
            if len(numbers) > 0:
                sorted_numbers = sorted(numbers)  #For sort
                n = len(sorted_numbers)
                if n % 2 == 1:  # The number of elements is odd
                    median = sorted_numbers[n // 2]
                else:  # The number of elements is even
                    median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
                print(f"The median of the list is:{median}")
            else:
                print("There is no numbers to manage")
        elif user_require == "variance":
            n = len(numbers)

            if n == 0:
                print("There is no numbers to manage")
            else:
                # For average
                mean = sum(numbers) / n

                # 计算离差平方和
                squared_diff_sum = sum((x - mean) ** 2 for x in numbers)

                # 总体方差（除以 n）
                population_var = squared_diff_sum / n

                # 样本方差（除以 n-1），需要 n >= 2
                if n >= 2:
                    sample_var = squared_diff_sum / (n - 1)
                    print(f"Total variance:{population_var}")
                    print(f"Sample variance:{sample_var}")
                else:
                    print(f"Total variance：{population_var}(Only one number,unable to calculate variance)")


#factorial function
def factorial(n):

    if not isinstance(n, int):
        raise TypeError("Must be int")
    if n < 0:
        raise ValueError("Must be positive")

    if n == 0:
        return 1

    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result


def get_valid_input():

    while True:
        user_input = input("Please enter the number ").strip()

        # For quit
        if user_input.lower() == 'q':
            print("Thanks for using")
            return None

        # For shift
        try:
            num = int(user_input)
            # For check
            if num < 0:
                print("The number have to be larger then 0(>=0)")
                continue

            return num
        except ValueError:
            #Invalid input,warning
            print("Error")


def factorial_first():

    while True:
        num = get_valid_input()
        if num is None:  # For break
            break

        try:
            result = factorial(num)
            print(f"{num}! = {result}\n")
        except (TypeError, ValueError) as e:
            print(f"error: {e}\n")


if __name__ == "__factorial_print__":
    factorial_first()


def factorial_second():

    while True:
        user_input = input("Please enter a number: ").strip()

        # For quit
        if user_input.lower() == 'q':
            print("Goodbye!")
            break

        # For shift
        try:
            num = int(user_input)
        except ValueError:
            print("Must be a positive integer")
            continue

        if num < 0:
            print("Must be >= 0")
            continue


        if num == 0:
            result = 1
        else:
            result = 1
            n = num
            while n > 0:
                result *= n
                n -= 1

        # For print result
        print(f" {num}! = {result}\n")


#截至目前加减乘除，数据初步管理以及阶乘的函数已经完备

#未完待续，敬请期待