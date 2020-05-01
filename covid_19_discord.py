import discord
import requests

token = "" #token for discord bot

def get_data(country):
    """gets data for specific country through API and displays it
    """
    get_data = requests.get("https://coronavirus-19-api.herokuapp.com/countries/"+str(country)).json()
    return get_data

def run_bot():
    """Runs the bot
    """
    client = discord.Client()

    @client.event
    async def on_ready():
        """when bot is logged in display message in our console
        """    
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        """Displays country covid-19 statiscic in discord chat

        Arguments:
            message {string} -- let's you specify country
        """        
        if message.content.find("!covid") != -1:
            try:
                data = get_data(message.content.split(" ")[1])
                for x in data:
                    await message.channel.send('{} {}'.format(x, data[x]))
            except:
                await message.channel.send("No such cuntry")

    client.run(token)   

def main() :
    run_bot()

if __name__ == "__main__" :
    main()