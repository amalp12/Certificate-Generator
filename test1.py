from PIL import Image, ImageDraw, ImageFont
import json
"""
Name ,college, event, prize
"""

#Getting Data from json files Start
eventsFile = open("events.json")
usersFile = open("users.json")

eventsData = eventsFile.read()
usersData = usersFile.read()

events = json.loads(eventsData)
users = json.loads(usersData)

eventsDict ={} #index with EventId
for i in events:
    eventsDict[i["id"]]= i["name"] 

usersDict ={}#index with useriId
for i in users:
    usersDict[i["id"]]= [i["name"] ,i["college"]]

"""
events = {"id_no: "name"}
users = {"id_no":["name", "college"]}
"""
#end


#opening image start and setting font start
image = Image.open('img/certificateTemplate.jpg')
draw = ImageDraw.Draw(image)
myFont = ImageFont.truetype("arial.ttf",50)
#end

"""
url = "yoursite.com/teamId=123&userId=456" #get teamID from this url
teamId = 
result = results[teamid]
pos =result["position"]
"""
#we should have teamId and position from the url
eventId =12
teamId = 123
pos ="1"

name= usersDict[teamId][0]
college= usersDict[teamId][1]
event= eventsDict[eventId]
prize= pos

coor_name= 300,1000
coor_college= 300,900
coor_event= 300,800
coor_prize= 300,600


draw.text(coor_name,name , "black", font= myFont)
draw.text(coor_college,college , "black", font= myFont)
draw.text(coor_event, event , "black", font= myFont)
draw.text(coor_prize,prize , "black", font= myFont)
image.show()