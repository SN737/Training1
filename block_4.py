a = input()
b = input()

if a == "желтый" or a == "синий" or a == "красный":
    if b == "желтый" or b == "синий" or b == "красный":
        if a == b:
            print(a)
        elif a == "желтый" and b == "красный" or b == "желтый" and a == "красный":
            print("оранжевый")
        elif a == "желтый" and b == "синий" or b == "желтый" and a == "синий":
            print("зеленый")
        elif a == "красный" and b == "синий" or b == "красный" and a == "синий":
            print("фиолетовый")
    else:
        print("ошибка цвета")
else:
    print("ошибка цвета")




