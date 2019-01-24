/* This function to fill all type=number with #inbox value
   when #chkParent is checked */
$(document).on( 'input', '#inbox', function ()
{
	function updateTime() {
		if ($("#chkParent").prop("checked")) {
			var timeinbox = parseInt($("#inbox").val());
			$('#tblData tr:has(td)').find('input[type="number"]').val(timeinbox);
		}
	}
	$(document).on("change keyup", "#inbox", updateTime);
});


/* This function to check all  type="checkbox" when
   #chkParent is checked */
$(document).on( 'click', '#chkParent', function () {
    var isChecked = $(this).prop("checked");
    $('#tblData tr:has(td)').find('input[type="checkbox"]').prop('checked', isChecked);

    $(this).closest("table").find("input[type='number']").not(this).prop("disabled", !isChecked);

  $('#tblData tr:has(td)').find('input[type="checkbox"]').click(function() {
    var isChecked = $(this).prop("checked");
    var isHeaderChecked = $("#chkParent").prop("checked");
    if (isChecked == false && isHeaderChecked)
      $("#chkParent").prop('checked', isChecked);
    else {
      $('#tblData tr:has(td)').find('input[type="checkbox"]').each(function() {
        if ($(this).prop("checked") == false)
          isChecked = false;
      });
      console.log(isChecked);
      $("#chkParent").prop('checked', isChecked);

    }
  });
});


  $(document).on("change","table input[type='checkbox']", function(){
    $(this).closest("tr").find("input[type='number']").not(this).prop("disabled", !this.checked);
});

