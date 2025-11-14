<html>
<head><title>Welcome to my excellent blog</title></head>
<body>
<img src='storage/my-excellent-blog.png'>
<h1>Welcome to my excellent blog</h1>
<?php
 $dbserver = "IP-VM-mysql"; 
 $dbuser = "Nom-utilisateur-db";
 $dbpassword = "Mot-de-passe-db";

 try {
   $conn = new PDO("mysql:host=$dbserver;dbname=mysql", $dbuser, $dbpassword);
   $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
   echo "Connected successfully";
 } catch(PDOException $e) {
   echo "Database connection failed: " . $e->getMessage();
 }
?>
</body></html>
