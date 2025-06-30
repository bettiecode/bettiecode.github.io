let ids=["index","diary","anime","code"]
let titles=["home","diary","animanga","music","programming"]
function makeRow()
{
    var row = document.getElementById("slctrow")
    row.innerHTML=""
    for(let i=0;i<ids.length; i++)
        {
            row.innerHTML+="<th class=\"slctcell\"><button class=\"slctbttn\" onclick=\"setCurrent(id)\" id=\""+ids[i]+"\">"+titles [i]+"</button></th>"
        }
}
function setCurrent(a)
{
    window.location.href=a+".html"
}
function decorate(a)
{
    document.getElementById(a).innerHTML=" &#9830 "+document.getElementById(a).innerHTML
}
makeRow()


