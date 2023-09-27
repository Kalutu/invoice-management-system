$(document).ready(function(){
  $('#id_quantity, #id_unit_price').keyup(function(){
    var quantity = $('#id_quantity').val();
    var unit_price = $('#id_unit_price').val();

    var total_price = quantity * unit_price;

    $('#id_total_price').val(total_price);
});
});