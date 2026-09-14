$(function() {
    $('.pai .filho').each(function() {
        var obj = $(this).find('.filho-do-filho');
        if(obj.length > 0){
            if(obj.hasClass('animar')){
                obj.animate({width:'100px'}, 3000, function(){
                    console.log("Terminamos nossa lógica");
                });
            }
        }
    });
});