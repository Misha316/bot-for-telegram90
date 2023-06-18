################################################################################
                    #ALL ORDERS FUNC AND ARRAYS OBJECT ORDER
################################################################################
class Executors():  # Класс исполнители (отвечает за работу всех исполнителей)
    executors = []
    size = 0
    def list_users(self):
        temp=[]
        for i in range(int(self.size)):
            self.add()
            self.executors[i].read(i)
        for i in range(int((self.size / 2)/2)):
            temp.append(self.executors[i].name)
        return list(temp)

    def orders_add_executors(self,user_name,money):
        for i in range(int(self.size)):
            self.add()
            self.executors[i].read(i)
        for i in range(int(self.size / 2)):
            if user_name == self.executors[i].user_name:
                self.add_orders_size(self.executors[i].user_name)
                self.add_money(self.executors[i].user_name,money)
                self.executors[i].show()
    def id_test(self,id,num):
        str_ = ""
        for i in range(int(self.size)):
            self.add()
            self.executors[i].read(i)
        for i in range(int(self.size / 2)):
            if id == self.executors[i].user_id:
                if(num==0):
                    str_ = str(self.executors[i].get_executor_tgmassage())
                elif(num==1):
                    str_=int(self.executors[i].money)
                elif(num==2):
                    str_=str(self.executors[i].user_name)
                elif(num==17):
                    str_ = str(self.executors[i].get_executor())
                elif (num == 3):
                    str_ = str(self.executors[i].user_name)
                    self.add_orders_size(str_)
        return str_
    def user_name_test(self,text,num):
        str_ = ""
        for i in range(int(self.size)):
            self.add()
            self.executors[i].read(i)
        for i in range(int(self.size / 2)):
            if text == self.executors[i].name:
                str_=int(self.executors[i].user_id)
        return self.id_test(str_,num)
    def my_profile(self,id):
        return self.id_test(id,0)
    def my_money(self,id):
        return self.id_test(id,1)
    def protect_id(self,id):
        self.read_size()
        protect = False
        for i in range(int(self.size)):
            self.add()
            self.executors[i].read(i)
        for i in range(int(self.size / 2)):
            if id == self.executors[i].user_id:
                protect = True
        return protect

    def read_size(self):  # Cчитаем сколько строк в файле, что бы при вычитании из файла пользователей, создавать под их количество обьекты
        # with open(r"Executor/executors.txt", 'r') as fp:
        self.size = 0
        with open("Executor/executors.txt", 'r') as file:
            for line in file:
                self.size += 1
    def add_orders_size(self,name):     #Добавляем активних пользователей
            self.size = 0
            self.read_size()
            for i in range(self.size):
                if self.executors[i].user_name == name:
                    self.executors[i].orders +=1
                    self.executors[i].activ_orders +=1

    def add_money(self, name,money):  #добавляем прибыль
        self.size = 0
        self.read_size()
        self.executors[0].re_write()
        for i in range(self.size):
            if self.executors[i].user_name == name:
                money=(money/100)*self.executors[i].stavka
                self.executors[i].money += int(money)
            self.executors[i].add_write()

    def add_read(self):  # Cоздаем количество обьектов под количество исполнителей в файле
        self.read_size()
        for i in range(self.size):
            self.executors.append(Executor())

    def add(self):  # Добавляем новый обьект для его создания в файле
        self.executors.append(Executor())
        self.size += 1

    def protect_add_executor(self, name, user_name, user_id, age, stavka, rang, orders, gave_orders, faild_orders,
                             activ_orders, money, card):
        # True проверка отработала и нашла похожее, False проверка отработала и не нашла похожего ника (создаем в случае если ника такого нету)
        try:
            self.read_size()
            protect = False
            for i in range(int(self.size)):
                self.add()
                self.executors[i].read(i)
            for i in range(int(self.size / 2)):
                if name == self.executors[i].name:
                    protect = True
            if protect == False:
                self.add()
                self.executors[(self.size - 1) / 2].add_executor(name, user_name, user_id, age, stavka, rang, orders,
                                                                 gave_orders, faild_orders, activ_orders, money, card)
            return protect
        except:
            self.add()
            self.executors[(self.size - 1) / 2].add_executor(name, user_name, user_id, age, stavka, rang, orders,
                                                             gave_orders, faild_orders, activ_orders, money, card)
            return False

    def show(self):  # Просмотр всех исполнителей
        self.add_read()
        for i in range(self.size):
            self.executors[i].read(i)
            self.executors[i].show()
