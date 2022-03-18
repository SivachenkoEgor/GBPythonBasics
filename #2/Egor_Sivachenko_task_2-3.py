task_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
skipper = 0

for i in task_list:
    if skipper != 0:
        skipper -= 1
        continue
    lstriped_value = i.lstrip('+', ).lstrip('-')
    if lstriped_value.isdigit():
        task_list.insert(task_list.index(i), '"')
        task_list.insert(task_list.index(i) + 1, '"')
        skipper = 2
        if len(lstriped_value) == 1:
            if i == lstriped_value:
                task_list[task_list.index(i)] = "0" + i
            else:
                task_list[task_list.index(i)] = i[0] + "0" + i[1]

output_string = " ".join(task_list)

temp = output_string
new_output = ""

# я уверен, что это отвратительный алгоритм, но это лучшее, что я придумал. Надеюсь посмотреть, как это делать правильно
while temp.count('"') > 0:
    new_output += temp[:temp.find('"')]
    temp = temp[temp.find('"'):]
    temp2 = temp[1:]
    temp2 = temp2[:temp2.find('"')]
    temp2 = temp2.strip()
    temp2 = '"' + temp2 + '"'
    new_output += temp2
    temp = temp[1:]
    ind = temp.find('"') + 1
    temp = temp[ind:]
new_output += temp

print(task_list)
print(new_output)
print(output_string)
