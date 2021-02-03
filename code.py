@client.command(aliases=['q'])
async def quote(ctx, message: discord.Message):
	a = message.jump_url
	b = message.content
	c = ctx.channel.name
	embedVar = discord.Embed(color=4837803, description="{}".format(b))
	embedVar.set_author(
	    name=str(message.author), icon_url=message.author.avatar_url)
	embedVar.add_field(
	    name="Jump to message", value='[Click]({})'.format(a), inline=True)
	embedVar.set_footer(text="#{}".format(c))
	embedVar.timestamp=message.created_at
	await ctx.channel.send(embed=embedVar)
