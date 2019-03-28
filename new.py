#!C:\python36\python.exe
print("Content-type:text/html")
print("")
import cgi,cgitb,pymysql
cgitb.enable()

form=cgi.FieldStorage()

db=pymysql.connect(host='localhost',user='root1',password='root1',database='creditmng')
cursor=db.cursor()
uaccno1=form.getvalue('uaccno1')
query1="select ucredit from user where uaccno='%s'"%(uaccno1)
cursor.execute(query1)
ucredit12=cursor.fetchone()
query123="select uaccno from user"
cursor.execute(query123)
res1=cursor.fetchall()
print("""
<!DOCTYPE html>
<html>
<head>
	<title>user</title>
	<link rel="icon" href="img/CT.png" />
</head>
<body bgcolor="lightblue">
	<form autocomplete="on">
		<center>
		<img src="img/CT.png" height="50" width="50"><br><br><br><br>
			Enter Details
			<table bgcolor="skyblue">
				<tr>
					<td>Enter date</td>
					<td><input type="date" name="tdate" placeholder="Enter Date"></td>
				</tr>
				<tr>
					<td>Enter Account no</td>
					<td>
					<select name="uaccno1">
						""")
for x in res1:
	print("<option value='"+x[0]+"'>"+x[0]+"</option>")
print("""
					</select>
					</td>
				</tr>
				<tr>
					<td>Enter Credit</td>
					<td><input type="number" name="ucredit1" placeholder="Enter Amount to transfer"></td>
				</tr>
				<tr>
					<td>Enter Account no</td>
					<td>
					<select name="uaccno2">
						""")
for x in res1:
	print("<option value='"+x[0]+"'>"+x[0]+"</option>")
print("""
					</select></td>
				</tr>
			</table>
			<br><br>
			<div>
				<input type="submit" name="Transfer" value="Transfer">
				<input type="reset" name="Cancel" value="Cancel">
			</div>
		</center>
	</form>

</body>
</html>
""")
submit=form.getvalue('Transfer')
if submit!=None:
	tdate=form.getvalue('tdate')
	uaccno1=form.getvalue('uaccno1')
	uaccno2=form.getvalue('uaccno2')
	ucredit1=form.getvalue('ucredit1')
	query="select ucredit from user where uaccno='%s'"%(uaccno2)
	cursor.execute(query)
	ucredit2=cursor.fetchone()
	if ucredit2!=None:
		if int(ucredit1)>int(ucredit12[0]):
			print("<script>alert('Enter valid credits')</script>")
			print("<script>window.location='new.py'</script>")
		else:
			ucredit3=int(ucredit1)+int(ucredit2[0])
			ucredit4=int(ucredit12[0])-int(ucredit1)
			query2="update user set ucredit='%s' where uaccno='%s'"%(ucredit3,uaccno2)
			cursor.execute(query2)
			db.commit()
			query3="update user set ucredit='%s' where uaccno='%s'"%(ucredit4,uaccno1)
			cursor.execute(query3)
			db.commit()
			query4="insert into trans values('%s','%s',%s,'%s')"%(uaccno1,uaccno2,ucredit1,tdate)
			cursor.execute(query4)
			db.commit()
			print("<script>alert('Transfer Successful')</script>")
			print("<script>window.location='transfer.py'</script>")
