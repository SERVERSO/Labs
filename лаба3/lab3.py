def zad1Open():
    arg = int(input("Введите 1 для чтения всего файла \nВведите 2 для построчного чтения файла \n"))
    if type(arg) == int:
        with open('C:\\Users\\Максим\\Documents\\лабы\\лаба3\\example.txt', 'r', encoding='utf-8') as fl:
            if arg == 1:

                text = fl.read()
                print(text)
            elif arg == 2:
                arr = fl.readlines()
                for x in range(len(arr)):
                    print(f'Номер строки файла: {x + 1}: Содержимое: {arr[x]}')
                    time.sleep(1)
            else:
                print("Такого метода чтения не существует")



zad1Open()


def zad2Write():
    text = input("Введите тект для записи: ")
    with open('user_input.txt', 'a+', encoding="utf-8") as f:
        f.seek(0)
        cont = f.read()
        if cont:
            text = " " + text
        f.write(text)
        print("файл успешно создан/обновлён")
zad2Write()

def zad3(first_func):
    def out_func():
        try:
            first_func()
        except FileNotFoundError:
            print("К сожалению, файла с таким именем не существует. Операция записи невозможна")
    return  out_func


@zad3
def zad1Mod():
    arg = int(input("Введите 1 для чтения всего файла \nВведите 2 для построчного чтения файла \n"))
    if type(arg) == int:
        with open('C:\\Users\\Максим\\Documents\\лабы\\лаба3\\example1.txt', 'r', encoding='utf-8') as fl:
            if arg == 1:

                text = fl.read()
                print(text)
            elif arg == 2:
                arr = fl.readlines()
                for x in range(len(arr)):
                    print(f'Номер строки файла: {x + 1}: Содержимое: {arr[x]}')
                    time.sleep(1)
            else:
                print("Такого метода чтения не существует")

zad1Mod()