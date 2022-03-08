import os
from keep_alive import keep_alive
from discord.ext import commands

client = commands.Bot(
	command_prefix="h.",
	case_insensitive=True
)

@client.event 
async def on_ready():
    print("I'm in")
    print(client.user)

extensions = [
	'cogs.idle_breakout'
]

if __name__ == '__main__':
	for extension in extensions:
		client.load_extension(extension)

keep_alive()
token = os.environ.get("token") 
client.run(token)