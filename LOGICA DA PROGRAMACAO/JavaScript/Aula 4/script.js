$(function(){

    function verificarTamanhoeAplicaCor(){
        var tamanhoTela = $(windows).width();
        if(tamanhoTela < 768){
            $('.header').css('background', 'blue');
        }else if(tamanhoTela < 1024){
           $('.header').css('background', 'green');
        }else{
            $('.header').css('background', 'red');
        }
    
        verificarTamanhoeAplicaCor
        setInterval(function(){
            verificarTamanhoeAplicaCor();
        },3000);

        $(window).resize(function(){
            verificarTamanhoeAplicaCor
        })
    }})