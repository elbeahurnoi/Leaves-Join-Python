import discord
from discord.ext import commands

# Introduce aquí tu token de Discord
TOKEN = 'tu_token_aqui'

# Prefijo de los comandos del bot
bot = commands.Bot(command_prefix='!')

# Evento de bienvenida
@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel  # Obtiene el canal de bienvenida
    if channel is not None:
        # Envia un mensaje de bienvenida al canal de bienvenida
        await channel.send(f'Bienvenido {member.mention} al servidor!')

# Evento de despedida
@bot.event
async def on_member_remove(member):
    channel = member.guild.system_channel  # Obtiene el canal de bienvenida
    if channel is not None:
        # Envia un mensaje de despedida al canal de bienvenida
        await channel.send(f'{member.display_name} ha abandonado el servidor. ¡Hasta luego!')

# Inicia el bot
bot.run(TOKEN)
