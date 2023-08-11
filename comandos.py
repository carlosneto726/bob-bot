import discord
from discord.ext import commands

class Comandos:
    def __init__(self, bot) -> None:
        self.bot = bot

        # Listar comandos
        @bot.slash_command(name="comandos", description="lista os comandos")
        async def comandos(ctx):
            embed = discord.Embed(
                title = '**COMANDOS**',
                description = 'Meus comandos.',
            )
            embed.set_author(name='Bob o Bot', icon_url='https://static.wikia.nocookie.net/hearthstone_gamepedia/images/7/71/Bartender_Bob_full.jpg/revision/latest/scale-to-width-down/1200?cb=20190604193931')
            embed.set_thumbnail(url='https://media.tenor.com/iWRE1gsz7roAAAAi/hearthstone-funny.gif')
            embed.add_field(name='$comandos', value='Listagem de todos os meus comandos', inline=False)
            embed.set_footer(text='Rocambole!')
            await ctx.respond(embed=embed)

        @bot.slash_command(name = "oi", description = "diz oi para você")
        async def oi(interaction: discord.Interaction):
            await interaction.response.send_message("Que bom te ver colega!")
