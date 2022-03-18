task_list = ["инженер-конструктор Игорь", "главный бухгалтер МАРИНА", "токарь высшего разряда нИКОЛАй",
             "директора аэлита"]

for i in range(len(task_list)):
    task_list[i] = task_list[i].split(" ")
    print(f"Привет, {task_list[i][-1].capitalize()}!")
