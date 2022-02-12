import asyncio
from turtle import st
import schedule
import time
import discord
import os
import json
import requests
from discord.ext import commands
import numpy as np


Token = "" #put your discord bot token here.
dayTime = 86400000
client = discord.Client()


@client.event
async def on_ready():
    print("M6ّo3 is online!")

    jsonFile = open("../Disbot/hadeeth.json", 'r', encoding="utf8")
    jsonDate = jsonFile.read()

    # parse
    obj = json.loads(jsonDate)
    counter = 0
    for itm in obj["hadeeth"]:

        print(obj["hadeeth"][itm])

        counter = counter+1
        # time.sleep(dayTime)

        channel = client.get_channel(819478355673481266)  # mybot channel
        await channel.send(obj["hadeeth"][itm])

        print(f"hadeeth {counter} sent successfully!")

        time.sleep(3)


client.run(Token)
