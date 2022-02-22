<h1 align="center">
	<img src="https://i.postimg.cc/K837xr93/dasdadsada.jpg" width="150px"><br>
    Telegram Tools - Swap your telegram username with these tools.
</h1>
<p align="center">
    These tools allows you to swap your username from channel to channel or profile to channel.<br> Disclaimer: If the event of you losing your username occurs when using these tools, I am not held responsible. By cloning/downloading this repository, you agree to this</br>
</p>

<h1></h1>

**Install**

```
git clone https://github.com/execution/Telegram-Tools
cd Telegram-Tools
```

<h1></h1>

**Swapper Example**

```python
from TelegramSwapper import TelegramSwapper

api_id = input("Enter API_ID: ")
api_hash = input("Enter API_HASH: ")
current = input("Current channel name: ")
target = input("Target channel name: ")

t = TelegramSwapper()
t.Swap(api_id, api_hash, current, target)
```
**Channel Register Example**
```python
from TelegramRegister import TelegramRegister

api_id = input("API_ID: ")
api_hash = input("API_HASH: ")
ch = input("Target: ")

t = TelegramRegister()
t.Register(ch, api_id, api_hash)
```
