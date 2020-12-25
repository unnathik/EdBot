import discord
import requests
import shutil
import json
import wolframalpha
from discord.ext import commands
import wikipedia
from googlesearch import search

client = discord.Client()

TOKEN = 'NzkyMDEyNzg4MTMzNjU4NjM0.X-XhYw.-9cujAxRDfSBYJtK2BaSbfEfW2I'
WOLFRAM = '6XLY7X-YJL4JLAEK4'
wolframclient = wolframalpha.Client(WOLFRAM)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!factor'):
        problem = message.content.replace('!factor ', 'factor ')
        res = wolframclient.query(problem)
        ans = next(res.results).text
        await message.channel.send(ans)

    if message.content.startswith('!domain'):
        problem = message.content.replace('!domain ', 'domain ')
        res = wolframclient.query(problem)
        ans = next(res.results).text
        await message.channel.send(ans)

    if message.content.startswith('!range'):
        problem = message.content.replace('!range ', 'range of ')
        res = wolframclient.query(problem)
        ans = next(res.results).text
        await message.channel.send(ans)

    if message.content.startswith('!solve'):
        problem = message.content.replace('!solve ', 'solve ')
        res = wolframclient.query(problem)
        ans = next(res.results).text
        await message.channel.send(ans)

    if message.content.startswith('!simplify'):
        problem = message.content.replace('!simplify ', 'simplify ')
        res = wolframclient.query(problem)
        ans = next(res.results).text
        await message.channel.send(ans)
        
    if message.content.startswith('!roots'):
        problem = message.content.replace('!roots ', 'solve ')
        problem += ' = 0 for x'
        res = wolframclient.query(problem)
        ans = next(res.results).text
        await message.channel.send(ans)

    if message.content.startswith('!search-summary'):
        problem = message.content.replace('!search-summary ', '')
        searchResults = wikipedia.search(problem)
        
        if not searchResults:
            await message.channel.send("No result from Wikipedia")

        try:
            page = wikipedia.page(searchResults[0])
        except wikipedia.DisambiguationError as err:
            page = wikipedia.page(err.options[0])

        wikiSummary = str(page.summary.encode('utf-8'))
        await message.channel.send(wikiSummary)

    if message.content.startswith('!tell-me'):
        problem = message.content.replace('!tell-me ', '')
        res = wolframclient.query(problem)
        output = next(res.results).text
        await message.channel.send(output)
    
    # if message.content.startswith('!equation-save'):
    #     equation = message.content.replace('equation-save', '')
    #     await message.author.send(equation)
    #     await message.delete()

    if message.content.startswith('!poll'):
        polldesc = message.content.replace('!poll', '')
        emb = discord.Embed(title = "POLL", description = polldesc)
        msg = await message.channel.send(embed = emb)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')

    if message.content.startswith('!stack-search'):
        await stacksearch(message)

async def stacksearch(message):
    query = message.content.replace('!stack-search', '') + "site:stackoverflow.com"
    for i in search(query):
        await message.channel.send(i)

@client.event
async def on_ready():
    print('Bot is ready.')

client.run(TOKEN)