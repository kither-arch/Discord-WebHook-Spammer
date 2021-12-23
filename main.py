import time
import requests
import pyfiglet
banner = pyfiglet.figlet_format("KINGMAN")
print(banner)
msg = input(" I LOVE YOU DEV: ")
webhook = input("https://discord.com/api/webhooks/923568259205320704/r3GOWrh6ims_dYXbp5kYbsJy1roaWFFxOlTN-LczIo19wEA54ZEfoSgiTGK-i7xPG3f0 : ")
def spam(msg, webhook):
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent MSG {msg}")
        except:
            print("Bad Webhook :" + webhook)
            time.sleep(5)
            exit()
kingman_top = 1
while kingman_top == 1:
    spam(msg, webhook)
