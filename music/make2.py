albums=[]

class Song:
    def __init__(self,title,duration,notes):
        self.title=title
        self.duration=duration
        self.notes=notes    

class Album:
    def __init__(self,title,artist,release,rating,cover,link,notes,songs):
        self.title=title
        self.artist=artist
        self.release=release
        self.notes=notes  
        self.rating=rating
        self.cover=cover
        self.link=link
        self.songs=songs 

files=[]
with open("music/data/data_sheet.txt","r") as f:
    files=f.readlines()

for file in files:
    with open("music/data/"+file.strip()+".txt","r",encoding="utf-8") as g:
        album=g.readlines()
    songs=[]
    for i in range(7,len(album)-1,3):
        songs.append(Song(album[i],album[i+1],album[i+2]))
    albums.append(Album(album[0],album[1],album[2],album[3],album[4],album[5],album[6],songs))

out=""
for alb in albums:
    out+="<div class='album'>\n"
    out+=f"<img src='{alb.cover}'>\n"
    out+="<div class='title'>\n"
    out+=f"<a href='{alb.link}'>{alb.title}</a><br>\n"
    out+=f"-{alb.artist} * ({alb.release})\n"
    out+="</div>\n"
    out+="<div class='rating'>\n"
    out+=f"{alb.rating}/10\n "
    out+="</div>\n"
    out+="<div class='main'>\n"
    out+=alb.notes+'\n'
    out+="</div>\n"
    out+="<div class='songs'>\n"
    out+="<ul\n>"
    for sng in alb.songs:
        out+="<li>\n"
        out+=f"<p>{sng.title} - ({sng.duration})</p><br>\n"
        out+=sng.notes+"\n"
        out+="</li>\n"
    out+="</ul>\n"
    out+="</div>\n"
    out+="</div>\n"

with open("music/music_list.html","w") as outf:
    outf.write(out)


