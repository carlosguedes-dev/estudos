<?php
//1) Verificar se tem mais de 5 letras
//2) Se é numero
//3) Se possui o @

if(isset($_POST['acao'])){
    $nome = $_POST['Nome'];
    $numero = $_POST['numero'];
    $email = $_POST['email'];
    if(strlen($nome) >=5){
        echo 'O nome é valido';
        echo '<br>';
    }
    if (is_numeric($numero)){
        echo 'O numero é valido';
        echo '<br>';
    }
    if (strstr($email, '@')) {
        echo 'O email é valido';
        echo '<br>';
        if(strstr($email, '@')){
            echo 'O email é gmail';
            echo '<br>';
            
            
        }

    }
}
    

?>
<form action="" method="post">
    <input type="text" name="Nome" id="">
    <input type="text" name="numero" id="">
    <input type="text" name="email" id="">
    <input type="submit" value="Enviar">
</form>
