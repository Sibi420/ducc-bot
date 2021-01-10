import random
import requests
import json
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import http.client

TOKEN = "NzE1MjU4Mjc4NDY4Mzg2ODQ3.Xs76uQ.glgyU6OYpNu4rrpinjiV50Vu8r0"

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print("Bot is on")

@bot.command()
async def song(ctx):
	songs = {1:'hax suggested: https://youtu.be/MtN1YnoL46Q',2:'hax suggested: https://youtu.be/w0AOGeqOnFY'}
	songNumber = random.randint(1,len(songs))
	await ctx.send(songs[songNumber])

@bot.command()
async def quacku(ctx):
	gc = 0
	gco = 0
	g = ''
	for guild in bot.guilds:
		g= guild.name + ", " + g
		gc = int(guild.member_count) + gc 
		gco += 1

	g = g[:-2]
	
	embed = discord.Embed(title='Ducc Bot 3.1', description="This is the final updated ducc bot version", color=0xeee657)
	embed.add_field(name="Servers Using Ducc" , value=g)
	embed.add_field(name="People Using Ducc" , value=gc) 
	embed.add_field(name="Server Count" , value=gco)    
	embed.add_field(name="Join Our Server", value='https://discord.gg/uKJHQkw')
	embed.add_field(name="Donate To Keep Ducc Running", value='Join server for more information')
	
		
	
	
		
	await ctx.send(embed=embed)

@bot.command()
async def quack(ctx):

	embed = discord.Embed(title='Ducc Bot 3.1', description="This is the final updated ducc bot version", color=0xeee657)
	embed.add_field(name="!quacku ", value='Shows how many people use ducc')
	embed.add_field(name="!quacks", value='Will show player and guild stats')
	embed.add_field(name="!quacka", value='Will show all player build battle stats')
	embed.add_field(name="!checkname", value='Will ckeck if username is available')
	embed.add_field(name="!servercount", value='Will show member count in ducc server')
	embed.add_field(name="Update Log", value='https://docs.google.com/document/d/1FyvdPyJ8jt_JddGqnfFVa8MwplQvbWX03U3F4xp5OwI/edit?usp=sharing')
	embed.add_field(name="Join Our Server", value='https://discord.gg/uKJHQkw')
	embed.add_field(name="Donate To Keep Ducc Running", value='Join server for more information')
	embed.add_field(name='Thank you for using Ducc Bot', value='Type one of the commands above to get your stats today!')
		
	
	
		
	await ctx.send(embed=embed)

@bot.command()
async def checkname(ctx, arg):
	try:
		ign = arg
		print(ign)
		
		
		username = ign



		http_conn = http.client.HTTPSConnection("api.mojang.com");
		http_conn.request("GET", "/users/profiles/minecraft/" + username,
		    headers={'User-Agent':'Minecraft Username -> UUID', 'Content-Type':'application/json'});
		response = http_conn.getresponse().read().decode("utf-8")

		json_data = json.loads(response)
		try:
		    uuid = json_data['id']
		except KeyError as e:
		    print("KeyError raised:", e);

		uuidurl = 'https://visage.surgeplay.com/full/'+uuid
		embed = discord.Embed(title='Ducc Bot 3.1', description="This is the final updated ducc bot version", color=0xeee657)
		embed.set_image(url=uuidurl)
		embed.add_field(name="Name: " + ign, value="Unavailable")

		await ctx.send(embed=embed)
	except:
		embed = discord.Embed(title='Ducc Bot 3.1', description="This is the final updated ducc bot version", color=0xeee657)
		embed.add_field(name="Name: " + ign, value='Available')
		await ctx.send(embed=embed)

