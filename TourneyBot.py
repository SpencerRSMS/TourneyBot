import discord
import logging
#import sqlite3
#from bs4 import BeautifulSoup
from lxml import etree
#from io import StringIO
#from cryptography.fernet import Fernet

#testing logging
logging.basicConfig(filename='TourneyBot.log', encoding='utf-8', level=logging.DEBUG)

#grab token from connection, needs try/except
def get_token(name):
    path = f'/TourneyBot/connection/{name}/token/text()'
    try:
        tree = etree.parse("config.xml")
        return tree.xpath(path)[0]
    except Exception:
        print('Unknown Error: get_token()')
        return -1

def main():
    #instance of client (connect to Discord)
    client = discord.Client()

    #console notification upon successful login
    @client.event
    async def on_ready():
        msg = 'We have logged in as {0.user}'.format(client)
        logging.info(msg)
        print(msg)

    #wait for commands, do stuff
    @client.event
    async def on_message(message):
        #if input is from myself (this bot), do nothing
        if message.author == client.user:
            return

        #if input is $hello, say hello (example code)
        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

    #bot login
    client.run(get_token('discord'))

#run
if __name__ == '__main__':
    main()