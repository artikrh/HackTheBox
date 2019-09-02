<?php if ( $_SERVER['SERVER_PORT'] != 60080 ) { die(); } ?>
<?php session_start(); if (!isset ($_SESSION['username'])) { header("Location: /login.php"); } ?>
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Jekyll v3.8.5">
    <title>OneTwoSeven - Administation</title>

    <!-- Bootstrap core CSS -->
    <link href="/dist/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous">

    <style>
      .bd-placeholder-img { font-size: 1.125rem; text-anchor: middle; -webkit-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none; }
      @media (min-width: 768px) { .bd-placeholder-img-lg { font-size: 3.5rem; } }
    </style>
    <!-- Custom styles for this template -->
    <link href="carousel.css" rel="stylesheet">
  </head>
  <body>
    <header>
  <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
    <a class="navbar-brand" href="/menu.php">OneTwoSeven - Administration</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse w-100 order-2" id="navbarCollapse">
      <ul class="navbar-nav ml-auto">
        <li class="nav-item"><a class="nav-link" href="/logout.php">Logout</a></li>
      </ul>
    </div>
  </nav>
</header>

<main role="main">

  <!-- Marketing messaging and featurettes
  ================================================== -->
  <!-- Wrap the rest of the page in another container to center all the content. -->

  <div class="container marketing">

    <!-- START THE FEATURETTES -->
    <br><br><br>

    <div class="row featurette">
      <div class="col-md-3">
<?php
foreach (glob("addons/ots-*.php") as $fn) {
	$addon_file = basename($fn);
	$addon_type = rtrim(file($fn)[1]);
	$addon_name = substr(file($fn)[2],2);
	echo '<p class="lead"><a href="?addon=',$fn,'">',$addon_name,'</a>&nbsp;<sup><font size="-2"><a href=/addon-download.php?addon=',$addon_file,'>[DL]</a></font></sup></p>';
}
?>
      </div>
      <div class="col-md-9">
        <pre>

<?php 
set_time_limit(2);
if (isset($_GET['addon'])) {
	$addon_file = basename($_GET['addon']);
	$addon_type = rtrim(file("addons/".$addon_file)[1]);
	if ( $addon_type == '# OneTwoSeven Admin Plugin' ) {
		require_once("addons/".$addon_file);
	} else {
		echo "Unknown plugin type.";
	}
}
?>

	</pre>
      </div>
    </div>

    <div class="row featurette">
      <div class="col-md-12">
        <h2 class="featurette-heading">Plugin Upload.<span class="text-muted"> Admins Only!</span></h2>
        <p class="lead">Upload new plugins to include on this status page using the upload form below.</p>
        <form action="addon-upload.php" method="POST" enctype="multipart/form-data">
          <input type="file" name="addon" />
          <input type="submit" disabled="disabled" /><sup><font size="-2" color="red"> Disabled for security reasons.</font></sup>
        </form>
      </div>
    </div>

    <hr class="featurette-divider">


  </div><!-- /.container -->

  <!-- FOOTER -->
  <footer class="container">
    <p class="float-right"><a href="#">Back to top</a></p>
    <p>&copy; 2019 OneTwoSeven, Dec. &middot; <a href="#">Privacy</a> &middot; <a href="#">Terms</a></p>
  </footer>
</main>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
      <script>window.jQuery || document.write('<script src="/docs/4.3/assets/js/vendor/jquery-slim.min.js"><\/script>')</script><script src="dist/js/bootstrap.bundle.min.js" crossorigin="anonymous"></script></body>
</html>
