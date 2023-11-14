import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

    server_id = SERVER ID GOES HERE
    roles_channel_id = ROLE CHANNEL ID

    guild = bot.get_guild(server_id)
    if guild:
        roles_channel = guild.get_channel(roles_channel_id)

        if roles_channel:
            message = await roles_channel.send(
                "Please react to the roles you want.\n"
                ":EMOJI_NAME1: - DeerIsle\n"
                ":EMOJI_NAME2: - Nyheim\n"
                ":EMOJI_NAME3: - Chernarus"
            )
            for emoji in ['EMOJI1', 'EMOJI2', 'EMOJI3']:
                await message.add_reaction(emoji)

@bot.command()
async def show_roles(ctx):
    server_id = SERVER ID GOES HERE
    roles_channel_id = ROLE CHANNEL ID

    if ctx.guild.id == server_id:
        roles_channel = ctx.guild.get_channel(roles_channel_id)

        if roles_channel:
            await roles_channel.send(
                "Please react to the roles you want.\n"
                ":EMOJI_NAME1: - DeerIsle\n"
                ":EMOJI_NAME2: - Nyheim\n"
                ":EMOJI_NAME3: - Chernarus"
            )

@bot.event
async def on_raw_reaction_add(payload):
    channel_id = payload.channel_id
    message_id = payload.message_id
    user_id = payload.user_id
    emoji = payload.emoji.name

    server_id = SERVER ID GOES HERE
    role_ids = {
        'EMOJI1': ROLE ID,
        'EMOJI2': ROLE ID,
        'EMOJI3': ROLE ID,
    }

    if channel_id == CHANNEL ID:
        guild = bot.get_guild(server_id)
        member = await guild.fetch_member(user_id)
        
        if member == bot.user:
            return

        if emoji in role_ids:
            role_id = role_ids[emoji]
            role = guild.get_role(role_id)
            await member.add_roles(role)
            print(f'Added {role.name} to {member.name}')

@bot.event
async def on_raw_reaction_remove(payload):
    channel_id = payload.channel_id
    message_id = payload.message_id
    user_id = payload.user_id
    emoji = payload.emoji.name

    server_id = SERVER ID GOES HERE
    role_ids = {
        'EMOJI1': ROLE ID,
        'EMOJI2': ROLE ID,
        'EMOJI3': ROLE ID,
    }

    if channel_id == CHANNEL ID:
        guild = bot.get_guild(server_id)      
        member = await guild.fetch_member(user_id)

        if emoji in role_ids:
            role_id = role_ids[emoji]
            role = guild.get_role(role_id)
            await member.remove_roles(role)
            print(f'Removed {role.name} from {member.name}')


bot.run('TOKEN')
