from telebot import types
from Recrutor.recrutor import *
from Executor.executor import *
from Log.log import *
from Orders.orders import *
class Buttons():
    size=0
    log=Log()
    orders=Orders()
    exe=Executors()
    rec=Recrutors()
    arr_buttons={
        "executors":[types.KeyboardButton("Взять заказ"),
                     types.KeyboardButton("Активные заказы"),
                     types.KeyboardButton("Мои заказы"),
                     types.KeyboardButton("Мой профиль"),
                     types.KeyboardButton("Правила"),
                     types.KeyboardButton("Мой баланс")],

        "Взять заказ":types.KeyboardButton("Назад"),
        "Мой профиль":types.KeyboardButton("Назад"),
        "Правила": types.KeyboardButton("Назад"),
        "Мой баланс":types.KeyboardButton("Назад"),

        "recrutors":[types.KeyboardButton("Создать заказ"),
                     types.KeyboardButton("Список заказов"),
                     types.KeyboardButton("Закрыть заказ"),
                     types.KeyboardButton("Правила"),
                     types.KeyboardButton("Мой баланс")],
        "Создать заказ":[types.KeyboardButton("Назад")],
        "admin":[types.KeyboardButton("Список исполнителей"),
                     types.KeyboardButton("Список заказов"),
                     types.KeyboardButton("Список рекрутеров"),
                     types.KeyboardButton("Правила"),
                     types.KeyboardButton("Мой баланс")],
        "Список исполнителей":[types.KeyboardButton("Добавить"),
                               types.KeyboardButton("Удалить"),
                               types.KeyboardButton("Назад")]
    }
################################################################################
                            #BUTTONS REALIZATIONS
