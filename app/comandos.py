import discord, requests, json, urllib.parse

class Comandos:
    def __init__(self, bot, blizzard_token) -> None:
        self.bot = bot
        self.blizzard_token = blizzard_token
        self.metadata = json.load(open('../data/metadata.json'))

        # Listar comandos
        @bot.slash_command(name="comandos", description="lista os comandos")
        async def comandos(ctx):
            embed = discord.Embed(
                title = '**COMANDOS**',
                description = 'Meus comandos.',
            )
            embed.set_author(name='Bob o Bot', icon_url='https://static.wikia.nocookie.net/hearthstone_gamepedia/images/7/71/Bartender_Bob_full.jpg/revision/latest/scale-to-width-down/1200?cb=20190604193931')
            embed.set_thumbnail(url='https://media.tenor.com/iWRE1gsz7roAAAAi/hearthstone-funny.gif')
            embed.add_field(name='/comandos', value='Listagem de todos os meus comandos', inline=False)
            embed.add_field(name='/card <pesquisa>', value='Retorna a(s) carta(s) que se ecaixam na pesquisa. Exemplo: /card ', inline=False)
            embed.set_footer(text='Rocambole!')
            await ctx.respond(embed=embed)

        # Retorna o ping do bot
        @bot.slash_command(name="ping", description="Verifique a latencia do Bob")
        async def ping(interaction: discord.Interaction):
            await interaction.response.send_message(f"``Pong! {round(bot.latency * 1000)}ms``") # Envia uma mensagem mostrando a latencia do bot

        # Comando que retorna informações sobre uma carta
        @bot.slash_command(name="battlegroundscards", description="retorna informações de uma carta")
        async def battlegroundscards(ctx, pesquisa, linguagem="pt_br"):
            cards = getBattlegroundsCards(pesquisa) # Pegando da API todas as cartas que se encaixam na pesquisa
            if(cards): # Caso a função getBattlegroundsCards() retorne alguma carta
                for card in cards: # Percorrendo todas as cartas
                    if(card["battlegrounds"]["hero"]): # Caso o tipo da carta seja Herói
                        await ctx.respond(embed=getHeroEmbedMessage(card)) # Envia no canal de texto a mensagem personalizada para Heróis
                    elif(card["battlegrounds"]["quest"] or card["battlegrounds"]["reward"]): # Caso o tipo da carta seja uma Missão ou Recopensa
                        # Definindo o tipo de carta
                        cardType = None
                        if(card["battlegrounds"]["quest"]):
                            cardType = "Missão"
                        elif(card["battlegrounds"]["reward"]):
                            cardType = "Recompensa"
                        await ctx.respond(embed=getQuestOrRewardEmbedMessage(card, cardType)) # Envia no canal de texto a mensagem personalizada para Missões ou Recopensas
                    else:
                        await ctx.respond(embed=getMinionEmbedMessage(card)) # Envia no canal de texto a mensagem personalizada para Lacaios
            else:
                await ctx.respond("Sinto muito colega, não achei nenhuma carta.") # Envia uma mensagem caso a API não tenha achado nenhuma carta

        # Função que recebe o id de raridade e retorna uma String do nome da raridade
        def getRarity(id_rarity):
            for rarity in self.metadata["rarities"]: # Para cada raridade no arquivo metadata.json
                if rarity["id"] == id_rarity: # Caso o id da raridade seja o mesmo do parametro da função
                    return rarity["name"] # Retorna o nome da raridade
            return "Nenhuma"
        
        # Função que recebe o id do tipo e retorna uma String do nome do tipo do lacaio
        def getMinionType(id_minionType):
            for minionType in self.metadata["minionTypes"]: # Para cada tipo de Lacaio no arquivo metadata.json
                if minionType["id"] == id_minionType: # Caso o id do tipo de minion seja o mesmo do parametro da função
                    return minionType["name"] # Retorna o nome do tipo do minion
            return "Nenhum"
        
        # Função que retorna os cards especificados pela a pesquisa
        def getBattlegroundsCards(textFilter, locale="pt_br", gameMode="battlegrounds"):
            tokenURI = f"access_token={self.blizzard_token}" # URI formatado para o token da URL
            localeURI = f"locale={urllib.parse.quote(locale)}" # URI que determina o idioma (Padrão: pt_br)
            textFilterURI = f"textFilter={urllib.parse.quote(textFilter)}" # URI que filtra a response
            gameModeURI = f"gameMode={urllib.parse.quote(gameMode)}" # URI que determina o modo de jogo (Padrão: battlegrounds)
            url = f"https://us.api.blizzard.com/hearthstone/cards?{localeURI}&{textFilterURI}&{gameModeURI}&{tokenURI}" # URL formatada para o reponse com todos o parametros
            response = requests.get(url) # Efetuando o GET da URL
            if(response.status_code == 200): # Caso o response retorne 200 (reponse feito com sucesso)
                return response.json()["cards"] # Retorna os cards do response
            else:
                return False # Caso o response seja diferente de 200 (response falhou)
            
        # Função que retorna uma mensagem personalizada para Heróis
        def getHeroEmbedMessage(card):
            tokenURI = f"access_token={self.blizzard_token}" # URI para o token da blizzard
            url = f"https://us.api.blizzard.com/hearthstone/cards/{card['childIds'][0]}?locale=pt_br&gameMode=battlegrounds&{tokenURI}" # URL formatada para o reponse com todos o parametros
            response = requests.get(url) # Efetuando o GET da URL
            embed=discord.Embed(
                title=card["name"],
                description=f"""{response.json()["name"]}: {response.json()["text"].replace('<b>', '**').replace('</b>', '**').replace('<i>', '*').replace('</i>', '*')}\n
                    ``Raridade: {getRarity(card['rarityId'])}``
                    ``Vida: {card["health"]}``
                    ``Armadura: {card["armor"]}``
                """
            )
            embed.set_thumbnail(url=card["image"] )
            embed.set_image(url=response.json()["image"])
            embed.set_footer(text="Herói")
            return embed

        # Função que retorna uma mensagem personalizada para Lacaios
        def getMinionEmbedMessage(card):
            minionType = "Nenhum"
            try: # Caso o response da carta não tenha a variavel minionTypeId
                minionType = getMinionType(card['minionTypeId'])
            except:
                pass
            embed=discord.Embed(
                title=card["name"],
                description=f"""{card['text'].replace('<b>', '**').replace('</b>', '**').replace('<i>', '*').replace('</i>', '*')}\n
                    ``Tipo: {minionType}``
                    ``Raridade: {getRarity(card['rarityId'])}``
                    ``Vida: {card["health"]}``
                    ``Ataque: {card["attack"]}``
                    ``Gráu da taverna: {card["battlegrounds"]["tier"]}``
                """
            )
            embed.set_image(url=card["image"])
            embed.set_footer(text="Lacaio")
            return embed
        
        # Função que retorna uma mensagem personalizada para Missões e Recopensas
        def getQuestOrRewardEmbedMessage(card, cardType):
            embed=discord.Embed(
                title=card["name"],
                description=f"{card['text'].replace('<b>', '**').replace('</b>', '**').replace('<i>', '*').replace('</i>', '*')}"
            )
            embed.set_image(url=card["image"])
            embed.set_footer(text=cardType)
            return embed
