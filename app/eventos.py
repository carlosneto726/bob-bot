import discord, discord.ext

class Eventos:
  def __init__(self, bot) -> None:
    self.bot = bot

    # Função que procura o primeiro canal de texto do servidor 
    async def find_channel(guild):
        for channel in guild.text_channels:
            if not channel.permissions_for(guild.me).send_messages:
                continue
            return channel

    @bot.event
    async def on_ready():
        print(f"{bot.user} Está onmlione")

    @bot.event
    async def on_member_join(member):
        channel = await find_channel(member.guild)
        await channel.send(file=discord.File('images/bob_pirata.jpg'), content=f"Que bom te ver colega! {member.mention} Seja bem vindo.")

    @bot.event
    async def on_member_remove(member):
        channel = await find_channel(member.guild)
        await channel.send(f"Até um outro dia amigo! {member.mention} espero que a gente se encontre por aí.")

    @bot.event
    async def on_message(message):
        if message.content.upper() == "F":
            await message.channel.send("F")
        else:
            await bot.process_commands(message)
