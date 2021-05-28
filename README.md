# Telegram link opener
Very work in progress python app to automatically open telegram links in web browser

# Disclaimer
Use at own risk!

# Installation and Usage
1. Download Python 3.8.x . Before installing, make sure to check “Add Python to PATH”.
2. Once installed, open CMD and type:
```
pip install Telethon
pip install asyncio
pip install pyyaml

```
3. Clone the repo using your favourite git application (I'm partial to Github Desktop for Windows users)
6. Copy config_example.yaml and rename it to config.yml
6. Replace the placeholders with the values for the api_id, api_hash and the telegram channels and save
7. cd to the folder from command line and run
```
python listen.py
```
8. put your phone number associated with your telegram account then confirm with the code that you'll receive on your phone.
9. Done.

# How to get the Telegram api_id and api_hash
https://docs.telethon.dev/en/latest/basic/signing-in.html

# How to get the channel number
Got to https://web.telegram.org and sign in
Open the channel you want to monitor
In the link identify the string that starts with c and ends with _
Example:
```
https://web.telegram.org/#/im?p=c1158879711_3707114065192498484
```
In this case it's c1158879711
Remove the c and add -100 to it, like this:
```
-1001158879711
```

This is it. You can add it to the config.yml now

# Requirements
asyncio, Telethon, pyyaml

# Operating Systems
This was designed for and only tested on windows.

# Credits
This script is a combination of the work of clearyy, Vincent1705, Smidelis and my own work
Based on: https://github.com/Smidelis/discord-link-opener
