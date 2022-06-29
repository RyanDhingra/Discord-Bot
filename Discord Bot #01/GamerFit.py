import discord
import random
import requests
from discord import message
from discord import client
from discord.colour import Colour
from discord.embeds import Embed
import asyncio

timer_num = 0
goal_num = 0
activity_counter = 0
total_activities = 0
activity_status = []
activity_list = ['Sit-Ups', 'Squats', 'Push-Ups', 'Jumping Jacks', 'Crunches', 'Lunges', 'Burpees', 'Leg Raises', 'Calf Raises', 'Russian Twists']
rep_list = [10, 15, 20, 25, 30, 35, 40, 45, 50]

client = discord.Client()

@client.event
async def on_ready():
    print('GamerFit is warmed up!')

@client.event
async def on_message(message):
    global timer_num, goal_num, activity_counter, total_activities

    if message.author == client.user:
        return
    
    elif message.content[0:9] == 'set timer':
        if ((message.content[-2:]).isdigit() == True) and (int(message.content[-2:]) != 0):
            await message.channel.send('Your activity timer has been set.')
            timer_num = int(message.content[-2:]) * 60
        else:
            await message.channel.send("To set your activity timer, type the following command with your desired number of minutes: 'set timer ##'.")
    
    elif message.content[0:8] == 'set goal':
        if ((message.content[-2:]).isdigit() == True) and (int(message.content[-2:]) != 0):
            await message.channel.send('Your activity goal has been set.')
            goal_num = int(message.content[-2:])
        else:
            await message.channel.send("To set your activity goal, type the following command with your desired goal number: 'set timer ##'.")
    
    elif message.content == 'activity status':
        if activity_counter == 0:
            activity_status.append("You haven't completed any activity sessions yet, so let's get started!")
            embed = discord.Embed(
                title = 'Activity Status',
                description = activity_status[-1],
                colour = discord.Colour.dark_blue()
            )
    
            await message.channel.send(embed = embed)
        else:
            activity_counter != 0
            if activity_counter < total_activities:
                activity_status.append("You have completed " + str(activity_counter) + " activity session(s), well done!")
                embed = discord.Embed(
                    title = 'Activity Status',
                    description = activity_status[-1],
                    colour = discord.Colour.dark_blue()
                )
    
                await message.channel.send(embed = embed)
            else:
                activity_counter == total_activities
                activity_status.append("You have completed " + str(activity_counter) + " activity session(s), and you have reached your activity goal!")
                embed = discord.Embed(
                    title = 'Activity Status',
                    description = activity_status[-1],
                    colour = discord.Colour.dark_blue()
                )

                await message.channel.send(embed = embed)
        
    elif message.content == 'ready to game':
        if (timer_num != 0)and  (goal_num != 0):
            await message.channel.send('The timer has been started. Have fun!')
            total_activities += goal_num
            for i in range(goal_num):
                x = random.randrange(0,9)
                y = random.randrange(0,10)
                await asyncio.sleep(timer_num)
                await message.channel.send("Hey <@" + str(message.author.id) + ">, it's time to start your activity!            Suggested Activity: " + activity_list[y] + "    Repititions: " + str(rep_list[x]))
                activity_counter += 1

        else:
            if timer_num == 0 and goal_num == 0:
                await message.channel.send("Hold up gamer! Don't forget to set your activity timer and activity goal.")
            elif timer_num == 0 and goal_num != 0:
                await message.channel.send("Slow down there! Don't forget to set your activity timer.")
            elif goal_num == 0 and timer_num != 0:
                await message.channel.send("Slow down there! Don't forget to set your activity goal.")
    
    elif message.content.lower() == 'motivation':
        x = random.randrange(0,300)
        quote = requests.get("https://type.fit/api/quotes")
        response = quote.json()
        await message.channel.send(response[x]["text"])

    elif message.content.lower() == '>help':
        embed = discord.Embed(
                    title = 'GamerFit Help Menu',
                    description = "This is a list of the commands to help you use GamerFit and all its awesome features!",
                    colour = discord.Colour.dark_blue()
        )
        embed.add_field(name = '1. Set Timer 00', value = 'Use this command to set your timer with your timer number.', inline = False)
        embed.add_field(name = '2. Set Goal 00', value = 'Use this command to set your goal with your goal number.', inline = False)
        embed.add_field(name = '3. Ready To Game', value = 'Use this command to start your timer, and begin to game away!', inline = False)
        embed.add_field(name = '4. Activity Status', value = 'Use this command to check your current activity status.', inline = False)
        embed.add_field(name = '5. Motivation', value = 'Use this command to get some fitness motivation!', inline = False)
        await message.channel.send(embed = embed)
        
client.run(TOKEN)
