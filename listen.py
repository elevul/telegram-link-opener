from telethon import TelegramClient, events, sync
import re
from playsound import playsound
import webbrowser
import asyncio
from datetime import datetime
import urllib.parse as urlparse
from urllib.parse import parse_qs
import yaml
import os
import numpy as np
from urllib.parse import unquote
from bs4 import BeautifulSoup
import requests

# Set current working directory to the script's root
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Remember to use your own values from my.telegram.org and set them in the config.json file!
with open("config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

api_id = cfg['auth']['api_id']
api_hash = cfg['auth']['api_hash']
client = TelegramClient('partlisten', api_id, api_hash)
myChannelIDList = cfg['channels']
GroupName = 'PlaceHolder'

# Decide whether you want to hear a bell sound when a link is opened (True/False)
playBellSound = cfg['various']['playBellSound']

def print_time(*content):
    """
    Can be used as a normal print function but includes the current date and time
    enclosed in brackets in front of the printed content.
    :param content: The content you would normally put in a print() function
    """
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"[{date_time}] - [INFO] ", *content)

# Check for keywords and blacklisted words in message urls and open browser if conditions are met
async def check_urls(url, channel_name):
    # Check if url contains partalert.net. If true, direct amazon link will be built.
    # Enter path to your browser
    webbrowser.open_new_tab(url)
    print_time(f'Link opened from #{channel_name}: {url}')
    if playBellSound:
        playsound('./bell.wav')

async def get_last_msg(channelid):
    msg = await client.get_channel(channelid).history(limit=1).flatten()
    return msg[0]

@client.on(events.NewMessage(chats = myChannelIDList))
async def my_event_handler(event):
    print(event.peer_id)
    peerid = str(event.peer_id)
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', event.text if event.text else "")
    unsafeurls = re.findall('tg:\/\/unsafe_url\?url=((?:https?%3A%2F%2F)?(?:www\.)?(?:.+?\..+?)%2F.+)', event.text if event.text else "")
    ldlcurls = re.findall('tg:\/\/unsafe_url?.*ldlc.com.*(PB\d*.html)', event.text if event.text else "")
    toopen = []
    #Normal URLs
    if isinstance(urls, str):
        if 'ldlc.com' not in urls:
            toopen.append(urls)
    else:
        for url in urls:
            if 'ldlc.com' not in url:
                toopen.append(url)
    #Unsafeurls
    if isinstance(unsafeurls, str):
        if 'ldlc.com' not in unsafeurls:
            cleanurl = unquote(unsafeurls)
            toopen.append(cleanurl)
    else:
        for unsafeurl in unsafeurls:
            if 'ldlc.com' not in unsafeurl:
                cleanurl = unquote(unsafeurl)
                toopen.append(cleanurl)
    #ldlcurls:
    if isinstance(ldlcurls, str):
        finalurl = 'https://www.ldlc.com/fiche/' + ldlcurls
        toopen.append(finalurl)
    else:
        for ldlcurl in ldlcurls:
            finalurl = 'https://www.ldlc.com/fiche/' + ldlcurl
            toopen.append(finalurl)
    #Removing Duplicates
    noduplicates = np.unique(toopen).tolist()
    #final opening
    if isinstance(noduplicates, str):
        asyncio.ensure_future(check_urls(noduplicates, peerid))
    else:
        for link in noduplicates:
            asyncio.ensure_future(check_urls(link, peerid))

client.start()
client.run_until_disconnected()