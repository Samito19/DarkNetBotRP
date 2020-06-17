import discord
from commands import commandes
import hashlib

client = discord.Client(command_prefix="/")

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    hash = hashlib.sha1(member.name.encode("UTF-8")).hexdigest()
    await member.edit(nick=hash[:15])
    await member.add_roles(member.guild.get_role(718942056709357569))

@client.event
async def on_message(message):
    # Code pour la commande /contacter
    if message.channel.id == 718936905047081000 and message.author.id != client.user.id and (message.author.bot == False):
        if message.content.lower().startswith('/'):
            odd = lambda data: data['name'] == message.content[1:].split(' ')[0]
            next_function = next(filter(odd, commandes), None)
            if next_function != None:
                await next_function['do'](client, message, " ".join(message.content.split(' ')[1:]), message.content.split(' ')[1:])
            else:
                channel = await message.guild.get_member(message.author.id).create_dm()
                await channel.send('Commande Incorrecte !')
                await client.http.delete_message(message.channel.id, message.id)
        else:
            channel = await message.guild.get_member(message.author.id).create_dm()
            await channel.send('Commande Incorrecte !')
            await client.http.delete_message(message.channel.id, message.id)

@client.event
async def on_guild_channel_create(channel):
    if channel.category.name == '📱Communication':
        await channel.set_permissions(channel.guild.get_role(718847270090571808), send_messages=False, read_messages=False)
        await channel.set_permissions(channel.guild.get_member_named(channel.name[:15]), send_messages=True, read_messages=True)
        await channel.set_permissions(channel.guild.get_member_named(channel.name[16:]), send_messages=True, read_messages=True)
        sender = channel.guild.get_member_named(channel.name[:15]).mention
        receiver = channel.guild.get_member_named(channel.name[16:]).mention
        await channel.send('Cette conversation est entièrement **cryptée**, les messages qui y seront échangés ne seront accéssibles  que par les utilisateurs {sender} et {receiver} . Pensez à vous transmettre un code Reddit pour communiquer avec un téléphone. '.format(sender=sender, receiver=receiver))

def main(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    message = 'It works!\n'
    return [message.encode()]

client.run('NzE4ODYyOTI0NDA3MzczOTA2.Xtvg8A.Ms9vwjatkOKpJdx3c9yZyDvkUZo')
