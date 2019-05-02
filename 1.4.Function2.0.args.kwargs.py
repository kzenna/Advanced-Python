# Домашнее задание к лекции 1.
# «Function 2.0 *args, **kwargs»
#
# Кокурникова Лилия Фаритовна, 01.05.19
#
class Contact:
    '''Базовый класс для контактов'''
    def __init__(self, *args, **kwargs):
        self.SecondName = args[0]
        self.FirstName = args[1]
        self.Phone = args[2]
        if len(args) < 4:
            self.Star = False
        else:
            self.Star = args[3]
        if kwargs != "":
            self.Info = kwargs
        else:
            self.Info = {}
        print(args, kwargs)

    def __str__(self):
        '''Определяет поведение функции str(), вызванной для экземпляра класса.'''
        def get_star_description(temp):
            return {
                temp is False: 'Нет',
                temp is True: 'Да'
            }[True]
        return_str = ""
        return_str += "Имя: {SecondName}\nФамилия: {FirstName}\n" \
                      "Телефон: {Phone}\nВ избранных: {Star}\n".format(SecondName=self.SecondName,
                                                                     FirstName=self.FirstName,
                                                                     Phone=self.Phone,
                                                                     Star=get_star_description(self.Star))
        return_str += "Дополнительная информация:\n"
        for key, value in self.Info.items():
            return_str += "\t {0} : {1}\n".format(key, value)
        return_str += "----\n"
        return return_str


class PhoneBook(object):
    '''Базовая телефонная книга'''

    def __init__(self, name):
        self.Name = name
        self.abonents = []

    def print_book(self):
        '''Вывод контактов из телефонной книги'''
        print(self.Name)
        if len(self.abonents) == 0:
            print('======НЕТ ДАННЫХ======')
        else:
            for ii in self.abonents:
                print(ii)
            print('============')

    def add_abonent(self, contact):
        '''Добавление нового контакта'''
        self.abonents.append(contact)

    def del_abonent(self, phone):
        '''Удаление контакта по номеру телефона'''
        if len(self.abonents) == 0:
            print('======НЕТ ДАННЫХ======')
        else:
            ii = 0
            while ii < len(self.abonents):
                if self.abonents[ii].Phone == phone:
                    print('Найдено совпадение. Удаление')
                    del self.abonents[ii]
                else:
                    ii += 1

    def search_star(self):
        '''Поиск всех избранных номеров'''
        if len(self.abonents) == 0:
            print('======НЕТ ДАННЫХ======')
        else:
            for ii in self.abonents:
                if ii.Star is True:
                    print('Найдена запись в избранном:')
                    print(ii)

    def search_abonent(self, SecondName, FirstName):
        '''Поиск контакта по имени и фамилии'''
        if len(self.abonents) == 0:
            print('======НЕТ ДАННЫХ======')
        else:
            for ii in self.abonents:
                if ii.SecondName == SecondName and ii.FirstName == FirstName:
                    print('Найдена запись:')
                    print(ii)


def grouper(iterable, n):
    return [iterable[i:i + n] for i in range(0, len(iterable), n)]

def adv_print(*args, **kwargs):
    #(self, *args, sep=' ', end='\n', file=None):  # known special case of print
    """
    Собственная реализация функции print
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False, start='', max_line=80)
    sep - разделитель между выводимыми значениями (по умолчанию - пробел)
    end - символ, которым заканчивается вывод (по умолчанию - символ новой строки)
    file - file-like объект, в который мы можем перенаправить вывод, который по умолчанию производится в sys.stdout
    flush: whether to forcibly flush the stream.
    start - с чего начинается вывод. По умолчанию пустая строка;
    max_line - максимальная длин строки при выводе.
               Если строка превыщает max_line, то вывод автоматически переносится на новую строку;
               10 - по-умолчанию
    in_file - аргумент, определяющий будет ли записан вывод ещё и в файл
    """
    return_str = ''
    sep_new = ' '
    end_new = ''
    file_new = None
    flush_new = False
    start_new = ''
    max_line_new = 10
    in_file_new = None
    # Разбор доп параметров и установка значений по-умолчанию
    if kwargs != "":
        for key, value in kwargs.items():
            if key == 'sep':
                sep_new = value
            if key == 'end':
                end_new = value
            if key == 'flush':
                flush_new = value
            if key == 'start':
                start_new = value
            if key == 'max_line':
                max_line_new = value
            if key == 'in_file':
                in_file_new = value
    return_str += start_new
    for i in range(0, len(args)):
        return_str += args[i]+sep_new
    return_str += end_new
    if max_line_new < len(return_str):
        temp = [return_str[i:i + max_line_new] for i in range(0, len(return_str), max_line_new)]
        for ii in range(0, len(temp)):
            print(temp[ii], sep='', end='\n', flush=flush_new)
            if in_file_new is None:
                print(temp[ii], sep='', end='\n', flush=flush_new, file=in_file_new)
    else:
        print(return_str, sep='', end='\n', flush=flush_new)
        if in_file_new is None:
            print(return_str, sep='', end='\n', flush=flush_new, file=in_file_new)


if __name__ == '__main__':
    # 1
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    print(jhon)
    jhon = Contact('Robert', 'Smith', '+71234507809', False, icq='@jhony',telegram='@jhony', email='jhony@smith.com')
    print(jhon)
    jhon = Contact('Ivan', 'Smith', '+70234567809', True, telegram='@jhony', email='jhony@smith.com')
    print(jhon)
    # 2
    book = PhoneBook('Телефонная книга №1')
    #book.print_book()
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    book.add_abonent(jhon)
    #book.print_book()
    jhon = Contact('Robert', 'Smith', '+71234507809', False, icq='@jhony',telegram='@jhony', email='jhony@smith.com')
    book.add_abonent(jhon)
    jhon = Contact('Ivan', 'Smith', '+70234567809', True, telegram='@jhony', email='jhony@smith.com')
    book.add_abonent(jhon)
    #book.print_book()
    # Удаление контакта по номеру телефона;
    book.del_abonent('+70234567809')
    #book.print_book()
    # Поиск всех избранных номеров
    #book.search_star()
    # Поиск контакта по имени и фамилии
    # book.search_abonent('Robert', 'Smith')
    book.search_abonent('Robet', 'Smith')

    print('111 ', '2 ', '3 ', '4 ', '5 ', sep='.', end='---', flush=True, file=open("output.txt", "a"))
    print('')
    adv_print('222 ', '2 ', '3 ', '4 ', '5 ', sep='.', end='---', flush=True,
              start='!', max_line=10, in_file=open("output.txt", "a"))
