<?php
$db_connection = pg_connect("host=localhost dbname=profiles user=profiles password=profiles");
$result = pg_query($db_connection, "SELECT * FROM profiles");
while ($row = pg_fetch_row($result)) {
  var_dump($row);
}
?>
