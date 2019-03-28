#!C:\python36\python.exe
print("Content-type:text/html")
print("")
import cgi,cgitb,pymysql
cgitb.enable()

form=cgi.FieldStorage()

db=pymysql.connect(host='localhost',user='root1',password='root1',database='creditmng')
cursor=db.cursor()
query="select * from user"
cursor.execute(query)
result=cursor.fetchall()

print("""
	<html>
		<head>
			<title>Credit Transfer</title>
			<link rel="icon" href="img/CT.png" />
		</head>
		<body bgcolor="#f44336">
			<center>
			<img src="img/CT.png" height="50" width="50">
			<h1>Users Records......</h1>
			<h3>Select Users</h3>
			<form action="new.py" method="get" autocomplete="on">
			<table border="2" cellspacing="10" cellpadding="10" bgcolor="skyblue">
				<tr bgcolor="bluered">
					<th>Name</th>
					<th>Account Number</th>
					<th>Email</th>
					<th>Date of Birth</th>
					<th>Address</th>
					<th>Current Credit</th>
					<th>Transfer from</th>
				</tr>
				""")

for x in result:
	print('<tr>')
	print("<td>",x[1],"</td>")
	print('<td>',x[6],'</td>')
	print('<td>',x[2],'</td>')
	print('<td>',x[3],'</td>')
	print('<td>',x[4],'</td>')
	print('<td>',x[5],'</td>')
	print("<td><a href='new.py?uaccno1="+x[6]+"'><input type='submit' name='uaccno1' value='"+x[6]+"'></a></td>")
	print('</tr>')

print("""
			</table>
			</form>
			</center>
		</body>
	</html>


	""")

submit=form.getvalue('submit')
uaccno1=form.getvalue('uaccno1')
if submit!=None and uaccno1!=None:
	print("<script>window.location='new.py'</script>")