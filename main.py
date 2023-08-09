import discord.ext
from dotenv import load_dotenv, find_dotenv
import discord, os
# Carrega o arquivo .env
load_dotenv(find_dotenv())

class MyClient(discord.Client):
  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    if message.author == client.user:
      return
        
    if message.content.lower() == "f":
      await message.channel.send("F")

  async def on_member_join(member):
    channel = client.get_channel("1033440648843501570")
    await channel.send(f"{member} has joined the server")

  async def on_member_remove(member):
    channel = client.get_channel("1033440648843501570")
    await channel.send(f"{member} has left the server")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.messages = True

client = MyClient(intents=intents)


if __name__ == '__main__':
  client.run(os.environ.get('TOKEN'))


# url para adicionar o bot em servidores.
# https://discord.com/oauth2/authorize?client_id=1138160805402128514&scope=bot&permissions=1099511627775