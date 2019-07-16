<?php

	$filename = 'pic';
	date_default_timezone_set('UTC');
	$date = date("Y-m-d_H:i:s", substr("1549828094", 0, 10));
	$fin = $filename.$date.'.png';
	print 'Final filename: '.$fin;
	print '| MD5 format:'.md5($fin);

?>