@bot.command()
async def quacka(ctx, arg):
	
	ign = arg
	print(ign)
	
	
	username = ign



	http_conn = http.client.HTTPSConnection("api.mojang.com");
	http_conn.request("GET", "/users/profiles/minecraft/" + username,
	    headers={'User-Agent':'Minecraft Username -> UUID', 'Content-Type':'application/json'});
	response = http_conn.getresponse().read().decode("utf-8")
	try:
		json_data = json.loads(response)
	except:
		await ctx.send('Invalid Username')
	try:
	    uuid = json_data['id']
	except KeyError as e:
	    print("KeyError raised:", e);

	uuidurl = 'https://visage.surgeplay.com/full/'+uuid
	try:
		url = "https://api.hypixel.net/player?key=b4db2c02-3829-47eb-a0f2-2c5753a65eb5&name=" + ign
	except:
		await ctx.send('Invalid Username')
	


	response = requests.get(url)

	json_response = response.json()

	
	
	bbstats = json_response['player']['stats']['BuildBattle']
	

	wins = json_response['player']['stats']['BuildBattle']['wins']
	try:
		team_wins = json_response['player']['stats']['BuildBattle']['wins_teams_normal']
	except:team_wins = 0
	try:
		solo_wins = json_response['player']['stats']['BuildBattle']['wins_solo_normal']
	except: solo_wins = 0
	try:
		super_votes = json_response['player']['stats']['BuildBattle']['super_votes']
	except: super_votes = 0
	try:
		gtb_wins = json_response['player']['stats']['BuildBattle']['wins_guess_the_build']
	except:gtb_wins = 0
	try:
		pro_wins = json_response['player']['stats']['BuildBattle']['wins_solo_pro']
	except:pro_wins = 0
	games_played = json_response['player']['stats']['BuildBattle']['games_played']
	coins = json_response['player']['stats']['BuildBattle']['coins']
	
	score = json_response['player']['stats']['BuildBattle']['score']

	try:
		json_rubber_duck = json_response['player']['stats']['BuildBattle']['wins']['votes_Rubber Duck']
	except:
		json_rubber_duck = 0

	solo_wins = int(wins) - int(team_wins) - int(gtb_wins) - int(pro_wins) - int(solo_wins) + int(solo_wins)


	url = 'https://sk1er.club/stats/' + ign

	roxurl = 'https://sk1er.club/stats/roxannegr'

	roxresponse1 = requests.get(roxurl, verify=False)
	roxhtmlContent = BeautifulSoup(roxresponse1.content, "html.parser")
	roxpage = roxhtmlContent.get_text()
	roxpagestr = str(roxpage)
	roxpagestr = str.splitlines(roxpagestr)


	for lines in roxpagestr:
		if "Build Battle Ranking:" in lines:
			lines = lines[24:]
			roxbbpos = lines
			roxbbpos = int(roxbbpos)
			roxbbpos = 2-roxbbpos





	response1 = requests.get(url, verify=False)
	htmlContent = BeautifulSoup(response1.content, "html.parser")
	page = htmlContent.get_text()
	pagestr = str(page)
	pagestr = str.splitlines(pagestr)

	for lines in pagestr:
		if "Build Battle Ranking:" in lines:
			lines = lines[24:]
			bbpos = lines
	try:
		bbpos = int(bbpos)		
		bbpos = bbpos + roxbbpos
	except:bbpos = "false"
			
	if score < 100:
		rank = "Rookie"	
	elif score > 100 and score < 250:
		rank = "Untrained"
	elif score > 250 and score < 1000:
		rank = "Apprentice"
	elif score > 1000 and score < 2000:
		rank = "Experienced"
	elif score > 2000 and score < 3500:
		rank = "Seasoned"
	elif score > 3500 and score < 5000:
		rank = "Trained"
	elif score > 5000 and score < 7500:
		rank = "Skilled"
	elif score > 7500 and score < 10000:
		rank = "Talented"	
	elif score > 10000 and score < 15000:
		rank = "Proffesional"
	elif score > 15000 and score < 20000:
		rank = "Expert"
	elif score > 20000 and score < 50000:
		rank = "Master"
	elif score > 50000:
		rank = "Ducc Worthy"

	winloss = wins / games_played

	winloss = str(winloss)
	winloss = winloss[:5]
	try:
		bbstats1 = json_response['player']['parkourCompletions']['BuildBattle']
		bbstats1 = str(bbstats1)
		bbstats1 = str.split(bbstats1)

		prevWord = ""
		recTime = 999999
		for aValue in bbstats1:
			if prevWord == "'timeTook':":
		
			
				aValue=aValue[:-2]
				aValue = int(aValue)
			

				if aValue < recTime:
					recTime = aValue
				

					
				else: aValue = aValue
		
			
			

			else:
				aValue = aValue
			prevWord = aValue

		recTime = str(recTime)
		if len(recTime) == 5: 
			recTime1 = recTime[:2]
			recTime2 = recTime[2:]
			recTime = recTime1 + '.' +recTime2
		elif len(recTime) == 6:
			recTime1 = recTime[:3]
			recTime2 = recTime[3:]
			recTime = recTime1 + '.'+recTime2
	except:
		recTime = "Never Attempted"



	else: wins = wins 
	wins = str(wins)
	solo_wins = str(solo_wins)
	team_wins = str(team_wins)
	pro_wins = str(pro_wins)
	gtb_wins = str(gtb_wins)
	games_played = str(games_played)
	winloss = str(winloss)
	coins = str(coins)
	
	rank = str(rank)
	
	bbpos = str(bbpos)
	score = str(score)
	recTime = str(recTime)

	if ign == 'morve':
		bbpos = 1
	# ign = ign.lower()
	# if ign == "ilysylvia":
	# 	wins = "USE HYPIXEL BUILD BATTLE BOT, WHAT YOU GET FOR DELETING MY SERVER CHANNEL NAMES"
	# 	solo_wins = wins
	# 	team_wins = wins
	# 	pro_wins = wins
	# 	gtb_wins = wins
	# 	games_played = wins
	# 	winloss = wins
	# 	coins = wins
	# 	coins_monthly = wins
	# 	rank = wins
	# 	json_rubber_duck = wins
	# 	bbpos = wins
	# 	score = 	wins
	# 	recTime = 	wins
	# 	uuidurl = 'https://cdn.newsapi.com.au/image/v1/542f75b5c5eb303758ad93bd0c705410?width=650'
		super_votes = wins 
	embed = discord.Embed(title='Ducc Bot 3.1', description=ign, color=0xeee657)
	embed.set_image(url=uuidurl)
	embed.add_field(name="Total Wins", value=wins)
	embed.add_field(name="Solo Wins", value=solo_wins)
	embed.add_field(name="Team Wins", value=team_wins)
	embed.add_field(name="Pro Wins", value=pro_wins)
	embed.add_field(name="Guess The Build Wins", value=gtb_wins)
	embed.add_field(name="Games Played", value=games_played)
	embed.add_field(name="Win Loss Ratio", value=winloss)
	embed.add_field(name="Coins", value=coins)
	embed.add_field(name="Record Parkour Time In Seconds", value=recTime)
	embed.add_field(name="Score", value=score)
	embed.add_field(name="Rank", value=rank)
	embed.add_field(name="Super Votes", value=super_votes)
	if bbpos == "false":
		embed.add_field(name="Build Battle Position (Approximately)", value="You Are Not Placed")
	else:
		embed.add_field(name="Build Battle Position (Approximately)", value=bbpos)
	embed.add_field(name="Join Our Server", value='https://discord.gg/uKJHQkw')
	embed.add_field(name="Donate To Keep Ducc Running", value='Join server for more information')
	
		
	await ctx.send(embed=embed)




