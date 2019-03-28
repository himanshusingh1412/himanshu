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
		<body bgcolor="lightblue">
			<center>
			<img src="img/CT.png" height="50" width="50">
			<h1>Users Records......</h1>
			<h3>Select Users</h3>
			<form>
			<table border="2" cellspacing="10" cellpadding="10" bgcolor="skyblue">
				<tr bgcolor="bluered">
					<th>Name</th>
					<th>Account Number</th>
					<th>Email</th>
					<th>Date of Birth</th>
					<th>Address</th>
					<th>Current Credit</th>
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
	print('</tr>')

print("""
					</table>
				</form>
				<a href="transfer2.py"><input type="submit" name="s1" value="Transfer details"></a>
				
			</center>
		</body>
	</html>


	""")

s1=form.getvalue('s1')
if s1!=None:
	print("<script>alert('Transfer Details')</script>")
	print("<script>window.location='transfer2.py'</script>")