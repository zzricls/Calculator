class Calculator:
    """docstring for Calculator"""
    """计算器完整逻辑"""
    def __init__(self):
        self.current = 0.0
        self.last_result = 0.0
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.d = 0.0
        self.e = 0.0
        self.f = 0.0

    def add(self):
        #加法函数
        num = float(input(''))
        self.current += num
        return self.current

    def subtract(self):
        #减法函数
        num = float(input(''))
        self.current -= num
        return self.current

    def multiply(self):
        #乘法函数
        num = float(input(''))
        self.current *= num
        return self.current

    def divide(self):
        #除法函数
        while True:
            num = float(input(''))
            if num == 0.0:
                print("The number cannot be zero（此数字不能为零）")
                continue
            else:
                break
        self.current /= num
        return self.current


    def power(self):
        #幂运算
        exponent = float(input(''))
        self.current **= exponent
        return self.current

    def equal(self):
        #输入等号获得结果
        print(self.current)
        self.last_result = self.current
        return self.current

    def view_last_result(self):
        #查看上一个结果，并选择是否将其作为目前数值
        print(self.last_result)
        choice = input('Want to use this number to make a new figure?(y/n)'
                       '（是否用上一个结果进行新的运算(y/n)）')
        while True:
            if choice == "y":
                self.current = self.last_result
                break
            elif choice == "n":
                break
            else:
                print("Please enter a valid input（请输入有效语句）")
                continue

    def factorial(self):
        """docstring for factorial
        It will automatically round the current number"""
        """阶乘函数完整逻辑"""
        # 阶乘函数
        n = self.current
        self.current = int(self.current)
        if self.current == 0:
            self.current = 1
            return self.current
        elif self.current <= 0:
            self.current = n
            return self.current
        elif self.current > 0:
            num = self.current - 1
            while num > 0:
                self.current *= num
                num -= 1
            return self.current

    @staticmethod
    def management_list():
        #数据管理
        numbers = []  # 创建一个空列表

        print("Please enter the number(Click enter to end)（请输入数字(回车结束输入)）:")

        while True:
            user_input = input(">>> ")

            # 退出条件：用户输入为空字符串
            if user_input == "":
                print("input ends（退出）")
                break

            try:
                # 尝试将输入转换为数字（支持整数和小数）
                num = float(user_input)
                numbers.append(num)  # 将数字存入列表
                print(f"Added {num},The current list is:{numbers}（已加入{num}，目前列表为{numbers}）")
            except ValueError:
                print("Please enter a number（请输入数字）")

        print(f"\nThe final list:{numbers}（最终列表为{numbers}）")
        while True:
            user_require = input(
                "Please chose the service(summation,average,maximum,minimum,median,variance)\n(Click enter to end)\n:"
                "（请输入选择(求和，求平均数，求最大值，求最小值，求中位数，求方差)（仍然输入英文）")
            if user_require == "":
                print("input ends（退出）")
                break
            elif user_require == "summation":
                print(sum(numbers))
            elif user_require == "average":
                print(sum(numbers) / len(numbers))
            elif user_require == "maximum":
                print(max(numbers))
            elif user_require == "minimum":
                print(min(numbers))
            elif user_require == "median":
                if len(numbers) > 0:
                    sorted_numbers = sorted(numbers)  #排序
                    n = len(sorted_numbers)
                    if n % 2 == 1:  #列表元素数目为奇数
                        median = sorted_numbers[n // 2]
                    else:  #列表元素数目为偶数
                        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
                    print(f"The median of the list is:{median}"
                          f"中位数为{median}")
                else:
                    print("There is no numbers to manage（没有数字我求尼玛）")
            elif user_require == "variance":
                n = len(numbers)

                if n == 0:
                    print("There is no numbers to manage（没有数字我求尼玛）")
                else:
                    #计算平均数
                    mean = sum(numbers) / n

                    # 计算离差平方和
                    squared_diff_sum = sum((x - mean) ** 2 for x in numbers)

                    # 总体方差（除以 n）
                    population_var = squared_diff_sum / n

                    # 样本方差（除以 n-1），需要 n >= 2
                    if n >= 2:
                        sample_var = squared_diff_sum / (n - 1)
                        print(f"Total variance:{population_var}"
                              f"方差为{population_var}")
                        print(f"Sample variance:{sample_var}"
                              f"样本方差为{sample_var}")
                    else:
                        print(f"Total variance：{population_var}(Only one number,unable to calculate variance)"
                              f"方差为{population_var}（就他妈一个数字我求你妈样本方差）")
            elif user_require == "quit":
                break

    def reset(self):
        """docstring for reset"""
        """归零完整逻辑"""
        #归零操作
        self.current = 0.0
        print('The result has been reset to 0'
              '（结果已经归零）')
        return self.current

    def store(self):
        #储存数操作
        while True:
            choice = input('Which variable do you want to store the currently calculated value in'
                           'a,b,c,d,e,f(Enter q to exit)'
                           '你想将目前数值储存到哪个变量'
                           'a,b,c,d,e,f（输入q退出）')
            if choice in ('a','b','c','d','e','f','q'):
                break
            else:
                print("Please enter a valid input（请输入有效语句，艹）")
                continue
        while True:
            if choice == "a" :
                self.a = self.current
                break
            elif choice == "b" :
                self.b = self.current
                break
            elif choice == "c" :
                self.c = self.current
                break
            elif choice == "d" :
                self.d = self.current
                break
            elif choice == "e" :
                self.e = self.current
                break
            elif choice == "f" :
                self.f = self.current
                break
            elif choice == "q" :
                break

    def check_store(self):
        #查看储存数操作
        while True:
            choice = input('Which variable do you want to know'
                           '你想查询哪个变量的值')
            if choice in ('a','b','c','d','e','f'):
                break
            else:
                print("Please enter a valid input"
                      "请输入有效语句")
                continue
        while True:
            if choice == "a" :
                print(self.a)
                break
            elif choice == "b" :
                print(self.b)
                break
            elif choice == "c" :
                print(self.c)
                break
            elif choice == "d" :
                print(self.d)
                break
            elif choice == "e" :
                print(self.e)
                break
            elif choice == "f" :
                print(self.f)
                break

class Application:
    """docstring for Application"""
    """计算机面板"""
    def __init__(self):
        self.calc = Calculator()

    @staticmethod
    def _get_numbers():
        #第一次启动时，输入第一个数
        while True:
            num = input("Please enter the number"
                        "请输入数字")
            try:
                num = float(num)
                return num
            except ValueError:
                print("Please enter a number"
                      "输入数字行不行")
                continue


    @staticmethod
    def _get_operation():
        #获得运算方式
        while True:
            operation = input("Please enter the operation('+','-','*','/','!','r','=','q','^','s','c','v')\n"
                              "(Enter q to exit)(r means reset)"
                              "(^ means power)(s means store)"
                              "(c means check)(v means view the last result)")
            if operation == "q":
                return 'q'
            elif operation in ('+', '-', '*', '/', '!', 'r', '=', 'q', '^', 's', 'c', 'v'):
                return operation

    def run(self):
        """docstring for run
        It will run the application"""
        """计算器运行完整逻辑"""
        #计算器运行完整逻辑

        print("Welcome to Calculator")
        w_r_update = input("Would you like to read the update notice?(y/n)"
                           "是否阅读更新公告(y/n)")
        while True:
            #更新公告
            if w_r_update == "y":
                print('01 2026.9.5  The calculator is officially completed today\n'
                      'As of now, this calculator boasts two modes: basic data processing and normal operation.\n'
                      'The calculation mode encompasses four arithmetic operations, factorial, and exponentiation.\n'
                      'Compared to the first generation, it can perform continuous operations, but it cannot use parentheses to specify the order of operations.\n'
                      'Additionally, it allows for digital storage (supporting six storage variables), resetting to zero, and viewing the previous result.\n'
                      '（更新公告就不提供中文了，嘻嘻）')
                break
            elif w_r_update == "n":
                print('Calculator starting（计算器，启动！）')
                break
            else:
                print("Please enter a valid input"
                      "输入y或者n不行吗")
                continue

        print('M stands for data management mode, and C stands for computation mode\n'
              '（M意思是数据管理模式，C意思是计算模式）')#按键提示
        while True:
            answer = input('Please chose the mode（请选择模式）')
            if answer == "M":
                self.calc.management_list()
            elif answer == "C":
                while True:
                    if self.calc.current == 0.0:
                        num = self._get_numbers()
                        self.calc.current = num
                    else:
                        break

                while True:
                    op = self._get_operation()
                    if op == "+":
                        self.calc.add()
                        continue
                    elif op == "-":
                        self.calc.subtract()
                        continue
                    elif op == "*":
                        self.calc.multiply()
                        continue
                    elif op == "/":
                        self.calc.divide()
                        continue
                    elif op == "!":
                        self.calc.factorial()
                        continue
                    elif op == "=":
                        self.calc.equal()
                        continue
                    elif op == "^":
                        self.calc.power()
                        continue
                    elif op == "r":
                        self.calc.reset()
                        continue
                    elif op == "s":
                        self.calc.store()
                        continue
                    elif op == "c":
                        self.calc.check_store()
                        continue
                    elif op == "v":
                        self.calc.view_last_result()
                        continue
                    elif op == "q":
                        break
                    else:
                        print("Please enter a valid operation（听老子的话，别输入乱七八糟的东西）")
                        continue
                continue
            elif answer == "q":
                print('Thank you for using calculator'
                      '谢谢使用')
                break
            else:
                print("Please enter a valid operation"
                      "（给老子输入有效语句！）")
                continue



if __name__ == "__main__":
    APP = Application()
    APP.run()


