import discord, requests, os
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

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

        # Comando que retorna informações sobre uma carta
        @bot.slash_command(name="carta", description="retorna informações de uma carta")
        async def carta(ctx, pesquisa, linguagem="pt_br", modo_jogo="battlegrounds"):
            token = os.environ.get('BLIZZARD_API_TOKEN')
            url = f"https://us.api.blizzard.com/hearthstone/cards?locale={linguagem}&textFilter={pesquisa}&gameMode={modo_jogo}&access_token={token}"
            response = requests.get(url)
            # print(url)

            for card in response.json()["cards"]:
                embed=discord.Embed(
                    title=card["name"], 
                    description=card["text"].replace("<b>", "**").replace("</b>", "**").replace("<i>", "*").replace("</i>", "*")
                )
                embed.set_thumbnail(url=card["image"])
                try:
                    embed.add_field(name="Tipo", value=getRaridade(getTipo(card["minionTypeId"])), inline=False)
                except:
                    pass
                embed.add_field(name="Raridade", value=getRaridade(card["rarityId"]), inline=False)
                embed.add_field(name="Vida", value=card["health"], inline=False)
                embed.add_field(name="Ataque", value=card["attack"], inline=False)
                embed.add_field(name="Gráu da taverna", value=card["battlegrounds"]["tier"], inline=False)
                embed.set_footer(text='Rocambole!')
                await ctx.send(embed=embed)

        def getRaridade(id_raridade):
            token = os.environ.get("BLIZZARD_API_TOKEN")
            url = f"https://us.api.blizzard.com/hearthstone/metadata/rarities?access_token={token}&locale=pt_br"
            response = requests.get(url)

            for raridade in response.json():
                if raridade["id"] == id_raridade:
                    return raridade["name"]
            
            return "Nenhuma"
        
        def getTipo(id_tipo):
            token = os.environ.get("BLIZZARD_API_TOKEN")
            url = f"https://us.api.blizzard.com/hearthstone/metadata/minionTypes?access_token={token}&locale=pt_br"
            response = requests.get(url)

            for tipo in response.json():
                if tipo["id"] == id_tipo:
                    return tipo["name"]
                
            return "Nenhum"
