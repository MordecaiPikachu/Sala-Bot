import discord
from discord.ext import commands


def is_owner():

    async def kontrol(ctx):
        return ctx.author.id == 528960664665063430

    return commands.check(kontrol)

def is_admin():

    async def kontrol(ctx):
        return ctx.author.guild_permissions.administrator

    return commands.check(kontrol)