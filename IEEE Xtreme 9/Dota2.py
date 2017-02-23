from operator import itemgetter

characters = open("Dota2.txt",'r')
import math
#Create matrix with each hero stats and rank
x = characters.readline().split()
n = int(x[0])
top = int(x[1])
heroes = []
agi = stre = intel = 0 
#Create list of dicts with each one being: NAme,Affinity,WR (w/w+r),
lines = characters.readlines()
for i in range(0,len(lines)):
	hero = lines[i].split(",")
	winlose = hero[2].split(":")
	winrate = float(winlose[0])/(float(winlose[0])+float(winlose[1].rstrip()))
	winrate = (round(winrate*100))
	hero_stats = {
    	"Name": hero[0],
        "Winrate": winrate,
        "Affinity": hero[1],
        "Popularity": i+1,
        "Overall": winrate*(i+1)
      }
	heroes.append(hero_stats)
for i in range(0,len(heroes)):
	sorted_heroes = sorted(heroes,key=itemgetter('Overall'),reverse=True)
for i in range(0,top):
	print sorted_heroes[i]['Affinity']
	if sorted_heroes[i]['Affinity']=='Intelligence':
		intel+=1
	if sorted_heroes[i]['Affinity']=='Strength':
		stre+=1
	if sorted_heroes[i]['Affinity']=='Agility':
		agi+=1
fmt = "{0:.2f}"
agi_pct = fmt.format((float(agi)/top)*100)
str_pct = fmt.format((float(stre)/top)*100)
int_pct = fmt.format((float(intel)/top)*100)
print agi_pct,str_pct,int_pct