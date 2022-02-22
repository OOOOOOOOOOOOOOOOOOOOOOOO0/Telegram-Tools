import os, tgcrypto
from telethon.sync import TelegramClient
from telethon import functions, types
from pyrogram import Client
from tprint import *

# swapper.py
# Author: execution
# Date: 21/02/2022

class TelegramSwapper:

    def __init__(self):
        self.tries = 0
        self.available = False
    
    def Clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def Swapper(self):
        while True:
            result = self.client(functions.account.CheckUsernameRequest(username=self._target))
            self.tries += 1

            if result == True:
                self.available = True
            else:
                pass
            if self.available == True:
                self.client(functions.channels.UpdateUsernameRequest(channel=self._current, username=self._target))
                tprint(tprint.GREEN, f"Claimed @{self._target}", 14)
    
    def Swap(self, api_id, api_hash, current, target):
        self._current = current
        self._target = target
        self.client = TelegramClient('anon', api_id, api_hash)
        self.client.start()
        self.Clear()
        self.Swapper()
