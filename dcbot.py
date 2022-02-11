import discord
from discord.ext import commands
import random
import asyncio
import datetime
from discord.ext.commands import has_permissions, MissingPermissions

# Config Kısmı

token             = 'ODUwNzc5NTQyOTcyMDA2NDkx.YLusMQ.d3UJZMvqREvofU1TEvL_OohtAnU'
prefix            = '.'
logkanali         = '941742494612324352' 
giriskanali       = '939900539553087530' 
cikiskanali       = '939900539553087530' 
kayıtsız          = '941742634903420948' 
whitelist         = '941742688556961872' 
tsip              = '1881'
serverip          = '1881'
discordurl        = 'https://discord.gg/AHxM37ay'
aktifimage    = 'https://cdn.discordapp.com/attachments/936287990685249656/939963962731151360/Ekran_goruntusu_2022-02-06_213213.png'
restartimage  = 'https://cdn.discordapp.com/attachments/936287990685249656/939963962731151360/Ekran_goruntusu_2022-02-06_213213.png'
bakımimage    = 'https://cdn.discordapp.com/attachments/936287990685249656/939963962731151360/Ekran_goruntusu_2022-02-06_213213.png'
servericon    = 'https://cdn.discordapp.com/attachments/936287990685249656/939963962731151360/Ekran_goruntusu_2022-02-06_213213.png'

# Tüm Configleri Doldurmadan Bot Tam Anlamıyla Çalışmaz

intents = discord.Intents().all()
client = commands.Bot(command_prefix=prefix, intents = intents)


@client.event
async def on_ready():
    print('Discord Botu Aktif!')
    await client.change_presence(activity=discord.Game(name=f"🔥 Made by FaP  🔥")) # Discord Botun Oynuyor Kısmı
    await client.change_presence(activity=discord.Game(name=f"🔥 x RP  🔥")) # İstediğiniz gibi değiştirebilirsiniz.
    client.remove_command('help')  # Bunu Silmenizi Önermem Kötü Bir help teması var siz yeni help yazarsanız daha hoş durur.

async def ch_pr():
    await client.wait_until_ready()

    statuses = ["🔥 Made by FaP  🔥", "🔥 x RP  🔥"] # Yukarda Değiştirdiğiniz yazıyı burayada eklemeniz gerekir!

    while not client.is_closed():

        status = random.choice(statuses)
        await client.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(5) # Yazının Kaç Saniyede Bir Değişceğini ayarlayabilirsiniz
client.loop.create_task(ch_pr())


#Destek Komutu
@client.command()
async def destek(ctx):        
    role = discord.utils.get(ctx.guild.roles, name=whitelist)
    if role in ctx.author.roles:
        embed = discord.Embed(
            title = f'{ctx.author.name} Destek Talebi',
            description = 'Destek Talebiniz Alınmıştır. En Yakın Zamanda Destek Ekibimiz Size Yardımcı Olacaktır.',
            color = 0
        )

        embed.set_footer(text=f"{ctx.guild.name}")

        await ctx.send(embed=embed)
        return
    else:
        await ctx.send('Kayıtlı Oyuncularımız Sadece Destek Talebinde Bulunabilir!')

#Kayıt Komutu
@client.command()
async def kayıt(ctx):

    role = discord.utils.get(ctx.guild.roles, name=kayıtsız)
    if role in ctx.author.roles:
        embed = discord.Embed(
            title = f'{ctx.author.name} Kayıt Talebi',
            description = 'Kayıt Talebiniz Alınmıştır. En yakın zamanda Kayıt Ekibimiz Size Yardımcı Olacaktır.',
            color = 0
        )

        embed.set_footer(text=f"{ctx.guild.name}")

        await ctx.send(embed=embed)
        return
    else:
        await ctx.send('Kayıtlı Oyuncularımız Kayıt Talebinde Bulunamaz!')


#Aktif Komutu
@client.command()
@has_permissions(manage_guild=True) # Sadece Manage_guild Yetkisi Olanlar Kullanabilir
async def aktif(ctx):
        aktifembed = discord.Embed(description="Sunucumuz Aktiftir! ✅")
        aktifembed.set_author(name="Discord Adresimiz", url=f"{discordurl}", icon_url=servericon)
        aktifembed.set_thumbnail(url=aktifimage)
        aktifembed.set_image(url=aktifimage)
        aktifembed.add_field(name=f'Server IP : {serverip} ', value= f'Ts3 : {tsip}', inline=False) 
        aktifembed.add_field(name=f'{ctx.guild.name} Herkese iyi roller diler.', value= '🎉', inline=False)
        await ctx.send(embed=aktifembed)

