function myfun()
{

var squ=document.querySelectorAll(".square");
// alert(squ.length);
for(var i=0;i<squ.length;i++)
{
	 var lm=kiss();
	 squ[i].style.backgroundColor="rgb("+lm[0]+","+lm[1]+","+lm[2]+")";
	function kiss()
	{
		var l=[];
		for(var j=0;j<3;j++)
		{
			l.push(Math.round((Math.random()*1000)%255));
		}
		return l;
	}

}
}