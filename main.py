import discord, os, discord.ext
from dotenv import load_dotenv, find_dotenv
from discord.ext import commands
from eventos import Eventos
from comandos import Comandos

class Bot:
    def __init__(self, intents, activity) -> None:
        self.intents = intents
        self.activity = activity
        self.bot = commands.Bot(intents=self.intents, activity=self.activity)

    def getBot(self):
        return self.bot

# Carrega o arquivo .env
load_dotenv(find_dotenv())
# Definindo todos os intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.messages = True
# Definindo o status do bot
activity = discord.Activity(name='/comandos', type=discord.ActivityType.watching)
# Carregando o bot
bot = Bot(intents, activity).getBot()
# Carregando os eventos do bot
Eventos(bot)
# Carregando os comandos do bot
Comandos(bot)
# Caso o arquivo que seja executado for o main
if __name__ == '__main__':
  # Rodando o bot com o Token
  bot.run(os.environ.get('TOKEN'))

# URL para adicionar o bot em servidores.
# https://discord.com/oauth2/authorize?client_id=1138160805402128514&scope=bot&permissions=1099511627775

# Documentação 
# https://docs.pycord.dev/en/stable/api/events.html