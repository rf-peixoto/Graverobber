<?php

  $target_dir = "uploads/";
  $target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
  $uploadok = 1;
  if ($uploadok == 1) {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)){
      echo "File received.";
    } else {
      echo "An error ocurred.";
    }
  }

?>
