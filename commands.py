import discord
import time
import hashlib

async def contacter(client, message, content, params):
    if content != '' and content != None and message.channel.id == 718936905047081000:
        try:
            user_id = int(params[0].replace('<@!', '').replace('>', ''))
            await message.guild.create_text_channel('{sender}-{receiver}'.format(sender=message.author.display_name, receiver=message.guild.get_member(user_id).display_name), category=discord.utils.get(message.guild.categories, name='📱Communication'))
            await client.http.delete_message(message.channel.id, message.id)
        except:
            await client.http.delete_message(message.channel.id, message.id)
            channel = await message.guild.get_member(message.author.id).create_dm()
            await channel.send('Commande Incorrecte !')
    else:
        await client.http.delete_message(message.channel.id, message.id)
        channel = await message.guild.get_member(message.author.id).create_dm()
        await channel.send('Commande Incorrecte !')

async def suppmessages(client, message, content, params):
    if message.channel.category.name == '📱Communication':
        try:
            msgs = await message.channel.history(limit=200).flatten()
            await message.channel.delete_messages(msgs)
            await message.channel.send(':warning: Tout les messages ont été supprimés ! Ce message sera également automatiquement supprimé dans les prochaines secondes. :warning:')
            time.sleep(7)
            await client.http.delete_message(message.channel.id, message.id)

        except:
            await client.http.delete_message(message.channel.id, message.id)
            channel = await message.guild.get_member(message.author.id).create_dm()
            await channel.send('Une erreur a été detectée, veuillez retaper la commande !')
    else:
        await client.http.delete_message(message.channel.id, message.id)
        channel = await message.guild.get_member(message.author.id).create_dm()
        await channel.send('Utilisez cette commande dans un channel !')

async def changerid(client, message, content, params):
    if message.channel.name == 'console':
        try:
             hash = hashlib.sha1(message.guild.get_member(message.author.id).display_name.encode("UTF-8")).hexdigest()
             await message.guild.get_member(message.author.id).edit(nick=hash[:15])
             await client.http.delete_message(message.channel.id, message.id)
        except:
             await client.http.delete_message(message.channel.id, message.id)
    else:
        await client.http.delete_message(message.channel.id, message.id)
        channel = await message.guild.get_member(message.author.id).create_dm()
        await channel.send('Utilisez cette commande dans le channel console !')

async def suppchannel(client, message, content, params):
    if message.channel.category.name == '📱Communication':
        try:
            msgs = await message.channel.history(limit=200).flatten()
            await message.channel.delete_messages(msgs)
            await message.channel.send(':warning: Ce channel en est en cours de suppression, ce dernier ne sera plus visible dans quelques secondes :warning:')
            time.sleep(5)
            await message.channel.delete()
        except:
            await client.http.delete_message(message.channel.id, message.id)
            channel = await message.guild.get_member(message.author.id).create_dm()
            await channel.send('Une erreur a été detectée, veuillez retaper la commande !')
    else:
        await client.http.delete_message(message.channel.id, message.id)
        channel = await message.guild.get_member(message.author.id).create_dm()
        await channel.send('Veuillez utiliser la commande dans un channel !')



commandes = [
    {
        "name":"contacter",
        "do":contacter
    },
    {
        "name": "suppmessages",
        "do": suppmessages
    },
    {
        "name": "changerid",
        "do": changerid
    },
    {
        "name": "suppchannel",
        "do": suppchannel
    }
]
