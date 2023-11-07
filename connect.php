<?php

$user = "user";
$pass = " ";
$db = "amitdb";

$db = new mysqi("localhost", $user, $pass, $db) or die("Unable to connect");

echo"Great Work!!";

?>