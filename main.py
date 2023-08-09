import discord.ext
from dotenv import load_dotenv, find_dotenv
import discord, os, eventos, comandos

# Carrega o arquivo .env
load_dotenv(find_dotenv())

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)


if __name__ == '__main__':
  client.run(os.environ.get('TOKEN'))


# url para adicionar o bot em servidores.
# https://discord.com/oauth2/authorize?client_id=1138160805402128514&scope=bot&permissions=1099511627775