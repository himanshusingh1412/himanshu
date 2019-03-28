#!C:\python36\python.exe
print("Content-type:text/html")
print("")
import cgi,cgitb,pymysql
cgitb.enable()

form=cgi.FieldStorage()

db=pymysql.connect(host='localhost',user='root1',password='root1',database='creditmng')
cursor=db.cursor()
query2="select * from trans"
cursor.execute(query2)
res=cursor.fetchall()
print("""
	<html>
		<head>
			<title>Credit Transfer</title>
			<link rel="icon" href="img/CT.png" />
		</head>
		<body bgcolor="lightblue">
			<center>
			<img src="img/CT.png" height="50" width="50">
			<h1>Transaction Records......</h1>
			<form>
			<table border="2" cellspacing="10" cellpadding="10" bgcolor="skyblue">
				<tr bgcolor="bluered">
					<th>Transfer From</th>
					<th>Transfer To</th>
					<th>Credit Transfered</th>
					<th>Date of Transaction</th>
				</tr>
				""")

for x in res:
	print('<tr>')
	print("<td>",x[0],"</td>")
	print('<td>',x[1],'</td>')
	print('<td>',x[2],'</td>')
	print('<td>',x[3],'</td>')
	print('</tr>')
			
print("""
					</table>
				</form>
				<a href="credit.py"><input type="submit" name="s3" value="Users"></a>
			</center>
		</body>
	</html>
		""")
s3=form.getvalue('s3')
if s3!=None:
	print("<script>window.location='credit.py'</script>")