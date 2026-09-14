<?php
//2 arrays e vamois verificar os números em comum

$array = array('Guilherme','Joao','Lucas','Guilherme','Matheus','Guestavo','Guilherme','Joao','Lucas','Guilherme','Matheus','Guestavo','Guilherme','Joao','Lucas','Guilherme','Matheus','Guestavo','Guilherme','Joao','Lucas','Guilherme','Matheus','Guestavo','Guilherme','Joao','Lucas','Guilherme','Matheus','Guestavo')

$arrayRepetido = array();

for($i = 0; $i < count($array);$i++){
    $valorAtual = $array[$i];
    if(!isset($arrayRepetido[$valorAtual])){
        $arrayRepetido[$valorAtual] = 0;
    }else{
        $arrayRepetido[$valorAtual]++;
    }

}

foreach($arrayRepetido as $key => $value) {
    echo $key;
    echo $value;
    echo '<br>';
}
?>
