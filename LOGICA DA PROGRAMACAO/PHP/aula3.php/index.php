<?php
//2 arrays e vamois verificar os números em comum

$array_0 = array(0,1,3,4,6,8)
$array_1 = array(10,90,23,8,6)


//rodar um looping e verificar se existe em um e no outro.
$em_comum = [];
for($i = 0; $i < cont ($array_0); $i++){
    for($j = 0; $j < cont ($array_1); $n++){
        if($array_0[$i] == $array_1[$j]){
            $em_comum[] = $array_0[$i];
        }
    }
}

foreach ($em_comum as $key => $value){
    echo $value;
    echo '<br>';
}
?>
