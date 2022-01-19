
	var shipping = '{{order.shipping}}'
	var total = '{{order.get_cart_total|floatformat:2}}'
	var user = '{{request.user}}'




  	function submitFormData(){
 		console.log('Payment button clicked')
 		var userFormData =  {
 		'name':null,
 		'email':null,
 		'total':total,}
 		var shippingInfo = {
 		'address':null,
 		'city':null,
 		'state':null,
 		'zipcode':null,
 		}
 		if (shipping !='False'){
 			shippingInfo.address=form.address.value
 			shippingInfo.city=form.city.value
 			shippingInfo.state=form.state.value
 			shippingInfo.zipcode=form.zipcode.value
 		}
 		if (user == 'AnonymousUser'){
 			userFormData.name = form.name.value
 			userFormData.email = form.email.value
 		}


 	var url = '/process_order/'
    fetch(url, {
    method:'POST',
    headers:{
    'Content-Type':'application/json',
    'X-CSRFToken':csrftoken,
    },
    body:JSON.stringify({'form': userFormData,'shipping':shippingInfo})})

    .then((response) => {return response.json();})
    .then((data) => {
     console.log('Success:', data);
     alert('Transaction completed');
     location.href ='/';
     });}