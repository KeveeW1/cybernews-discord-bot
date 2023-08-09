import discord
from cybernews.cybernews import CyberNews
from GoogleNews import GoogleNews
import pandas as pd

import os
#-----------------------------------------------------------------------------------------------------------

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
news = CyberNews()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    activity = discord.Game(name="the news", type=1)
    await client.change_presence(status=discord.Status.online, activity=activity)

key1=r'\hi'
key2=r'\news'
key3=r'\hackathons'
key4=r'\tips'
key5=r'\pass'
@client.event

async def on_message(message):
  #\hi
  if message.content==key1:
      await message.channel.send("hi, i'm cybernews bot!")

  #\news
  if message.content==key2:
      gNews = GoogleNews(period='1d')
      gNews.set_lang('en')
      gNews.set_encode('utf-8')
      gNews.search("cybersecurity")
    
      result = gNews.result()
      data = pd.DataFrame.from_dict(result)
      data = data.drop(columns=["img"])
      data.head()
    
      for res in result:
        await message.channel.send("-------------------------------------------------------------------------------------------------------------------\nTitle: ", res["title"])
        await message.channel.send("Link: ", res["link"] + "\n-------------------------------------------------------------------------------------------------------------------\n")

  #\hackathons
  if message.content==key3:
    await message.channel.send("pending...")

  #\tips
  if message.content==key4: 
    await message.channel.send("-------------------------------------------------------------------------------------------------------------------\n**__TIPS TO STAY SAFE ON THE INTERNET:__** \n" +  
                               "1. NEVER GIVE THESE OUT: \n\t\t- address \n\t- phone number \n\t- birthday \n\t- internal family private info" +
                               "\n2. never open files from unknown senders \n3. create STRONG passwords. need help? *type \pass* \n4. update all computer software \n5. don't trust public wifi. make sure secure.\n-------------------------------------------------------------------------------------------------------------------")

  #\pass
  if message.content==key5:
    await message.channel.send("-------------------------------------------------------------------------------------------------------------------\n**__HOW TO CREATE A STRONG PASSWORD__**\n"+ "\t- at least 12 characters long \n- a combination of uppercase letters, lowercase letters, numbers, and symbols \n- not a word that can be found in dictionary or the name of a person, character, product, or organization\n-------------------------------------------------------------------------------------------------------------------")
    
  if message.author == client.user:
    return


client.run(os.getenv("TOKEN")) #<-- TOKEN should be your bot's API key! don't share your API key to the public