# project start
"""
1. Користувач вводить рядок з клавіатури. Порахуйте кількість літер, цифр у рядку. Виведіть обидві кількості на екран.

2. Користувач вводить з клавіатури рядок та символ для пошуку. Порахуйте скільки разів у рядку зустрічається потрібний
символ. Отримане число виведіть на екран.

3. Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни. Зробіть у рядку заміну одного слова на
інше. Отриманий рядок на екрані.

4. Дано рядок. (зробити зрізи)

- Спершу виведіть третій символ цього рядка.

- У другому рядку виведіть передостанній символ цього рядка.

- У третьому рядку виведіть перші п'ять символів цього рядка.

- У четвертому рядку виведіть весь рядок, крім двох останніх символів.

- У п'ятому рядку виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0, тому
символи виводяться з першого).

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

while task_n != 5:
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
                finish_t1_l = "y"
                while finish_t1_l == "y":
                    text_t1 = input("\tEnter please text here to count letters and number: ")
                    symb_c = len(text_t1)

                    num_c = 0
                    let_c = 0

                    # v1
                    #
                    # for i in range(symb_c):
                    #     if text_t1[i]=="0" or text_t1[i]=="1" or text_t1[i]=="2" or text_t1[i]=="3" or text_t1[i]=="4" or text_t1[i]=="5" or text_t1[i]=="6" or text_t1[i]=="7" or text_t1[i]=="8" or text_t1[i]=="9":
                    #         num_c += 1
                    #     elif text_t1[i]!=" " and text_t1[i]!="0" and text_t1[i]!="1" and text_t1[i]!="2" and text_t1[i]!="3" and text_t1[i]!="4" and text_t1[i]!="5" and text_t1[i]!="6" and text_t1[i]!="7" and text_t1[i]!="8" and text_t1[i]!="9":
                    #         let_c += 1

                    # v2
                    for i in range(symb_c):
                        num = 0
                        for a in range(0, 10):
                            if text_t1[i] == str(num):
                                num_c += 1
                            num += 1
                    n = 0
                    s = 0
                    for i in range(symb_c):
                        num = 0
                        for a in range(0, 10):
                            c = text_t1[i] != str(num)
                            if not c:
                                n += 1
                            elif text_t1[i] == " ":
                                s += 0.1
                            num += 1
                    let_c = symb_c - n - s

                    # v3  # only for text on English!!!!!!!
                    # for i in range(len(text_t1)):
                    #     if 65 <= ord(text_t1[i]) <= 90 or 97 <= ord(text_t1[i]) <= 122:
                    #         let_c += 1
                    #     elif 48 <= ord(text_t1[i]) <= 57:
                    #         num_c += 1

                    print(f"\tCount of letters: {let_c}")
                    print(f"\tCount of numbers: {num_c}")

                    while finish_t1_l != "y" or finish_t1_l != "n":
                        finish_t1 = input("Do you want to continue?\n"
                                          "\ty - yes, n - no\n"
                                          "\tEnter your choice: ")
                        finish_t1_l = finish_t1.lower()
                        try:
                            if finish_t1_l == "y":
                                break
                            elif finish_t1_l == "n":
                                break
                            else:
                                raise Exception("Please enter valid answer!")
                        except Exception as e:
                            print(f"\tError: {e}")
            case 2:
                finish_t2_l = "y"
                while finish_t2_l == "y":
                    text_t2 = input("\tEnter please text here to count quantity of needed symbols: ")
                    symb_t2 = input("\tEnter symbol, that you want to count in text: ")

                    try:
                        if len(symb_t2) == 1:

                            # v1
                            symb_c_t2 = 0
                            for i in range(len(text_t2)):
                                if symb_t2 == text_t2[i]:
                                    symb_c_t2 += 1
                            print(f"\tQuantity of \"{symb_t2}\" in text is {symb_c_t2}")

                            # v2
                            # print(f"Quantity of \"{symb_t2}\" in text is {text_t2.count(symb_t2)}")

                        else:
                            raise Exception("Enter only one character, please!")
                    except Exception as e:
                        print(f"\tError: {e}")

                    while finish_t2_l != "y" or finish_t2_l != "n":
                        finish_t2 = input("Do you want to continue?\n"
                                          "\ty - yes, n - no\n"
                                          "\tEnter your choice: ")
                        finish_t2_l = finish_t2.lower()
                        try:
                            if finish_t2_l == "y":
                                break
                            elif finish_t2_l == "n":
                                break
                            else:
                                raise Exception("Please enter valid answer!")
                        except Exception as e:
                            print(f"\tError: {e}")
            case 3:
                finish_t3_l = "y"
                while finish_t3_l == "y":
                    text_t3 = input("\tEnter please text here to switch content: ")
                    find_t3 = input("\tEnter symbol or word(s), that you want to remove: ")
                    new_t3 = input("\tEnter symbol or word(s), that you want to use instead: ")

                    #v1
                    last_ch = 0
                    first_ch = 0
                    word_search = -1
                    for i in range(len(text_t3)-1):
                        if word_search == len(find_t3):
                            print(text_t3[:first_ch] + new_t3 + text_t3[last_ch + 1:])
                            break
                        else:
                            a = 0
                            word_search = 0
                            for n in range(len(find_t3)):
                                if find_t3[n] == text_t3[i]:
                                    word_search += 1
                                    last_ch = i
                                    i += 1
                                    first_ch = last_ch-len(find_t3)+1
                                    if word_search == len(find_t3):
                                        break
                    print("Needed word or symbol was not found. Try again!")

                    #v2
                    # text_ch_t3 = text_t3.replace(find_t3, new_t3)
                    # print(text_ch_t3)

                    while finish_t3_l != "y" or finish_t3_l != "n":
                        finish_t3 = input("Do you want to continue?\n"
                                          "\ty - yes, n - no\n"
                                          "\tEnter your choice: ")
                        finish_t3_l = finish_t3.lower()
                        try:
                            if finish_t3_l == "y":
                                break
                            elif finish_t3_l == "n":
                                break
                            else:
                                raise Exception("Please enter valid answer!")
                        except Exception as e:
                            print(f"\tError: {e}")
            case 4:
                finish_t4_l = "y"
                while finish_t4_l == "y":
                    text_t4 = input("\tEnter please text here to operate with it: ")

                    print(f"1. Third character: {text_t4[2]}")
                    print(f"2. Penultimate character: {text_t4[len(text_t4) - 2]}")
                    print(f"3. First 5 characters: {text_t4[0:4]}")
                    print(f"4. Almost all characters(without last two): {text_t4[0:len(text_t4) - 3]}")
                    print(f"5. All characters with paired indices: {text_t4[::2]}")
                    print(f"6. All characters with odd indices: {text_t4[1::2]}")
                    print(f"7. Reversed string: {text_t4[::-1]}")
                    print(f"8. Almost all characters(without last two): {text_t4[len(text_t4) - 1::-2]}")
                    print(f"9. String Length: {len(text_t4)}")

                    while finish_t4_l != "y" or finish_t4_l != "n":
                        finish_t4 = input("Do you want to continue?\n"
                                          "\ty - yes, n - no\n"
                                          "\tEnter your choice: ")
                        finish_t4_l = finish_t4.lower()
                        try:
                            if finish_t4_l == "y":
                                break
                            elif finish_t4_l == "n":
                                break
                            else:
                                raise Exception("Please enter valid answer!")

                        except Exception as e:
                            print(f"\tError: {e}")
            case 5:
                print("\tThanks for your time!")
                break
            case _:
                raise Exception("Please enter a valid task number!")
    except ValueError as e:
        print("\tError: Please enter only integers!")
    except Exception as e:
        print(f"\tError: {e}")
