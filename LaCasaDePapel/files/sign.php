<?php
// For SSL certificates, the  commonName is usually the domain name of
// that will be using the certificate, but for S/MIME certificates,
// the commonName will be the name of the individual who will use the certificate.
$dn = array(
    "countryName" => "UK",
    "stateOrProvinceName" => "Somerset",
    "localityName" => "Glastonbury",
    "organizationName" => "The Brain Room Limited",
    "organizationalUnitName" => "PHP Documentation Team",
    "commonName" => "Wez Furlong",
    "emailAddress" => "wez@example.com"
);

// Generate a new private (and public) key pair
//$privkey = openssl_pkey_new();
$privkey = file_get_contents("/home/arti/htb/lacasadepapel/files/lacasadepapel.key");

// Generate a certificate signing request
$csr = openssl_csr_new($dn, $privkey);

// Create a CA signed certificate valid for 365 days
$cacert = file_get_contents("/home/arti/htb/lacasadepapel/files/lacasadepapel.cer");
$sscert = openssl_csr_sign($csr, $cacert, $privkey, 365);

// Now you will want to preserve your private key, CSR and self-signed
// cert so that they can be installed into your web server.
openssl_csr_export($csr, $csrout) and var_dump($csrout);
openssl_x509_export($sscert, $certout) and var_dump($certout);
openssl_pkey_export($privkey, $pkeyout, "lacasadepapel") and var_dump($pkeyout);

// Show any errors that occurred here
while (($e = openssl_error_string()) !== false) {
    echo $e . "\n";
}
//save certificate and privatekey to file
file_put_contents("lacasadepapel-signed.cer", $certout);
//file_put_contents("privatekey.pem", $pkeyout);
?>
