#addition function
def addition():

    while True:
        try:
            addend1 = input("Please enter the first addend:")
            addend2 = input("Please enter the second addend:")
            addend_01=float(addend1)
            addend_02=float(addend2)
            break
        except ValueError:
            print("Please enter a number")

    print(f"The answer is {addend_01+addend_02}")


#subtraction function
def subtraction():
    while True:
        try:
            minuend = input("Please enter the minuend:")
            subtrahend = input("Please enter the subtrahend:")
            minuend_01=float(minuend)
            subtrahend_01 = float(subtrahend)
            break
        except ValueError:
            print("Please enter a number")

    print(f"The answer is {minuend_01-subtrahend_01}")


#multiplication function
def multiplication():
    while True:
        try:
            multiply1 = float(input("Please enter the first multiplication:"))
            multiply2 = float(input("Please enter the second multiplication:"))
            multiply_01=float(multiply1)
            multiply_02=float(multiply2)
            break
        except ValueError:
            print("Please enter a number")

    print(f"The answer is {multiply_01*multiply_02}")


#division function
def division():
    while True:
        try:
            dividend = input("Please enter the dividend:")
            divisor = input("Please enter the divisor:")
            division_01=float(dividend)
            division_02=float(divisor)
            break
        except ValueError:
            print("Please enter a number")

    print(f"The answer is {division_01/division_02}")


#exponentiation function
def exponentiation_function():
    while True:
        try:
            base_number = input("Please enter the base number:")
            exponent = input("Please enter the exponent:")
            base_number_01=float(base_number)
            exponent_01=float(exponent)
            break
        except ValueError:
            print("Please enter a number")

    print(f"The answer is {base_number_01**exponent_01}")


#square root
def square_root():
    while True:
        try:
            root=input("Please enter the root of the number:")
            root_01=float(root)
            break
        except ValueError:
            print("Please enter a number")

    print(f"The answer is {root_01**0,5}")


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
        user_require=input("Please chose the service(summation,average,maximum,minimum,median,variance)\n(Click enter to end)\n:")
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
        elif user_require == "quit":
            break


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




def selection():
    print("Please enter your choice:"
          "(addition,subtraction,multiplication,division,exponentiation,square root,factorial,list management)"
          "(Enter 'quit' to quit): ")

    while True:
        choice = input("Please enter your choice:")
        if choice == 'addition':
            addition()
        elif choice == 'subtraction':
            subtraction()
        elif choice == 'multiplication':
            multiplication()
        elif choice == 'division':
            division()
        elif choice == 'exponentiation':
            exponentiation_function()
        elif choice == 'square root':
            square_root()
        elif choice == 'factorial':
            factorial_second()
        elif choice == 'list management':
            management_list()
        elif choice == 'quit':
            print("Are you sure you want to quit?\nIf yes,enter quit again")
            quit_sure=input('Please enter quit to make a sure\n'
                            'Enter others will back to the starting point: ')
            if quit_sure == 'quit':
                break
            elif quit_sure != 'quit':
                print('Enter your choice again')
                continue
        elif choice != 'addition' or 'subtraction' or 'multiplication' or 'division' or 'exponentiation' or 'square root' or 'factorial' or 'list management' or 'quit':
            print("Invalid choice. Please try to chose again.")
            continue




while True:
    #主程序用于编码公告以及用法
    print('Welcome to the calculator,This calculator will help you to calculate an arithmetic '
          'expression.\nIn this calculator, you can manage a large amount of data and perform basic arithmetic operations.\n'
          'Such as addition, subtraction, multiplication, and division, as well as exponentiation, extraction, and factorial.\n'
          'More functions will be developed in the future, so stay tuned!')
    yn=input("Do you wanna read the Update Notice?(yes/no): )")
    if yn == 'yes':
        print('2026.8.23  The calculator is completed today.\n'
              'The current issue is that it can only perform addition, subtraction, multiplication, and division of two numbers, and cannot handle operations with multiple numbers.\n'
              'This functionality will be updated in the future.\n'
              'Currently, there is no Chinese version available. WARNING,NO CHINESE')
    elif yn == 'no':
        print('')
    elif yn != 'yes' or yn != 'no':
        print("Invalid choice. Please try to chose again.")
        continue

    selection()
    print('Thank you for using calculator')
    break