#Restart Komutu
@client.command()
@has_permissions(manage_guild=True) # Sadece Manage_guild Yetkisi Olanlar Kullanabilir
async def restart(ctx):
        restartembed = discord.Embed(description="Sunucumuza Restart Atılıyor ❗️❗️") 
        restartembed.set_thumbnail(url=restartimage)
        restartembed.set_image(url=restartimage)
        restartembed.set_author(name="Discord Adresimiz", url=f"{discordurl}", icon_url=servericon)
        restartembed.add_field(name=f'Datalarınızın Zarar Görmemesi İçin Lütfen Oyundan Çıkış Yapalım', value="Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz", inline=False) 
        restartembed.add_field(name=f'{ctx.guild.name} Ailesi', value= '💖', inline=False)
        await ctx.send(embed=restartembed)

#Bakım Komutu
@client.command()
@has_permissions(manage_guild=True) # Sadece Manage_guild Yetkisi Olanlar Kullanabilir
async def bakım(ctx):
        bakımembed = discord.Embed(description="Sunucumuz Kısa Süreliğine Bakıma Alınmıştır ❗️❗️")
        bakımembed.set_thumbnail(url=bakımimage)
        bakımembed.set_author(name="Discord Adresimiz", url=f"{discordurl}", icon_url=servericon)
        bakımembed.set_image(url=bakımimage)
        bakımembed.add_field(name=f'En Kısa Sürede Tekrar Aktif Verilecektir', value="Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz", inline=False) 
        bakımembed.add_field(name=f'{ctx.guild.name} Ailesi', value= '💖', inline=False)
        await ctx.send(embed=bakımembed)



# Kayıtal Komutu
@client.command(pass_context=True)
@has_permissions(manage_nicknames=True)
async def kayıtal(ctx, user: discord.Member):
    rol = discord.utils.get(ctx.guild.roles, name=whitelist)
    rol2 = discord.utils.get(ctx.guild.roles, name=kayıtsız)
    await user.add_roles(rol)
    await user.remove_roles(rol2)
    await ctx.message.add_reaction(u"✅")
    channel = client.get_channel(int(logkanali))
    await channel.send(f"<@!{ctx.author.id}> isimli yetkili , {user.mention} isimli Oyuncuya {rol.name} permi verdi!")

#Avatar Komutu
@client.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    if avamember == None:
        await ctx.send('Lütfen Birini Etiketleyiniz')
    else:
        userAvatarUrl = avamember.avatar_url
        await ctx.send(userAvatarUrl)
        return

#Clear Komutu
@client.command()
@has_permissions(manage_guild=True) # Sadece Manage_guild Yetkisi Olanlar Kullanabilir
async def clear(ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.channel.send(f'Başarıyla {amount} tane mesaj silindi', delete_after=2)

@client.event
async def on_member_join(member):
        date_format = "%x, %X"
        girisembed = discord.Embed(title=f"discord id : {member.id}")
        girisembed.set_thumbnail(url=f'{member.avatar_url}')
        girisembed.set_author(name=member.name, icon_url=member.avatar_url)
        girisembed.add_field(name="Hesap Kuruluş Tarihi: ", value=member.created_at.strftime(date_format))
        girisembed.set_footer(text=f"{member.guild.name}", icon_url=f"{member.avatar_url}")
        giriskanal = client.get_channel(int(giriskanali))
        await giriskanal.send(member.mention, embed=girisembed)

@client.event
async def on_member_remove(member):

        membercikis = datetime.datetime.now()
        membercikistarihi = membercikis.strftime("%x, %X")
        
        cikisembed = discord.Embed(title=f"Bir Kullanıcı Sunucudan Çıktı")
        cikisembed.set_author(name=f"{member.name}#{member.discriminator}" ,icon_url=member.avatar_url)
        cikisembed.set_thumbnail(url=f'{member.avatar_url}')
        cikisembed.add_field(name="Sunucudan Ayrılma Tarihi", value=f"{membercikistarihi}", inline=False)
        cikisembed.add_field(name="Kullanıcı Bilgileri:", value=f"{member.name}#{member.discriminator}  -  {member.id}", inline=False)
        cikisembed.set_footer(text=f"{member.guild.name}", icon_url=member.guild.icon_url)
        giriskanal = client.get_channel(int(cikiskanali))
        await giriskanal.send(member.mention, embed=cikisembed)

client.run(f'{ODUwNzc5NTQyOTcyMDA2NDkx.YLusMQ.d3UJZMvqREvofU1TEvL_OohtAnU}')
