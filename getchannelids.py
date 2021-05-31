from telethon import TelegramClient, sync
import yaml

#Code to get the group ids of all the groups you're participating in
#Source: https://stackoverflow.com/a/55391603/14755904

# Remember to use your own values from my.telegram.org and set them in the config.json file!
with open("config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

api_id = cfg['auth']['api_id']
api_hash = cfg['auth']['api_hash']

client = TelegramClient('partlisten', api_id, api_hash)
client.start()
# To get the channel_id,group_id,user_id
for chat in client.get_dialogs():
    print('name:{0} ids:{1} is_user:{2} is_channel{3} is_group:{4}'.format(
        chat.name, chat.id, chat.is_user, chat.is_channel, chat.is_group))
#Asking the user to press enter before closing the window
input("Press enter to exit ;)")