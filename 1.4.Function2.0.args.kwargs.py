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
            # print('!=')
            self.Info = kwargs
        else:
            self.Info = {}

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
    book.print_book()
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    book.add_abonent(jhon)
    book.print_book()
    jhon = Contact('Robert', 'Smith', '+71234507809', False, icq='@jhony',telegram='@jhony', email='jhony@smith.com')
    book.add_abonent(jhon)
    jhon = Contact('Ivan', 'Smith', '+70234567809', True, telegram='@jhony', email='jhony@smith.com')
    book.add_abonent(jhon)
    book.print_book()
    # Удаление контакта по номеру телефона;
    book.del_abonent('+70234567809')
    book.print_book()
    jhon = Contact('Ivan', 'Smith', '+70234567809', True, telegram='@jhony', email='jhony@smith.com')
    book.add_abonent(jhon)
    # Поиск всех избранных номеров
    book.search_star()
    # Поиск контакта по имени и фамилии
    book.search_abonent('Robert', 'Smith')
    book.search_abonent('Robet', 'Smith')
