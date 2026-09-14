<?php
    $arr = [];

    for($i = 0; $i < 5; $i++){
        $arr[$i] = rand(1,20);
        while(in_arrayCustom($i,$arr[$i], $arr)){
            $arr[$i] = rand(1,20);
        }

    }
    function in_arrayCustom($indice,$value, $arr){
        for($i = 0; $i < count($arr); $i++){
            if($i != $indice && $arr[$i] == $value){
                return true;
            }
        }
        return false;
    }
?>
