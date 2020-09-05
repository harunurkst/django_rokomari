
function delete_cart_item(cart_id) {
       console.log(cart_id)
       var apiUrl = '/api/remove-cart-item/'+cart_id;

       $.ajax({
            url: apiUrl,
            method: 'GET',
            success: function(result){
                var div_id = "item_"+cart_id;
                $("#"+div_id).remove();
            }
       })
}