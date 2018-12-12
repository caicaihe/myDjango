$(function () {
  // Handle create environment
  $("#newEnvConfirmBtn").click(function () {
    data = $("#newEnvForm").serializeArray().reduce(function (obj, item) {
      obj[item.name] = item.value;
      return obj;
    }, {});

    $.post("/environments", data, function(resp) {
      if (resp == 'ok') {
        console.log('New environment added successfully~');
      }
      $('#addNewEnvDialog').modal('hide');
    });
  });

  $("#envTable").on('click', 'tr', function() {
    $(this).toggleClass('selected');
  });

  // Handle delete environment
  $('#removeEnvBtn').click(function() {
    $("#envTable .selected").each(function() {
      console.log('to delete ' + $(this).data('name'));
      $.ajax({
        url: "/environments/"+$(this).data('name'),
        type: 'DELETE',
      }).done(function(resp){
        console.log(resp);
      });
    }).remove();
  });
});