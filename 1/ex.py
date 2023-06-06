def show_data():
    with open('data.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    return data
def get_new_user():
    print('Введите данные нового абонента:')
    surname = input('Фамилия: ')
    name = input('Имя: ')
    phone= input('Телефон: ')
    patronymic = input('Описание: ')
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(surname + " " + name + " " + phone + " " + patronymic +"\n")
def find_data():
    search = input('Выбирите, пожалуста, по чем вы хотите искать: ')
    search_result = list()
    if search == "имя":
        
        with open('data.txt', 'r', encoding='utf-8') as file:
            data = list(file.read().split())
            searchname = input('Введите искомое имя:')
            for i in range (len(data)):
                if data[i] == searchname:
                    search_result.append(data[i-1])
                    search_result.append(data[i])
                    search_result.append(data[i+1])
                    search_result.append(data[i+2])
            if searchname not in data:
                print('Искомое имя отсутствует в списке') 
    elif search == 'фамилия':
        with open('data.txt', 'r', encoding='utf-8') as file:
            data = list(file.read().split())
            searchsurname= input('Введите искомую фамилию:')
            for i in range (len(data)):
                if data[i] == searchsurname:
                    search_result.append(data[i])
                    search_result.append(data[i+1])
                    search_result.append(data[i+2])
                    search_result.append(data[i+3])
            if searchsurname not in data:
                print('Искомая фамилия отсутствует в списке')
    elif search == 'телефон':
        with open('data.txt', 'r', encoding='utf-8') as file:
            data = list(file.read().split())
            searchphone = input('Введите искомый номер:')
            for i in range (len(data)):
                if data[i] == searchphone:
                    search_result.append(data[i-2])
                    search_result.append(data[i-1])
                    search_result.append(data[i])
                    search_result.append(data[i+1])
            if searchphone not in data:
                print('Искомый телефон отсутствует в списке')
    return print ("".join(search_result))
 
while True:
    mode = input('Выберите режим работы справочника' + '\n' +'0-поиск, 1-чтение файла, 2-добавление в файл, 3-выход: ')
    if mode == '1':
        print(show_data())
    elif mode == '0':
        find_data()
    elif mode == '2':
        get_new_user()
    elif mode == '3':   
        break
    else:
        print('No mode')
