<?php session_start(); if (!isset ($_SESSION['username'])) { header("Location: /login.php"); }; if ( strpos($_SERVER['REQUEST_URI'], '/addons/') !== false ) { die(); };
# OneTwoSeven Admin Plugin
# OTS Default User
function username() { $ip = '127.0.0.1'; return "ots-" . substr(str_replace('=','',base64_encode(substr(md5($ip),0,8))),3); }
function password() { $ip = '127.0.0.1'; return substr(md5($ip),0,8); }
echo "<h4>Default User Credentials</h4><br>";
echo "<b>Username:</b> ",username(),"<br>";
echo "<b>Password:</b> ",password(),"<br>";
?>
