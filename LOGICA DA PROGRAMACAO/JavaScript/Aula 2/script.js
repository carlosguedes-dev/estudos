$(function() {
    var index =
    $('.pai .filho').each(function() {
        if(index%2 == 0){
            $(this).css('background','red');
        }
        index++;        

    })
    console.log(index)
})