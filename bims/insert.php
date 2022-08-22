<!doctype html>
<html>
<head>
    <meta charseet="utf-8">
    <title>新增配送员记录</title>
</head>
        <h1 align="center">新增配送员记录</h>
        <form action="" method="post" name="inf">
        <p align="center">序号:<input type="text" name ="no"/></p>
        <p align="center">电话<input type="text" name ="tel"/></p>
        <p align="center">姓名<input type="text" name ="name"/></p>
        <p align="center">等级<input type="text" name ="grade"/></p>
        <p align="center"><input type="submit" name ="insub"/></p>
        
        </form>
<?php
session_start();
    $link=mysqli_connect('localhost','root','password','test_table');
    if(!$link){
        exit('数据库连接失败');
    }
    if(!empty($_POST["insub"])){
        $no=$_POST['no'];
        $name=$_POST['name'];
        $tel=$_POST['tel'];
        $grade=$_POST['grade'];
        mysqli_query($link,"insert into delivery values('$no','$tel','$name','$grade')");
        $_SESSION['success'] = "添加success";
    //_SESSION['success']=
        header('location:page.html');
    }   




?>

    </body>
    </html>