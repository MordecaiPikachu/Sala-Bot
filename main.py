import discord
from discord.ext import commands
import os 
import random



class Bot(commands.Bot):

    
    def __init__(self):
        super().__init__(command_prefix='s+', pm_help=None, description="Discord Bot")
        self.add_command(self.ping)
        self.mypath=os.listdir("./komutlar")
        self.myfile=[]
        for dosya in self.mypath:
            if '.py' in dosya:
                lenght = len(dosya)
                fls = dosya[:lenght -3]
                self.myfile.append(fls)

        for x in self.myfile:
            try:
                self.load_extension("komutlar."+x)
            except:
                print("Hatalı dosya:"+x)
        
    async def on_ready(self):
        print("Kalktı")
        print(self.user.name)
        print(self.user.id)

    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content == "cinsel":
            await message.channel.send("cinsel demeyin ohhh")

        if message.content == "sa":
            await message.channel.send("as yiğen")

        if message.content == "ateist":
            await message.channel.send("dinsiz diyemezsin bana")

        if message.content == "büyücü":
            await message.channel.send("büyücü gibisini bulamazsınız")

        if message.content == "hacked":
            await message.channel.send("bunların yaptığı işler falan çok basit yani")
            await message.channel.send("iki üç hacked komutuyla hallediliyo")
            await message.channel.send("yani istesem ben sunucu kurup yaparımda")
            await message.channel.send("çocuklara şans tanıyorum işte")
            await message.channel.send("yenilere falan")

        if message.content == "turkish rap":
            await message.channel.send("söyle ona kasinmasin")

        if message.content == "reyiz naber":
            await message.channel.send("iyiyiz yeğen")

        if message.content == "hacked misin yoksa":
            await message.channel.send("hacked değilim eğer ölürsem dirilir tekrar yüz nakli yaparım")
            await message.channel.send("hacked dememelisin kimseye")

        if message.content == "hackedlersin istesen de merhamet ediyorsun":
            await message.channel.send("valla yengen zor tutuyor")
            await message.channel.send("yoksa biliyorsun işleri")
            await message.channel.send("karanlık işler falan")
            await message.channel.send("uğraşmıyorum")
            await message.channel.send("ekmeğimin peşindeyim artık")

        if message.content == "gerekirse canımızı veririz":
            await message.channel.send("destekleriniz önemli ben bu sunucunun kralıyım biliyorsun")
        
        if message.content == "multiplen seni banladı mı reyiz":
            await message.channel.send("valla banlamadı da yengene çok laf atıyor")
            await message.channel.send("laşşak da öyle")

        await self.process_commands(message) ##

    

    
    @commands.command()
    async def ping(self,ctx):
        await ctx.send("Büyücü :heart: ")

bot = Bot()
bot.run("buraya token yaz")
