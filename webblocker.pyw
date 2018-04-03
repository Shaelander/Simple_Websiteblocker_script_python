#look for host file "C:\Windows\System32\drivers\etc\hosts"
#insted of using \\ i used r here which passes path as row
#ctrl + c used to exit while loop
import time
from datetime import datetime as dt
#temp_host = r"C:\Users\Naresh mehta\Documents\Website Blocker\hosts"
host_path =r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websitelist = ["www.facebook.com","facebook.com","www.instagram.com","www.fb.com"]

while True:
    #means study hours are 4 pm to 11 pm
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("Study hours")
        #r+ is used to read and write a file
        with open(host_path,"r+") as file:
            content = file.read()
            for website in websitelist:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:
        with open(host_path,"r+")as file:
            content = file.readlines()
            #used to put cursor on the top
            file.seek(0)
            for lines in content:
                if not any(website in lines for website in websitelist):
                    file.write(lines)
                #truncate used for deleting
                file.truncate()

        print("Party time")


    time.sleep(5)
