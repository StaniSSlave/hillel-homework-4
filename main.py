# project start
"""
1. Користувач вводить рядок з клавіатури. Порахуйте кількість літер, цифр у рядку. Виведіть обидві кількості на екран. (використовувати цикл)

2. Користувач вводить з клавіатури рядок та символ для пошуку. Порахуйте скільки разів у рядку зустрічається потрібний символ. Отримане число виведіть на екран.

3. Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни. Зробіть у рядку заміну одного слова на інше. Отриманий рядок на екрані.

4. Дано рядок. (зробити зрізи)

- Спершу виведіть третій символ цього рядка.

- У другому рядку виведіть передостанній символ цього рядка.

- У третьому рядку виведіть перші п'ять символів цього рядка.

- У четвертому рядку виведіть весь рядок, крім двох останніх символів.

- У п'ятому рядку виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0, тому символи виводяться з першого).

- У шостому рядку виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.

- У сьомому рядку виведіть усі символи у зворотному порядку.

- У восьмому рядку виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.

- У дев'ятому рядку виведіть довжину цього рядка.

Додатково:

Є певний текст. Реалізуйте наступну функціональність:

■ Змінити текст таким чином, щоб кожне речення починалися з великої літери;

■ Порахуйте скільки разів цифри зустрічаються у тексті;

■ Порахуйте скільки разів розділові знаки зустрічаються в тексті;

■ Порахуйте кількість знаків оклику в тексті.
"""
task_n = 1

while task_n !=5:
    try:
        task_n = int(input("Select please task number, that you want to check: \n"
                        "\t1. Порахуйте кількість літер, цифр у рядку. Виведіть обидві кількості на екран.\n"
                        "\t2. Порахуйте скільки разів у рядку зустрічається потрібний символ.\n"
                        "\t3. Зробіть у рядку заміну одного слова на інше. Отриманий рядок на екрані.\n"
                        "\t4. Дано рядок. Зробити зрізи.\n"
                        "\t5. Stop checking tasks\n"
                        "Enter choise here: "))

        match task_n:
            case 1:
                finish_t1 = "n":
                while finish_t1 == "n":
                    text_t1 = input("Enter please text here to count letters and number: ")
                    symb_c = len(text_t1)
                    num_c = 0
                    let_c = 0
                    #v1
                    for i in range(symb_c):
                        if text_t1[i]=="0" or text_t1[i]=="1" or text_t1[i]=="2" or text_t1[i]=="3" or text_t1[i]=="4" or text_t1[i]=="5" or text_t1[i]=="6" or text_t1[i]=="7" or text_t1[i]=="8" or text_t1[i]=="9":
                            num_c += 1
                        elif text_t1[i]!=" " and text_t1[i]!="0" and text_t1[i]!="1" and text_t1[i]!="2" and text_t1[i]!="3" and text_t1[i]!="4" and text_t1[i]!="5" and text_t1[i]!="6" and text_t1[i]!="7" and text_t1[i]!="8" and text_t1[i]!="9":
                            let_c += 1
                    #v2
                    # for i in range(symb_c):
                    #     num = 0
                    #     for a in range(0,10):
                    #         if text_t1[i] == str(num):
                    #             num_c += 1
                    #         num +=1
                    # n = 0
                    # s = 0
                    # for i in range(symb_c):
                    #     num = 0
                    #     for a in range(0,10):
                    #         c = text_t1[i] != str(num)
                    #         if c == False:
                    #             n += 1
                    #         elif text_t1[i] == " ":
                    #             s += 0.1
                    #         num += 1
                    # let_c = symb_c-n-s
                    print(f"Count of letters: {let_c}")
                    print(f"Count of numbers: {num_c}")

                    finish_t1 = input("Do you want to finish task?\n"
                                      "\ty - yes, n - no\n"
                                      "\tEnter your choice: ")
            case 2:
                finish_t2 = "n"
                while finish_t2 == "n":
                    text_t2 = input("Enter please text here to count quantity of needed symbols: ")
                    symb_t2 = input("Enter symbol, that you want to count in text: ")
                    symb_c_t2 = 0

                    for i in range(len(text_t2)):
                        if symb_t2 == text_t2[i]:
                            symb_c_t2 += 1
                    print(f"Quantity of \"{symb_t2}\" in text is {symb_c_t2}")

                    finish_t2 = input("Do you want to finish task?\n"
                                      "\ty - yes, n - no\n"
                                      "\tEnter your choice: ")
            case 3:
                finish_t3 = "n"
                while finish_t3 == "n":


                    finish_t3 = input("Do you want to finish task?\n"
                                      "\ty - yes, n - no\n"
                                      "\tEnter your choice: ")
            case 4:
                finish_t4 = "n"
                while finish_t4 == "n":
                    finish_t4 = input("Do you want to finish task?\n"
                                      "\ty - yes, n - no\n"
                                      "\tEnter your choice: ")
            case 5:
                print("Thanks for your time!")
                break
            case _:
                raise Exception("Please enter a valid task number!")
    except ValueError as e:
        print("Error: Please enter only integers!")
    except Exception as e:
        print(f"Error: {e}")