from discord.ext import commands, tasks
from dotenv import load_dotenv, find_dotenv
import discord, os, asyncio, requests
# Carrega o arquivo .env
load_dotenv(find_dotenv())

intents = discord.Intents.default()
intents.members = True

# Define a atividade do bot
activity = discord.Activity(name='/comandos', type=discord.ActivityType.watching)
# Define o prefixo dos comandos
client = commands.Bot(command_prefix='/', intents = intents, activity=activity)

# Status do Bot
@client.event
async def on_ready():
    print("Logamos com sucesso como {0.user}".format(client))

# Lendos as mensagens
@client.event
async def on_message(message):
  if message.content.upper() == "F":
    await message.channel.send("F :sob:")

  elif message.content.upper() == "PING":
    await message.channel.send("pong?", reference=message)

  else:
    await client.process_commands(message)
    
if __name__ == '__main__':
  client.run(os.environ.get('TOKEN'))


# url para adicionar o bot em servidores.
# https://discord.com/oauth2/authorize?client_id=1138160805402128514&scope=bot&permissions=1099511627775