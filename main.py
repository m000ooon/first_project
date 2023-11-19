def date_maker(st):  # Задание номер 1
    months = ['', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля',
              'августа', 'сентября', 'октября', 'ноября', 'декабря']
    months_days = ['', 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def leap_year(y):
        if y % 4 == 0 and y % 25 != 0:
            return 1
        elif y % 400 == 0:
            return 1
        else:
            return 0

    st = [int(x) for x in st.replace('.', ' ').replace(',', '').split()]

    if leap_year(st[2]):
        months_days[2] += 1

    if len(st) == 3:
        if 1 <= st[1] <= 12 and 1 <= st[0] <= months_days[st[1]] and st[2] > 0:
            st = f'{str(st[0])} {months[st[1]]} {str(st[2])} года\n'
            return st
    return 'Введённый формат даты не существует.\n'


def name_diary(names):  # Задание номер 2
    ls = sorted(set(names))
    dt = dict()
    for i in ls:
        dt[i] = names.count(i)
    return dt


def full_name(name):  # Задание номер 3
    b = [x for x in name.keys()]
    if len(b) == 3:
        return f"{name['last_name']} {name['first_name']} {name['middle_name']}"
    elif len(b) == 2:
        if not ('last_name' in b):
            return f"{name['first_name']} {name['middle_name']}"
        elif not ('first_name' in b):
            return name['last_name']
        else:
            return f"{name['last_name']} {name['first_name']}"
    elif len(b) == 1:
        if 'middle_name' not in b:
            print(name[b[0]])
    return 'Нет данных'