################################################################################
                            #ORDER DATA AND FUNCTIONAL
################################################################################
class Executor():  # Класс исполнитель (отвечает за шаблон реализации каждого исполнителя)
    name = ""
    user_name = ""
    user_id = 0
    age = 0
    stavka = 0
    rang = ""
    orders = 0
    gave_orders = 0
    faild_orders = 0
    activ_orders = 0
    money = 0
    card = 0

    def add_write(self):  # Записываем исполнителя нового в файл(со всеми его данными по форме)
        write=open("Executor/executors.txt","a+")
        #write = open("executors.txt", "a+")
        write.write(f"{self.name} "
                    f"{self.user_name} "
                    f"{self.user_id} "
                    f"{self.age} "
                    f"{self.stavka} "
                    f"{self.rang} "
                    f"{self.orders} "
                    f"{self.gave_orders} "
                    f"{self.faild_orders} "
                    f"{self.activ_orders} "
                    f"{self.money} "
                    f"{self.card}\n")
        write.close()
    def re_write(self):
        write = open("Executor/executors.txt", "w")
        write.write(f"")
    def read(self, num):  # Записываем исполнителя нового в файл(со всеми его данными по форме)
        # with open("Executor/executors.txt") as read:
        with open("Executor/executors.txt") as read:
            s = 0
            for i in read.readlines():
                if s == num:
                    self.name, self.user_name, self.user_id, self.age, self.stavka, self.rang, self.orders, self.gave_orders, self.faild_orders, self.activ_orders, self.money, self.card = i.strip().split(
                        " ")
                    self.age = int(self.age)
                    self.stavka = int(self.stavka)
                    self.user_id = int(self.user_id)
                    self.orders = int(self.orders)
                    self.gave_orders = int(self.gave_orders)
                    self.faild_orders = int(self.faild_orders)
                    self.activ_orders = int(self.activ_orders)
                    self.money = int(self.money)
                    self.card = int(self.card)
                s += 1

    def add_executor(self, name, user_name, user_id, age, stavka, rang, orders, gave_orders, faild_orders, activ_orders,
                     money, card):  # Добавление исполнителя с записью в файл
        self.name = name
        self.user_name = user_name
        self.user_id = user_id
        self.age = age
        self.stavka = stavka
        self.rang = rang
        self.orders = orders
        self.gave_orders = gave_orders
        self.faild_orders = faild_orders
        self.activ_orders = activ_orders
        self.money = money
        self.card = card
        self.add_write()

    def show(self):  # Просмотр данных исполнителя
        print(f"{self.name} "
              f"{self.user_name} "
              f"{self.user_id} "
              f"{self.age} "
              f"{self.stavka} "
              f"{self.rang} "
              f"{self.orders} "
              f"{self.gave_orders} "
              f"{self.faild_orders} "
              f"{self.activ_orders} "
              f"{self.money} "
              f"{self.card} ")

    def get_executor(self):
        return (f"Им'я: {self.name} \n"
                f"Тег: {self.user_name} \n"
                f"ID: {self.user_id} \n"
                f"Возраст: {self.age} \n"
                f"Ставка: {self.stavka}% \n"
                f"Ранг: {self.rang} \n"
                f"Заказы: {self.orders} \n"
                f"Переданые заказы: {self.gave_orders} \n"
                f"Плохо исполненые: {self.faild_orders} \n"
                f"Активные заказы: {self.activ_orders} \n"
                f"Деньги: {self.money} \n"
                f"Карта: {self.card} \n")

    def get_executor_tgmassage(self):
        return (f"Имя: {self.name}\n"
                f"Возраст: {self.age}\n"
                f"Тег: {self.user_name}\n"
                f"Ставка: {self.stavka}%\n"
                f"Рвнг: {self.rang}\n"
                f"Кол-во: {self.orders}\n"
                f"Переданые заказы: {self.gave_orders}\n"
                f"Не выполненые заказы: {self.faild_orders}\n"
                f"Активные заказы: {self.activ_orders}\n"
                f"Деньги: {self.money}\n")
