################################################################################
                            #
################################################################################
class Recrutors():
    recrutors=[]
    job = [False, False, False, False,False]
    recrutors_add_orders={}
    size=0
    def read_size(self):
        self.size = 0
        with open("Recrutor/recrutor.txt", 'r') as file:
            for line in file:
                self.size += 1

    def add_obj(self):
        self.recrutors.append(Recrutor())
    def protect_id(self,id):
        self.read_size()
        protect=False
        for i in range(self.size):
            self.add_obj()
        for i in range(self.size):
            self.recrutors[i].read_recrutor(i)
        for i in range(self.size):
            if self.recrutors[i].id==id:
                protect=True
        return protect
    def return_uname_id(self,id):
        for i in range(self.size):
            self.add_obj()
        for i in range(self.size):
            self.recrutors[i].read_recrutor(i)
        f=""
        for i in range(self.size):
            if self.recrutors[i].id==id:
                f=self.recrutors[i].user_name
        return f

################################################################################
                            #
################################################################################
class Recrutor():
    name=""
    user_name=""
    id=0
    stavka = 0
    orders = 0
    gave_orders = 0
    faild_orders = 0
    activ_orders = 0
    money=0
    card=0
    def read_recrutor(self,num):
        with open("Recrutor/recrutor.txt") as read:
            s = 0
            for i in read.readlines():
                if s == num:
                    self.name, self.user_name, self.id, self.stavka,self.orders, self.gave_orders, self.faild_orders, self.activ_orders, self.money, self.card = i.strip().split(
                        " ")
                    self.stavka = int(self.stavka)
                    self.id = int(self.id)
                    self.orders = int(self.orders)
                    self.gave_orders = int(self.gave_orders)
                    self.faild_orders = int(self.faild_orders)
                    self.activ_orders = int(self.activ_orders)
                    self.money = int(self.money)
                    self.card = int(self.card)
                s += 1
    def rewrite(self):
        file=open("Recrutor/recrutor.txt","w")
        file.write(f"")

    def write_recrutor(self):
        file=open("Recrutor/recrutor.txt","a+")
        file.write(f"{self.name} "
                   f"{self.user_name} "
                   f"{self.id} "
                   f"{self.stavka} "
                   f"{self.orders} "
                   f"{self.gave_orders} "
                   f"{self.faild_orders} "
                   f"{self.activ_orders} "
                   f"{self.money} "
                   f"{self.card}\n")
    def add(self,name,user_name,id,stavka,card):
        self.name=str(name)
        self.user_name=str(user_name)
        self.id=int(id)
        self.stavka=int(stavka)
        self.card=int(card)
        self.write_recrutor()