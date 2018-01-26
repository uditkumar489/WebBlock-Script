import time
from datetime import datetime as dt

hosts_path_windows = "C:\Windows\System32\drivers\etc\hosts" # This is for WINDOWS-users only || check READme.md for mac and unix

redirect = "127.0.0.1"

websites_to_block = ["www.pointless.com","www.pointlesssites.com/"]  # Replace with your own

count = 0

while True:
    
    with open(hosts_path_windows,'r+') as file:
        
        content = file.read()
        
        for website in websites_to_block:
            
            if website in content:
                pass
            else:
                file.write(redirect + " " + website + "\n")
                
    time.sleep(5)