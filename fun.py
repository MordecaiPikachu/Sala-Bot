from discord.ext import commands
import discord
import random
import kontrol

class Eğlence:
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def özlüsöz(self, ctx):
        messages = ["gerçekleri tarih yazar tarihi de salaş baba yapar","Mutsuzluk başa bela, yaşamak deva", "herkes hata yapar ama ben yapmam yaptıysam da yanlışlıkla olmuştur", "herkes sevdiğinden ayrılır er ya da geç önemli olan anı yaşamak", "susmak ölümden daha tehlikelidir","krallık genlerde","κlαπα $αlαş εl κøψδu" ]
        await ctx.send(random.choice(messages))

    @commands.command()
    async def klan(self,ctx):
        await ctx.send("κlαπα $αlαş εl κøψδu")
   
    @commands.command()
    async def salastaninciler(self,ctx):
        await ctx.send("dere yedeği ne")
        await ctx.send("sürekli alıyor multiplen")

def setup(bot):
    bot.add_cog(Eğlence(bot))