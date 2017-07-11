<?php 
$ip = $_SERVER['REMOTE_ADDR']; //ip of the user
$date = date("d-m-y"); //date when the user visited
$time = date("H:i:s"); //time when the user visited
$browser = $_SERVER['HTTP_USER_AGENT']; //browser user agent
$hrefa=$_SERVER['HTTP_REFERER']; //where the user was refeered to your site
$arr=array('IP' => $ip, 'Date' => $date, 'Time' => $time, 'Browser' => $browser,'ip reference' => $hrefa);
print_r($arr);
?> 
