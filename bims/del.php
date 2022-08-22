<!doctype html>
<html>
<head>
<meta charset='uft-8'>
<title>删除记录界面</title>
</head>

    
<body>
<?php
    $link =mysqli_connect('localhost','root','password','test_table');
    session_start();
    $del=$_SESSION['del'];
    
    if(!$link){
        exit('connect failed');
    }
    $ans=mysqli_query($link,"delete from delivery where dno='$del'");
    if(!$ans){
        echo '<script> 
        if(confirm("删除")==true){
            location.href="del.php";
        }
        </script>';
    }
    unset($_SESSION['del']);//清理session
    header('location:page.html');
    
?>

</body>
</html>