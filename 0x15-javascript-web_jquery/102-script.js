$('document').ready(function () {
  $('INPUT#btn_translate').click(() => {
    const value = $('INPUT#language_code').val();
    $.get(`https://fourtonfish.com/hellosalut/?lang=${value}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
