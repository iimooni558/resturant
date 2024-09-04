function add_to_cart(id)
{
    var cart=document.getElementById('cart')
    var ajaxurl="/add_to_cart/";
    $.ajax({
        headers: { "X-CSRF-TOKEN": $('meta[name="csrf-token"]').attr("content") },
        url:ajaxurl,
        data:{id:id},
        method:"post",
        success:function(response){
           cart.innerHTML=response.count
           swal.fire({
                position: "top-end",
                icon: "success",
                title: "تم الاضافة للسلة بنجاح",
                showConfirmButton:false,
                timer:1500

        });

        }
});
}

$(document).ready(function() {
    $('#search-button').click(function() {
      var searchQuery = $('#search-input').val();
      $.ajax({
        url: '{% url "search_products" %}',
        type: 'GET',
        data: { query: searchQuery },
        success: function(response) {
          $('#search-results').html(response.results);
        }
      });
    });
  });