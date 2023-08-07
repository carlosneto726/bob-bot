from discord.ext import commands, tasks
from dotenv import load_dotenv, find_dotenv
import discord, os, asyncio, requests
# Carrega o arquivo .env
load_dotenv(find_dotenv())

intents = discord.Intents.default()
intents.members = True

# Define a atividade do bot
activity = discord.Activity(name='-comandos', type=discord.ActivityType.watching)
# Define o prefixo dos comandos
client = commands.Bot(command_prefix='-', intents = intents, activity=activity)

# ==================================== Eventos ====================================

# Status do Bot
@client.event
async def on_ready():
    print("Logamos com sucesso como {0.user}".format(client))    


if __name__ == '__main__':
  client.run(os.environ.get('TOKEN'))