################################################################################
    def markup_out(self,id):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if(self.exe.protect_id(id)):
            for s in self.arr_buttons["executors"]:
                markup.add(s)
            self.log.add_log(self.exe.id_test(id,2),"Full menu")
        elif(self.rec.protect_id(id)):
            for s in self.arr_buttons["recrutors"]:
                    markup.add(s)
        elif (id == 864179107):
            for s in self.arr_buttons["admin"]:
                markup.add(s)
        else:
            markup.add(types.KeyboardButton("No bad"))
        return markup
    def markup_out_b(self,id,text):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        money=0
        protect=False
        ## Кнопки исполнителя
        if(self.exe.protect_id(id)):
            if text == "Взять заказ":
                money=[]
                self.orders.orders_read()
                for i in range(self.orders.size_orders):
                    money.append(self.orders.orders[i].return_data())
                markup.add(self.arr_buttons["Мой баланс"])
            elif text == "Активные заказы":
                money = []
                self.orders.orders_read()
                money=self.orders.protect_activ_orders(self.exe.id_test(id, 2))
                markup.add(self.arr_buttons["Мой баланс"])
            elif text == "Мои заказы":
                self.orders.orders_read()
                money=self.orders.protect_user_orders(self.exe.id_test(id, 2))
                markup.add(self.arr_buttons["Мой баланс"])
            elif text == "Мой баланс":
                money=f"Твой баланс: {self.exe.my_money(id)}"
                markup.add(self.arr_buttons["Мой баланс"])
                self.log.add_log(self.exe.id_test(id, 2), "Menu: 'Мой баланс'")
                protect =  False
            elif text=="Мой профиль":
                money=self.exe.my_profile(id)
                self.log.add_log(self.exe.id_test(id, 2), "Menu: 'Мой профиль'")
                markup.add(self.arr_buttons["Мой баланс"])
                protect = False
            elif text=="Правила":
                money=""    ##линк на правила
                self.log.add_log(self.exe.id_test(id, 2), "Menu: 'Правила'")
                markup.add(self.arr_buttons["Мой баланс"])
                protect = False
            elif text== "Назад":
                self.log.add_log(self.exe.id_test(id, 2), "Menu: 'Назад'")
                for s in self.arr_buttons["executors"]:
                    markup.add(s)
                protect = True
            if (protect):
                money = "<-"
        ## Кнопки рекрутера
        elif(self.rec.protect_id(id)):
            if(text=="Создать заказ"):
                for s in self.arr_buttons["Создать заказ"]:
                    markup.add(s)
                money="Введите название заказа: "
                self.rec.job[0]=True
            elif text== "Назад":
                for s in self.arr_buttons["recrutors"]:
                    markup.add(s)
                protect = True
            elif (self.rec.job[0]):
                print(text)
                money = "Введите описание(если большое или файл то ссилкой на документ, файл не крепить): "
                try:
                    tmp = [self.clear_str(text)]
                    self.rec.recrutors_add_orders[id]=tmp
                    self.rec.job[0] = False
                    self.rec.job[1] = True
                    print("cool")
                   # self.log.add_log((self.rec.return_uname_id(id), money))
                except:
                    money = "Не верно введены данные!"
            elif(self.rec.job[1]):
                tmp=list(self.rec.recrutors_add_orders[id])
                money = "Введите дату дедлайна(только число): "
                try:
                    tmp.append(self.clear_str(str(text)))
                    self.rec.recrutors_add_orders[id]=list(tmp)
                    self.rec.job[1] = False
                    self.rec.job[2] = True
                    #self.log.add_log((self.rec.return_uname_id(id), money))
                except:
                    money="Не верно введены данные!"
            elif (self.rec.job[2]):
                money = "Введите время дедлайна(только число): "
                tmp = list(self.rec.recrutors_add_orders[id])
                try:
                    tmp.append(int(text))
                    self.rec.recrutors_add_orders[id] = list(tmp)
                    self.rec.job[2] = False
                    self.rec.job[3] = True
                except:
                    money="Не верно введены данные!"
            elif(self.rec.job[3]):
                money = "Введите сумма дедлайна(только число): "
                tmp = list(self.rec.recrutors_add_orders[id])
                try:
                    tmp.append(int(text))
                    print(tmp)
                    self.rec.recrutors_add_orders[id] = list(tmp)
                    self.rec.job[3] = False
                    self.rec.job[4] = True
                    #self.log.add_log((self.rec.return_uname_id(id), money))
                except:
                    money="Не верно введены данные!"
            elif (self.rec.job[4]):
                tmp = list(self.rec.recrutors_add_orders[id])
                tmp.append(int(text))
                self.rec.recrutors_add_orders[id] = list(tmp)
                self.rec.job[4] = False
                tmp.append(int(text))
                self.rec.job=[False,False,False,False,False]
                try:
                    #self.log.add_log((self.rec.return_uname_id(id), money))
                    tmp[0]=str(self.clear_str(tmp[0]))
                    tmp[1]=str(self.clear_str(tmp[1]))
                    tmp[2]=int(tmp[2])
                    tmp[4]=int(tmp[4])
                    tmp[5]=int(tmp[5])
                    self.orders.add_new_orders(tmp[0],tmp[1],True,self.log.return_data(),tmp[2],str(self.rec.return_uname_id(id)),tmp[4],tmp[5])
                    money = "Спасибо!"
                except:
                    money="Ты не правильно заполнил данные!"
            if (protect):
                money = "<-"
        ## Кнопки админа
        elif(id==864179107):
            protect=False
            if text == "Отчёт":
                money=self.exe.user_name_test("Nikola", 17)
                markup.add(self.arr_buttons["Мой баланс"])
            elif text=="Список исполнителей":
                money=""
                iterator=0
                for s in self.exe.list_users():
                    iterator += 1
                    money+=str(f"#{iterator} {s}\n")
                    markup.add(s)
                for s in self.arr_buttons["Список исполнителей"]:
                    markup.add(s)
            elif text== "Назад":
                self.log.add_log(self.exe.id_test(id, 2), "Menu: 'Назад'")
                for s in self.arr_buttons["admin"]:
                    markup.add(s)
                protect = True
            if (protect):
                money = "<-"
        #Кнопка для посторонних людей
        else:
            markup.add(types.KeyboardButton("No bad"))
        return [money,markup]

################################################################################
                            #BUTTONS ADD FUNCTIONS
################################################################################
    #def add_orders(self,id,text):

    def protect_ordres(self,num):   #проверка номера заказа для определения ее нажатия и того номера что в базе
        self.orders.orders_read()
        for i in range(self.orders.size_orders):
            if int(self.orders.orders[i].num)==int(num):
                return True
        return False
    def orders_add_executors(self,id,num):
        self.orders.add_user_name(self.exe.id_test(id,2),num)
        self.exe.orders_add_executors(self.exe.id_test(id, 2), self.orders.add_money_executors(self.exe.id_test(id,2)))
    def clear_str(self,text):
        str_=""
        for i in list(text):
            if i != " ":
                str_+=i
            else:
                str_+="_"
        return str(str_)