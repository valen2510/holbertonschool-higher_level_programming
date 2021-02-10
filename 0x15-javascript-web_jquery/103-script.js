$('document').ready(function () {
  const langHello = val => {
    $.get(`https://fourtonfish.com/hellosalut/?lang=${val}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  };

  $('INPUT#btn_translate').click(() => {
    const value = $('INPUT#language_code').val();
    langHello(value);
  });
  $('INPUT#language_code').keypress(event => {
    if (event.keyCode === 13) {
      const value = $('INPUT#language_code').val();
      langHello(value);
    }
  });
});
