# this is website blocker in specfic time period 

import datetime
import time



end_time=datetime.datetime(2025,04,18)
site_block=["www.wscubetech.com","www.facebook.com"]
host_path=""
redirect=""


while True:
    if datetime.datetime.now()<end_time:
        print("Start Blocking ")
        with open(host_path,"r+") as host_file:
            content=host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write(redirect +" "+website+"\n")
                else:
                    pass

    else:
         with open(host_path,"r+") as host_file:
             content = host_file.readlines()
             host_file.seek(0)
             for lines in content :
                 if not any (website in lines  for website in site_block):
                     host_file.write(lines)



             host_file.truncate()        
         time.sleep(3)














                                       # Jay Kumar Singh
