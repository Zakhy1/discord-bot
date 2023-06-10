import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="/", help_command=None, intents=disnake.Intents.all())

CENSORED_WORDS = ["елизарова"]

BOT_TOKEN = open("token.txt").readline()

@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready to work!")


@bot.event
async def on_member_join(member):
    role = await disnake.utils.get(guild_id=member.guild.roles, id=1049575838015832074)
    channel = bot.get_channel(941619280112398389)
    embed = disnake.Embed(
        title="Новый попуск!",
        description=f"{member.name}#{member.discriminator}",
        color=0xffffff
    )
    await member.add_roles(role)
    await channel.send(embed=embed)


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    for i in message.content.split():
        for j in CENSORED_WORDS:
            if i.lower() == j:
                await message.delete()
                await message.channel.send(f"{message.author.mention} мы здесь падл не упоминаем!")


if __name__ == '__main__':
    bot.run(BOT_TOKEN)
