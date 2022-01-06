import discord
import time
import random
from discord import message
from discord import client
from discord.colour import Colour
from discord.embeds import Embed

timer_num = []
goal_num = []
activity_counter = []
activity_status = []
activity_list = ['Sit-Ups', 'Squats', 'Push-Ups', 'Jumping Jacks', 'Crunches', 'Lunges', 'Burpees', 'Leg Raises', 'Calf Raises', 'Russian Twists']
rep_list = [10, 15, 20, 25, 30, 35, 40, 45, 50]

client = discord.Client()

@client.event
async def on_ready():
    print('GamerFit is warmed up!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    elif message.content[0:9] == 'set timer':
        if ((message.content[-2:]).isdigit() == True) and (int(message.content[-2:]) != 0):
            await message.channel.send('Your activity timer has been set.')
            x = int(message.content[-2:]) * 6
            timer_num.append(x)
        else:
            await message.channel.send("To set your activity timer, type the following command with your desired number of minutes: 'set timer ##'.")
    
    elif message.content[0:8] == 'set goal':
        if ((message.content[-2:]).isdigit() == True) and (int(message.content[-2:]) != 0):
            await message.channel.send('Your activity goal has been set.')
            y = int(message.content[-2:])
            goal_num.append(y)
        else:
            await message.channel.send("To set your activity goal, type the following command with your desired goal number: 'set timer ##'.")
    
    elif message.content == 'activity status':
        if activity_counter == []:
            activity_status.append("You haven't completed any activity sessions yet, so let's get started!")
            embed = discord.Embed(
                title = 'Activity Status',
                description = activity_status[-1],
                colour = discord.Colour.dark_blue()
            )
    
            await message.channel.send(embed = embed)
        else:
            activity_counter != []
            if activity_counter[-1] < goal_num[-1]:
                activity_status.append("You have completed " + str(activity_counter[-1]) + " activity session(s), well done!")
                embed = discord.Embed(
                    title = 'Activity Status',
                    description = activity_status[-1],
                    colour = discord.Colour.dark_blue()
                )
    
                await message.channel.send(embed = embed)
            else:
                activity_counter[-1] >= goal_num[-1]
                activity_status.append("You have completed " + str(activity_counter[-1]) + " activity session(s), and you have reached your activity goal!")
                embed = discord.Embed(
                    title = 'Activity Status',
                    description = activity_status[-1],
                    colour = discord.Colour.dark_blue()
                )
    
                await message.channel.send(embed = embed)
        
    elif message.content == 'ready to game':
        if (timer_num != [0] and goal_num != [0]) and (timer_num != [] and goal_num != []):
            await message.channel.send('The timer has been started. Have fun!')
            activity_count = 0
            for i in range(goal_num[0]):
                activity_count += 1
                activity_counter.append(activity_count)
                x = random.randrange(0,9)
                y = random.randrange(0,10)
                time.sleep(timer_num[0])
                await message.channel.send("Hey <@" + str(message.author.id) + ">, it's time to start your activity!            Suggested Activity: " + activity_list[y] + "    Repititions: " + str(rep_list[x]))


        else:
            if timer_num == [] and goal_num == []:
                await message.channel.send("Hold up gamer! Don't forget to set your activity timer and activity goal.")
            elif timer_num == [] and goal_num != []:
                await message.channel.send("Slow down there! Don't forget to set your activity timer.")
            elif goal_num == [] and timer_num != []:
                await message.channel.send("Slow down there! Don't forget to set your activity goal.")

client.run('OTI3OTg3ODQwODM3NjMyMDkw.YdSOBg.KDXHob91GsWyhqS41sSA0M-kHzU')