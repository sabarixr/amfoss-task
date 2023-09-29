import discord
from discord.ext import commands
from scraper import get_livescore, livescore_file, team_info
import os
from dotenv import load_dotenv
from discord import File

# CHANNEL_ID = 1148976335151190048

crickey = commands.Bot(command_prefix="/", intents=discord.Intents.all(), help_command=None)


# @crickey.event
# async def on_member_join(member):

#   channel = member.guild.get_channel(CHANNEL_ID)


#   welcome_message = f"Welcome on board! Have a great time ahead, {member.mention}!"
#   await channel.send(welcome_message)


@crickey.command(aliases=["hello_message"])
async def hello(ctx):
    await ctx.send(
        "Hello there! I am a cricket score Discord bot named CricKey created as part of Amfoss task. I am glad to "
        "help you by providing data of cricket matches.")


@crickey.command(aliases=["more_info_message"])
async def moreinfo(ctx):
    await ctx.send(
        "you can get more info about cricket matches by visiting the link "
        "https://www.espncricinfo.com/live-cricket-score")


@crickey.command(aliases=["live_score"])
async def livescore(ctx):
    await ctx.send("Fetching match data....")
    score_data = get_livescore()
    if "error" in score_data:
        await ctx.send("NO live matches available! Try again later")
    else:
        response = f"{score_data['team_one']} vs {score_data['team_two']}\n"
        response += f"Score: {score_data['match_score1']} - {score_data['match_score2']}\n"
        response += f"Overs: {score_data['match_over1']} - {score_data['match_over2']}\n"
        response += f" {score_data['match_summary']}\n\n"
        response += f" {score_data['time']}"

        await ctx.send(response)


@crickey.command(aliases=["livescorecsv"])
async def generate(ctx):
    await ctx.send("generating csv file...")
    livescore_file()

    if os.path.exists('livescore.csv'):
        if os.path.exists('livescore.csv'):

            with open('livescore.csv', 'rb') as file:
                csv_file = File(file, filename='livescore.csv')
                await ctx.send("Here is the updated live score CSV file:", file=csv_file)
        else:
            await ctx.send("CSV file generation failed.")


@crickey.command(aliases=["team_info"])
async def teaminfo(ctx):
    await ctx.send("Generating file....")
    team_info()
    if os.path.exists('team_info.csv'):
        if os.path.exists('team_info.csv'):

            with open('team_info.csv', 'rb') as file:
                csv_file = File(file, filename='team_info.csv')
                await ctx.send("Here is the CSV file:", file=csv_file)
        else:
            await ctx.send("CSV file generation failed.")


@crickey.command(aliases=["help_message"])
async def help(ctx):
    await ctx.send("/hello - Get an into about the bot.\n"
                   "/moreinfo-provides link to the website to obtain more info about matches\n"
                   "/livescore - Get the live cricket score.\n"
                   "/generate - Generate a CSV file with live scores.\n"
                   "/teaminfo - Generate a csv file that gives the name of current players in team india"
                   "/help - Show this help message.")
load_dotenv()
DISCORD_API = os.getenv("DISCORD_API_TOKEN")
crickey.run(DISCORD_API)
