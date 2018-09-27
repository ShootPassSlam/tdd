window.Superlists = {}; 
window.Superlists.initialize = function () { 
  $('input[name="text"]').on('propertychange change click keyup input paste', function () {
    $('.has-error').hide();
  });
  $('input[name="text"]').click(function () {
    $('.has-error').hide();
  });
};