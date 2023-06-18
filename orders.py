################################################################################
                            #
################################################################################
class Orders():
    orders=[]
    size_orders=0
    def size_orders_read(self):     ##Читаем количество заказов в файле
        self.size_orders = 0
        with open("Orders/order.txt", 'r') as file:

        #with open("order.txt", 'r') as file:
            for line in file:
                self.size_orders += 1
    def add_orders(self):       ##Создание массива обьектов
        self.orders.append(Order())
    def orders_read(self):      ##Функция вычитки всех заказов по массиву обьектов
        self.orders=[]
        self.size_orders_read()
        for i in range(self.size_orders):
            self.add_orders()
        for i in range(self.size_orders):
            self.orders[i].read(i)
    def add_money_executors(self,text):
        self.orders_read()
        temp = []
        for i in range(self.size_orders):
            if self.orders[i].executor_uname == text:
                return self.orders[i].sum
    def protect_activ_orders(self,text):
        self.orders_read()
        temp = []
        for i in range(self.size_orders):
            if self.orders[i].executor_uname == text:
                if self.orders[i].activ == True:
                    temp.append(self.orders[i].return_data())
        return list(temp)
    def protect_user_orders(self,text):
        self.orders_read()
        temp=[]
        for i in range(self.size_orders):
            if self.orders[i].executor_uname==text:
                temp.append(self.orders[i].return_data())
        return list(temp)
    def add_user_name(self,text,num):   ##Добавление тега исполнителя
        self.orders_read()
        self.orders[0].clear_file()
        for i in range(self.size_orders):
            if self.orders[i].num==num:
                self.orders[i].executor_uname=text
                self.orders[i].activ=False
            self.orders[i].write_orders()
    def add_new_orders(self,title,description,activ,orders_data,dedline,recrutor,time,sum): #title -строка/description - строка/activ- бул/ордерс дата-инт/ддедлайн -инт/recrutor -строка/time -строка/сума-инт/////////
        self.orders_read()
        print(self.size_orders,title,description,activ,orders_data,dedline,recrutor,time,sum)
        print(self.orders)
        self.add_orders()
        self.orders[self.size_orders].create_order(int(self.size_orders+1),title,description,activ,orders_data,dedline,recrutor,time,sum)
################################################################################
                            #
################################################################################
class Order():
    num=0
    title=" "
    description=""
    activ=False
    orders_data=0
    dedline=0
    time=""
    recrutor=""
    sum=0
    executor_uname=" "
    file_pn="Orders/order.txt"  #file path and name
    #file_pn="order.txt"  #file path and name
    #file_pn="order.txt"  #file path and name
    def create_order(self,num,title,description,activ,orders_data,dedline,recrutor,time,sum): #номер заказа будет исходить из строк в файле
        self.num,self.title,self.description,self.activ,self.orders_data, self.dedline,self.recrutor,self.time,self.sum=int(num), str(title), str(description), bool(activ), int(orders_data), int(dedline),str(recrutor),str(time),int(sum)
        self.write_orders()
    def clear_file(self):
        file = open(self.file_pn, "w")
        file.write("")
    def write_orders(self):
        file=open(self.file_pn,"a+")
        file.write(f"{self.num} {self.title} {self.description} {self.activ} {self.orders_data} {self.dedline} {self.recrutor} {self.time} {self.sum} {self.executor_uname}\n")
    def read(self,num):
        with open(self.file_pn) as read:
            s = 0
            for i in read.readlines():
                if s == num:
                    try:
                        self.num,self.title,self.description,self.activ,self.orders_data,self.dedline,self.recrutor,self.time,self.sum,self.executor_uname = i.strip().split(" ")
                    except:
                        self.num, self.title, self.description, self.activ,self.orders_data, self.dedline,self.recrutor,self.time, self.sum= i.strip().split(" ")
                        self.executor_uname=""
                    self.activ=bool(self.activ)
                    self.orders_data=int(self.orders_data)
                    self.dedline=int(self.dedline)
                    self.sum=int(self.sum)
                s += 1
    def return_data(self):
        return f"#{self.num}\n" \
               f"Название: {self.title}\n" \
               f"Описание: {self.description}\n" \
               f"Состояние активности: {self.activ}\n" \
               f"Дата заказа: {self.orders_data}\n" \
               f"Дата дедлайна: {self.dedline}\n" \
               f"Время дедлайна: {self.time}\n" \
               f"Заказ оформлял: {self.recrutor}\n" \
               f"Сумма: {self.sum}\n" \
               f"Исполнитель: {self.executor_uname}"
# f=Order()
#a=Orders()
# # title -строка/description - строка/activ- бул/ордерс дата-инт/ддедлайн -инт/recrutor -строка/time -строка/сума-инт/
#a.add_new_orders("----","hxx",True,90,97,"@jnngjn","1712",293)
# #f.create_order(9,"----","hxx",True,90,97,"@jnngjn","1712",293)