@bot.command()
async def quacks(ctx, arg):
	
	ign = arg
	print(ign)
	
	
	username = ign



	http_conn = http.client.HTTPSConnection("api.mojang.com");
	http_conn.request("GET", "/users/profiles/minecraft/" + username,
	    headers={'User-Agent':'Minecraft Username -> UUID', 'Content-Type':'application/json'});
	response = http_conn.getresponse().read().decode("utf-8")
	try: 
		json_data = json.loads(response)
	except:
		await ctx.send("Invalid Username")
	try:
	    uuid = json_data['id']
	except KeyError as e:
	    print("KeyError raised:", e);

	uuidurl = 'https://visage.surgeplay.com/full/'+uuid


	url = 'https://sk1er.club/stats/' + ign
	response1 = requests.get(url, verify=False)
	htmlContent = BeautifulSoup(response1.content, "html.parser")
	page = htmlContent.get_text()

	pagestr = str(page)
	pagestr = pagestr.splitlines()

	slevel = 0 
	skarma = 0
	sacv = 0
	for lines in pagestr:
		
		
		if 'Network Level:' in lines:
			if slevel == 0:
				level1 = lines[15:]
				slevel = 1 
			lines = lines[15:]
			level = lines

			
		if 'Karma:' in lines:
			if skarma == 0:
				karma1 = lines[7:]
				skarma = 1 
			lines = lines[7:]
			karma = lines
		if 'Achievement Points:' in lines:
			if sacv == 0:
				acv_pts1 = lines[20:]
				sacv = 1 
			lines = lines[20:]
			acv_pts = lines
		if 'Name:' in lines:
			lines = lines[6:]
			g_name = lines

	url = 'https://sk1er.club/guild/player/' + ign
	response1 = requests.get(url, verify=False)
	htmlContent = BeautifulSoup(response1.content, "html.parser")
	page = htmlContent.get_text()
	pagestr = str(page)

	pagestr = pagestr.splitlines()

	for lines in pagestr:
		
		
		if 'Members:' in lines:
			lines = lines[9:]
			members = lines
		if 'Guild Level:' in lines:
			lines = lines[13:]
			g_level = lines

	try:
		level = int(level)
		karma = int(karma)
		acv_pts = int(acv_pts)
		karma = ''
		acv_pts = ''
	except:
		dumb = 1




	if karma1 == karma:
		karma = ''
	if acv_pts == acv_pts1:
		acv_pts = ''

	try:
		embed = discord.Embed(title='Ducc Bot 3.1', description=ign, color=0xeee657)
		embed.set_image(url=uuidurl)
		level1 = level1.strip()
		level1 = str(level1)
		level = str(level) 
		if level1 == level:
			level1 = " "
		embed.add_field(name="Player Level", value=str(level1)+"   " +str(level))
		embed.add_field(name="Player Karma", value=str(karma1)+"   " +str(karma))
		embed.add_field(name="Achievement Points", value=str(acv_pts1)+"   " + str(acv_pts))
		embed.add_field(name="Guild Name", value=g_name)
		embed.add_field(name="Guild Members", value=members)
		embed.add_field(name="Guild Level", value=g_level)
		embed.add_field(name="Join Our Server", value='https://discord.gg/uKJHQkw')
		embed.add_field(name="Donate To Keep Ducc Running", value='Join server for more information')
		await ctx.send(embed=embed)
	except:
		embed = discord.Embed(title='Ducc Bot 3.1', description=ign, color=0xeee657)
		embed.set_image(url=uuidurl)
		embed.add_field(name="Player Level", value=str(level1)+"   " +str(level))
		embed.add_field(name="Player Karma", value=str(karma1)+"   " +str(karma))
		embed.add_field(name="Achievement Points", value=str(acv_pts1)+"   " + str(acv_pts))
		embed.add_field(name="Guild Name", value=g_name)
		embed.add_field(name="Guild Members", value=members)
		embed.add_field(name="Guild Level", value=g_level)
		embed.add_field(name="Join Our Server", value='https://discord.gg/uKJHQkw')
		embed.add_field(name="Donate To Keep Ducc Running", value='Join server for more information')
		await ctx.send(embed=embed)

@bot.command()
async def breakbeak(ctx, user:discord.Member):
     if message.author.guild_permissions.administrator:
        muteRole = discord.utils.get(ctx.guild.roles,name="Muted")
        await user.add_roles(muteRole)
        embed=discord.Embed(title="User Muted!", description= ctx.message.author+ "broke" +user+"'s beak!", color=0xff00f6)
        await ctx.send(embed=embed)

@bot.command()
async def servercount(ctx):
	gc = 0
	g = ''
	guilds = bot.get_guild
	for guild in bot.guilds:
		
		g= guild.name
		if "Ducc Land" in g:

			gc = str(guild.member_count)

	embed=discord.Embed(title='Ducc Land', description= gc + " members", color=0xeee657)
	await ctx.send(embed=embed)
bot.run(TOKEN)







