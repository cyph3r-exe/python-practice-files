import discord
import os 

client = discord.Client()

@client.event
async def on_ready():
    print("We've logged in")

#helping out content 
help = """This is the official bot for all Z3NITH'22
It'll be providing you with all the information you need for any particular event. 
You can try out the following commands 
Prefix is **$**

`$website` = Link to website 
`$brochure` = Link to Brochure
`$socials` = Link to all our socials 
`$gaming` = Gaming Valo, Valo idhar hai  
`$photoshop` = Cafe News-Latte: At your Inbox!
`$film` = Sk-EaT
`$cryptic`= Cryptic Hunt: Tagline
`$meme` = Now Meme-ing: Test your Expertise
`$hackx` = HackX. CodeX. BuildX : Skill it! Build it! Kill it!
"""

#Gaming Content 
gaming = """Mode: LIVE@Discord | 1000 IST Onwards, 6th-7th August
Class: 9-12   
Game: Valorant ()
Participants: A Team Comprising of 5+1 Members

**Software Requirements**
Windows 7/8/10 64-bit
Ram 4GB
VRAM 1GB
**Recommended Specs**
-> CPU: Intel i3-4150 
-> GPU: Geforce GT 730
-> 16 Teams will be registered on a “first-come, first-served” basis.
-> All matches except the finals will be knockouts. The finals would be the best of 3.
-> The discord server link has been given in the general guidelines. Only the registered participants would get the access to the gaming channel after verification. Participants are requested to join the server at least one day prior to the event with their real names.
-> The matches will go on for 2 days but the schedules of the tournament will be laid out in advance on the Discord Server itself. 
-> Any kind of hack/aimbot is strictly prohibited.And will be punished for the same. (PS: We don't believe in Vangaurd) 

Event Coordinator:  <@819247258830241837> and <@773540030823661568> 
"""

#Website command info 
website = "Link to Website : "

#brochure command info
brochure = "Link to Brochure : "

#Opening video 
video = "Link to Opening Video : "  

#socials 
socials = "Link to socials : "

#cryptic hunt 
cryptic = """
Mode: LIVE@??? | 1000 IST Onwards, 6th-7th August
Class: 9-12
Participants: A Team Comprising of 2 Members

An online cryptic hunt where participants will be pitted against each other in a race to decrypt the hints and clues.
The event will commence on 6th August at 1000 IST and will 2200 IST. 
The hunt would cover themes of pop culture, current affairs and tech events. 
Questions will be released on the discord server every 2 hours ( 10 - 12-2-4-6-8)
It is mandatory for participants to join the server. <DM Answers???> 
(Testing GooseChase/website thingy)
Points will be awarded based on the time taken to answer and be displayed on a public leaderboard, which will update every 2 hrs
Clues / hints will also be posted on the server itself. Participants can also ask for additional, exclusive hints at a cost of points. These will be announced on the discord server before the commencement of the event.
Any of the participants, if found sharing answers or exclusive hints online will be immediately disqualified.

Event Coordinator: Abhinav Mishra, +91 9958310261

Team - 3 members - 
"""

#photoshop event details
photoshop = """
Mode: Submission
Software: Adobe Photoshop.
Class: 9-10
Participants: A Team Comprising of 2 Members

-> The team of participants have to design an email newsletter on any one of the above listed topics:
-> A Marketing Email from newly launched H&M Home India
-> A Mental Health Newsletter
-> A College Brochure in the form of a newsletter
-> Participants have to upload the design in both .psd and .jpeg/.png format into a  Google Drive folder in the email and send the link to the official email address, futurz.afgji@gmail.com. Please make sure that the .psd file is in its raw state and the layers have not been merged.
-> Please make sure the Drive folder is ACCESSIBLE TO EVERYONE.
-> The width of the email newsletter should be 600 pixels while the height of the newsletter is left to the student’s choice. 
-> Use of third-party design platforms like Canva is strictly prohibited. 
-> The Submission Deadline is 1900 IST, 30th July. Please read the General Guidelines for more details.
-> Judgement Criteria: Aesthetics, Template Design, Creativity, Content.

Event Coordinator: Soumil, +91 9999448903

"""
#meme event detaisl 
meme = """
Mode: Submission | IST Onwards, 5th August
Class: 6-8
Participants: Individual

-> Participants would be given three topics at different times through the event WhatsApp group on 5th August and they have to make a meme in any format on the given topic. 
-> Participants can use any software to create the meme.
-> Memes can be submitted in .jpeg, .png or .mp4 formats.
-> The duration for a meme in .mp4 format should be between 3-10 seconds.
-> The event will last for 10 hours and consist of 3 topics with the first topic being announced on <date, time> and a new topic being announced every 2 hours until the announcement of the 3rd topic on <time>.
-> Participants would have 30 minutes at hand from the announcement of the topic to make and 10 mins to submit the meme. Late submissions will not be accepted.
-> Please read the General Guidelines for more details. Google Form for this event???
-> The jury would be eliminating participants after every round.
-> Judgement Criteria: Creativity, Relevance

Event Coordinator: Arnav Sood , +91 99718 54653
"""

