<?php session_start(); if (!isset ($_SESSION['username'])) { header("Location: /login.php"); }; if ( strpos($_SERVER['REQUEST_URI'], '/addons/') !== false ) { die(); };
# OneTwoSeven Admin Plugin
# OTS Addon Manager
switch (true) {
	# Upload addon to addons folder.
	case preg_match('/\/addon-upload.php/',$_SERVER['REQUEST_URI']):
		if(isset($_FILES['addon'])){
			$errors= array();
			$file_name = basename($_FILES['addon']['name']);
			$file_size =$_FILES['addon']['size'];
			$file_tmp =$_FILES['addon']['tmp_name'];

			if($file_size > 20000){
				$errors[]='Module too big for addon manager. Please upload manually.';
			}

			if(empty($errors)==true) {
				move_uploaded_file($file_tmp,$file_name);
				header("Location: /menu.php");
				header("Content-Type: text/plain");
				echo "File uploaded successfull.y";
			} else {
				header("Location: /menu.php");
				header("Content-Type: text/plain");
				echo "Error uploading the file: ";
				print_r($errors);
			}
		}
		break;
	# Download addon from addons folder.
	case preg_match('/\/addon-download.php/',$_SERVER['REQUEST_URI']):
		if ($_GET['addon']) {
			$addon_file = basename($_GET['addon']);
			if ( file_exists($addon_file) ) {
				header("Content-Disposition: attachment; filename=$addon_file");
				header("Content-Type: text/plain");
				readfile($addon_file);
			} else {
				header($_SERVER["SERVER_PROTOCOL"]." 404 Not Found", true, 404);
				die();
			}
		}
		break;
	default:
		echo "The addon manager must not be executed directly but only via<br>";
		echo "the provided RewriteRules:<br><hr>";
		echo "RewriteEngine On<br>";
		echo "RewriteRule ^addon-upload.php   addons/ots-man-addon.php [L]<br>";
		echo "RewriteRule ^addon-download.php addons/ots-man-addon.php [L]<br><hr>";
		echo "By commenting individual RewriteRules you can disable single<br>";
		echo "features (i.e. for security reasons)<br><br>";
		echo "<font size='-2'>Please note: Disabling a feature through htaccess leads to 404 errors for now.</font>";
		break;
}
?>
