class Calculator:
    def __init__(self):
        self.current = 0.0
        self.last_result = 0.0
        self.storage = {}


    def computation(self):
        def add():
            # 加法函数
            _num = float(input('Please enter a number'))
            self.current += _num
            return self.current

        def subtract():
            # 减法函数
            _num = float(input('Please enter a number'))
            self.current -= _num
            return self.current

        def multiply():
            # 乘法函数
            _num = float(input('Please enter a number'))
            self.current *= _num
            return self.current

        def divide():
            # 除法函数
            while True:
                _num = float(input('Please enter a number'))
                if _num == 0.0:
                    print("The number cannot be zero")
                    continue
                else:
                    break
            self.current /= _num
            return self.current

        def power():
            # 幂运算
            exponent = float(input('Please enter a number'))
            self.current **= exponent
            return self.current

        def equal():
            # 输入等号获得结果
            print(self.current)
            self.last_result = self.current
            return self.current

        def view_last_result():
            # 查看上一个结果，并选择是否将其作为目前数值
            print(self.last_result)
            while True:
                choice = input('Want to use this number to make a new figure?(y/n)')
                if choice == "y":
                    self.current = self.last_result
                    break
                elif choice == "n":
                    break
                else:
                    print("Please enter a valid input")
                    continue

        def factorial():
            self.current = float(int(self.current))
            if self.current == 0.0:
                self.current = 1
                return self.current
            elif self.current <= 0.0:
                print("Negative numbers do not have a factorial")
                return self.current
            else:
                n = self.current - 1.0
                while n > 0.0:
                    self.current *= n
                    n -= 1
                return self.current

        def reset():
            """docstring for reset"""
            # 归零操作
            self.current = 0.0
            print('The result has been reset to 0')
            return self.current

        def store():
            while True:
                choice = input('Which variable do you want to store?\n'
                               '(a,b,c,d,e,f,g) (Enter q to exit)')
                if choice == 'q':
                    break
                elif choice in ('a', 'b', 'c', 'd', 'e', 'f', 'g'):
                    self.storage[choice] = self.current
                    print('Successfully stored')
                    break
                else:
                    print("Please enter a valid input")

        def check_store():
            while True:
                choice = input('Which variable do you want to check?\n'
                               '(a,b,c,d,e,f,g) (Enter q to exit)')
                if choice == 'q':
                    break
                if choice in ('a', 'b', 'c', 'd', 'e', 'f', 'g'):
                    value = self.storage.get(choice, 'This variable have not been stored')
                    print(f"{choice} = {value}")
                    break
                else:
                    print("Please enter a valid input")

        def _get_numbers():
            # 第一次启动时，输入第一个数
            while True:
                _num = input("Please enter the number(Enter q to exit)")
                if _num == "q":
                    break
                try:
                    _num = float(_num)
                    return _num
                except ValueError:
                    print("Please enter a number")
                    continue

        def _get_operation():
            # 获得运算方式
            while True:
                operation = input("Please enter the operation('+','-','*','/','!','r','=','q','^','s','c','v')\n"
                                  "(Enter q to exit)(r means reset)"
                                  "(^ means power)(s means store)"
                                  "(c means check)(v means view the last result)")
                if operation == "q":
                    return 'q'
                elif operation in ('+', '-', '*', '/', '!', 'r', '=', 'q', '^', 's', 'c', 'v'):
                    return operation

        while True:
            if self.current == 0.0:
                num = _get_numbers()
                self.current = num
            else:
                break

        op_map = {
            '+': add,'-': subtract,'*': multiply,
            '/': divide,'^': power,'s': store,
            '!': factorial,'r': reset,'=': equal,
            'c': check_store,'v': view_last_result
        }
        while True:
            op = _get_operation()
            if op == 'q':
                break
            elif op in op_map:
                op_map[op]()
            else:
                print("Please enter a valid input")

    @staticmethod
    def management_list():
        # 数据管理
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

        print(f"\nThe final list:{numbers}")
        while True:
            user_require = input(
                "Please chose the service(summation,average,maximum,minimum,median,variance)\n(Click enter to end)\n:")
            if user_require == "":
                print("input ends")
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
                    sorted_numbers = sorted(numbers)  # 排序
                    n = len(sorted_numbers)
                    if n % 2 == 1:  # 列表元素数目为奇数
                        median = sorted_numbers[n // 2]
                    else:  # 列表元素数目为偶数
                        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
                    print(f"The median of the list is:{median}")
                else:
                    print("There is no numbers to manage")
            elif user_require == "variance":
                n = len(numbers)
                if n == 0:
                    print("There is no numbers to manage")
                else:
                    # 计算平均数
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

class Application:
    """docstring for Application"""
    def __init__(self):
        self.calc = Calculator()

    def run(self):
        print("Welcome to Calculator")

        while True:
            # 更新公告
            w_r_update = input("Would you like to read the update notice?(y/n)")
            if w_r_update == "y":
                print('')#还没有更新公告
                break
            elif w_r_update == "n":
                print('Calculator starting')
                break
            else:
                print("Please enter a valid input")
                continue

        print('M stands for data management mode, and C stands for computation mode')  # 按键提示
        mode_list = {
            'M': self.calc.management_list , 'C': self.calc.computation
        }
        while True:
            answer = input('Please chose the mode(Enter q to exit)')
            if answer == 'q':
                print('Thank you for using calculator')
                break
            elif answer in mode_list:
                mode_list[answer]()
            else:
                print("Please enter a valid input")
                continue

if __name__ == '__main__':
    application = Application()
    application.run()