#film event details 
film = """
Mode: Submission 
Class: 9-10
Participants: A Team Comprising of 3 Members

-> Participants would have to create a skit/sketch comedy based on any of the listed themes:
A. What matters more: hard work or luck?
B. Does Money bring happiness? 
C. Is Sex Education Necessary?
-> The skit/sketch should be portrayed in a humorous and/or satirical way conveying the message the team has chosen.
-> The listed themes are open-ended questions and participants are free to interpret the topic in any manner. 
-> Participants can use any watermark-free software to create the video but the voiceover (if any) should be of the participants and is not to be computerised.
-> The duration of the video should be 3-4 minutes.
-> Participants have to upload the movie in .mp4 format on YouTube and send the link of unlisted video to the official email address, futurz.afgji@gmail.com. Please title the video as: Your School Name, Branch | Event Name. For instance,
-> Air Force Golden Jubilee Institute, Subroto Park | Sk-EaT
-> The Submission Deadline is 1900 IST, 30th July. Please read the general guidelines for more details.
-> Judgement Criteria: Originality, Creativity, Content, Relevance to Theme, Time Adherence, Overall Impact

Event Coordinator: Sougata Garai, +91 

"""

#word event details 
word = """
Mode: Submission 
Class: 3-5
Participants: Individual

-> The participants would be provided with a cuisine as well as assets at 1000 IST, 25th July and they have to accordingly design a restaurant brochure menu in Microsoft Word.
-> The document should not exceed more than 3 pages.
-> Participants have to upload the design in ..docx format on Google Drive and send the link to the official email address, futurz.afgji@gmail.com. 
-> The usage of assets other than the ones provided is strictly prohibited.
-> The use of templates is also prohibited but you can take the help of the internet for design inspirations. 
-> Use of third-party design platforms like Canva is strictly prohibited. 
-> The Submission Deadline is 1900 IST, 31st July. Please read the General Guidelines for more details.
-> Judgement Criteria: Creativity, Aesthetics, Use of Resources, Relevance to Theme, Overall Presentation

Event Coordinator: <@752118247494516766> 
"""

#hackx event details 
hackx = """
Mode: LIVE@Discord | 1000 IST, 6th August - 1000 IST, 7th August
Duration: 24 hours
Class: 9-12
Participants: A Team Comprising of 4 Members
"""

#bot code 
@client.event
async def on_message(message):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name ="$help"))

    if message.author == client.user:
        return

    elif message.content.startswith('$hello'):
        await message.channel.send('Hello there!')

    elif message.content.startswith('$help'):
        await message.channel.send(help)

    elif message.content.startswith('$website'):
        await message.channel.send(website)
    
    elif message.content.startswith('$brochure'):
        await message.channel.send(brochure)

    elif message.content.startswith('$gaming'):
        await message.channel.send(gaming)
    
    elif message.content.startswith('$socials'):
        await message.channel.send(socials)

    elif message.content.startswith('$photoshop'):
        await message.channel.send(photoshop)
    
    elif message.content.startswith('$meme'):
        await message.channel.send(meme)
    
    elif message.content.startswith('$word'):
        await message.channel.send(word)
    
    elif message.content.startswith('$film'):
        await message.channel.send(film)
    
    elif message.content.startswith('$hackx'):
        await message.channel.send(hackx)

    elif message.content.startswith('$cryptic'):
        await message.channel.send(cryptic)
    
client.run()