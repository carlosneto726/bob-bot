from discord.ext import commands, tasks
import discord, os, asyncio, requests


@client.command()
async def feliz_aniversario(ctx):
  await ctx.channel.send("Feliz aniversário")
