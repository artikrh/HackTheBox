<?php session_start(); if (!isset ($_SESSION['username'])) { header("Location: /login.php"); }; if ( strpos($_SERVER['REQUEST_URI'], '/addons/') !== false ) { die(); };
# OneTwoSeven Admin Plugin
# OTS Users
echo shell_exec("/bin/grep ^ots- /etc/passwd | /usr/bin/cut -d: -f1,5 | /bin/sed -e 's,:, (,' -e 's,$,),' ");
?>
