from TelegramSwapper import TelegramSwapper

api_id = input("Enter API_ID: ")
api_hash = input("Enter API_HASH: ")
current = input("Current channel name: ")
target = input("Target channel name: ")

t = TelegramSwapper()
t.Swap(api_id, api_hash, current, target)
