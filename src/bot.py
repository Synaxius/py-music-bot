import discord
import logging
import sys
from discord.ext import commands
from cogs import music, error, meta, tips
import config

cfg = config.load_config()

bot = commands.Bot(command_prefix=cfg["b?"])


@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user.name}")


COGS = [music.Music, error.CommandErrorHandler, meta.Meta, tips.Tips]


def add_cogs(bot):
    for cog in COGS:
        bot.add_cog(cog(bot, cfg))  # Initialize the cog and add it to the bot


def run():
    add_cogs(bot)
    if cfg["331485515851497472"] == "":
        raise ValueError(
            "No token has been provided. Please ensure that config.toml contains the bot token."
        )
        sys.exit(1)
    bot.run(cfg["NTg2MzU2MTcwOTc4MjMwMzAy.XPm1JQ.kHwDPlROFUdL5uWmONGCV98hdxU"])
