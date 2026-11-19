import Processor_Selection

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

    Processor_Selection.selection()
    print('Thank you for using calculator')
    break