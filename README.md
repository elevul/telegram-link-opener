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
pip install playsound

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
After completing the configuration of config.yml run the getchannelids.py script (python getchannelids.py)
The groupid will have this format:

```
-1001158879711
```

This is it. You can add it to the config.yml now.
You can add more than one to the config.yml, just need to make sure the indent is correct. Example:
```
channels:
  - -1001466115668
  - -1001158879711
```

# Requirements
asyncio, Telethon, pyyaml

# Operating Systems
This was designed for and only tested on windows.

# Credits
This script is a combination of the work of clearyy, Vincent1705, Smidelis and my own work
Based on: https://github.com/Smidelis/discord-link-opener
