var add_cart=document.getElementsByClassName("update-cart");
for(var i=0;i<add_cart.length;i++)
{
	add_cart[i].addEventListener("click",function(){
		var productid=this.dataset.product;
		var action=this.dataset.action;
		if(user=="AnonymousUser"){
			alert("Not logged in");
		}
		else
		{
			updatecart(productid,action);
		}

	});
}

function updatecart(productid,action)
{
	
	var url="/add_cart/";
	fetch(url,{
		method:"POST",
		credentials:'same-origin',
		headers:{
			'Content-Type': 'application/json',
			'X-CSRFToken':csrftoken
		},
		body:JSON.stringify({'productId':productid,'action':action})
	})
	.then((response)=>{
		return response.json()
	})
	.then((data)=>{
		location.reload()
		alert(data);
	})
}