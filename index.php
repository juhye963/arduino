<?php
function DB_conn()
{
    $db_type="mysql";
    $db_host="localhost";
    $db_name="arduino";
    $db_user="sample";
    $db_pass="password";

    $dsn="$db_type:host=$db_host;dbname=$db_name;charset=utf8";

    try
    {   $pdo=new PDO($dsn,$db_user,$db_pass);
        $pdo->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
        $pdo->setAttribute(PDO::ATTR_EMULATE_PREPARES,false);
    }
    catch(PDOException $Exception)
    {   die('error:'.$Exception->getMessage());    } 
    
    return $pdo; 
}
?>

<html>
<head>
<title>온도</title>
</head>
<body text-align="center">
<font size=4>조도 리스트</font>
<table width='500' border='1'>
<tr>
<th align='center'>온도</th>
<th align='center'>시간</th>

<?php
$pdo = DB_conn();

try
{
    $sql="SELECT * FROM temp_tb;";
    $stmh=$pdo->prepare($sql);
    $stmh->execute();
}
catch(PDOException $e)
{   print 'err: '. $e->getMessage();   }

while($row=$stmh->fetch(PDO::FETCH_ASSOC))
{
?>
    <tr>
    <td align='center'><?=$row['light']?></td>
    <td align='center'><?=$row['dt']?></td>
    <tr>
<?php
}
?>
</tr>
</table>
</body>
</html>
