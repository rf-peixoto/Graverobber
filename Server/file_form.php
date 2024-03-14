<?php
  // Just a random form
  $target_dir = "uploads/";
  $target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
  $uploadok = 1;
  if ($uploadok == 1) {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)){
      echo "200 - File received.";
    } else {
      echo "??? - An error ocurred.";
    }
  }

?>

//<?php
  // Just a random form with extensive file type support
//  $target_dir = "uploads/";
//  $target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
//  $uploadOk = 1;
//  $fileType = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));
//
  // List of allowed file types
//  $allowedTypes = array("txt", "pdf", "odt", "xls", "png", "jpg", "jpeg", "exe",
//                        "epub", "mp3", "gif", "doc", "odp", "ods", "json", "rs",
//                        "mp4", "avi", "md", "ogg", "m4a", "ini", "c", "cpp", "jar",
//                        "rb", "java", "pl", "py", "apk", "raw", "eml", "msg", "tmp",
//                        "conf", "config", "yaml", "asm", "h", "r", "m", "luac", "dat",
//                        "sasf", "lua", "src", "perl", "c#", "go", "smali", "csproj",
//                        "bash", "sh", "asic", "run", "vb", "vbe", "kt", "lsp", "vba",
//                        "nt", "geojson", "c++", "ps1", "dev", "mk", "owl", "scala", "mkv",
//                        "odl", "rar", "bak", "bkp", "iso", "zip", "7z", "sbf", "old", "meta",
//                        "psw", "bkf", "fbk", "xar", "moz-backup", "orig", "new", "001", "bps",
//                        "img", "deleted", "eg", "ren", "undo", "ofb", "da1", "sql", "bak1", "gcb",
//                        "in1", "och", "exclude", "data", "$$$", "000", "bac", "arc", "assets",
//                        "resource", "resS", "info", "dll", "vdx", "cache", "csv");
//
  // Check if the file is an allowed type
//  if (!in_array($fileType, $allowedTypes)) {
//    echo "Error - File type not allowed.";
//    $uploadOk = 0;
//  }
//
  // Check if $uploadOk is set to 0 by an error
//  if ($uploadOk == 0) {
//    echo "Your file was not uploaded.";
  // if everything is ok, try to upload file
//  } else {
//    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
//      echo "200 - The file " . htmlspecialchars( basename( $_FILES["fileToUpload"]["name"])) . " has been uploaded.";
//    } else {
//      echo "??? - An error occurred during the upload.";
//   }
//  }
//?>
