const bd = new Date("2000-02-08"); 
const cd = new Date(); 

if((cd.getMonth()==bd.getMonth)&(cd.getDate()==bd.getDate()))
{
    document.getElementById("date").innerHTML += "my birthday!!!";
} else 
{
    document.getElementById("date").innerHTML += "not my birthday...";
}