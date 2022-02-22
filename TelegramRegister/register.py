from telethon.sync import TelegramClient
from telethon import functions, types
from pyrogram import Client
from tprint import *
import time

class TelegramRegister:

    def __init__(self):
        pass


    def Register(self, target, api_id, api_hash):
        client_t = TelegramClient('Checker', api_id, api_hash)
        client_t.start()
        client = Client("spad_sec", api_id, api_hash)
        client.start()

        
        available = False

        while available == False:
            result = client_t(functions.account.CheckUsernameRequest(username=target))
            time.sleep(2)
            if result == True:
                try:
                    channel = client.create_channel(f"@{target}", "This channel was created by")#https://github.com/execution/Telegram-Tools")
                    client.update_chat_username(channel.id, target)
                    tprint(tprint.GREEN, f"Claimed @{target}", 14)
                except Exception as err:
                    print(err)
            else:
                quit()


        
