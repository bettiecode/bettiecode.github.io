data=[]
with open("music/data/data_sheet.txt","r",encoding="utf-8") as inf:
    for line in inf:
        data.append(line.strip().split("; "))
print(data)

outf = open("music/music_list.html","w")

for dt in data:
    line="<div class='album'>\n"
    line+=f"<b>{dt[0]} - {dt[1]} ({dt[2]})</b>\n"
    line+="<div class='main_text'>\n"
    line+=dt[3]+"<br>\n"
    with open(f"music/data/{dt[4]}.txt") as f:
        line+=f.readline()+"<br>\n"
    line+="</div>\n"
    line+="</div>"

    outf.writelines(line)

outf.close()


