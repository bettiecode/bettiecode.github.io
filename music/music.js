let dat=[]

function readTextFile(file) {
  var rawFile = new XMLHttpRequest();
  rawFile.open("GET", file, false);
  rawFile.onreadystatechange = function () {
    if(rawFile.readyState === 4)  {
      if(rawFile.status === 200 || rawFile.status == 0) {
        var allText = rawFile.responseText;
        console.log(allText);
       }
    }
  }
  rawFile.send(null);
}

readTextFile("music/test.txt")
/*
fetch("music/test.txt")
  .then((res) => res.text())
  .then((text) => {
    dat.push(text)
   })
  .catch((e) => console.error(e));
*/
let c = document.getElementById("content");
let t = 0;
let elem=""


for(var i=0;i<dat.length;i++)
    {
        elem=""
        elem+="<div class='main_box'>"
        elem+=dat[i]
        elem+="</div>"

        c.innerHTML+=elem
    }



