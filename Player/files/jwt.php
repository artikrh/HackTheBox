<?php
require 'vendor/autoload.php';
use \Firebase\JWT\JWT;

	$token_payload = [
	  'project' => 'PlayBuff',
	  'access_code' => '0E76658526655756207688271159624026011393' // qetu veq e ndrrova
	];
	$key = '_S0_R@nd0m_P@ss_';
	$jwt = JWT::encode($token_payload, base64_decode(strtr($key, '-_', '+/')), 'HS256');

	setcookie('access',$jwt, time() + (86400 * 30), "/");

	echo $jwt;
?>
