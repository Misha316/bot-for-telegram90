from time import asctime as time_
################################################################################
                            #Loging process bot
################################################################################
class Log():
    file="Log/log_file.txt"
    g=0
    def add_log(self,user_name,text):
        file=open(self.file,"a+")
        file.write(f"{time_()}\t{user_name}\t{text}\n")
    def return_data(self):
       tmp=list(str(time_()).strip().split(" "))
       return int(tmp[2])