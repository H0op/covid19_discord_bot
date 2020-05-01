Welcome to covid-19-discord's documentation!
==========================================

Using an API for covid-19 data and discord access to send us updates for COVID-19 cases

python
discord account
create a discord server
add bot to discord server by oauth2 in https://discordapp.com/developers/applications -> create application -> bot -> add bot -> 
give it atleast 207872 permission

get the bot token and place it in variable token= inside covid_19_discord.py

invite the bot to your channel https://discordapp.com/api/oauth2/authorize?client_id=<ID_HERE>&permissions=207872&scope=bot
# Replace ID_HERE with the client ID from developers/application

requirements to run:
pip install -U discord.py
pip install pandas
pip install requests