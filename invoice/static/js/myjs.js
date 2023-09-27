$(document).ready(function(){
  $('#id_line_one_quantity, #id_line_one_unit_price').keyup(function(){
    var line_one_quantity_text = $('#id_line_one_quantity').val();
    var line_one_unit_price_text = $('#id_line_one_unit_price').val();
    var line_one_total = line_one_quantity_text * line_one_unit_price_text;

    var total = line_one_total;
    
    $('#id_line_one_total_price').val(line_one_total);
    $('#id_total').val(total);
});
});