import yagmail
paswrd = 'nrtqsyfjkoncjbem'
myemail = 'pythontestemailshtrikuldmitry'
yagmail.register(myemail, paswrd)
yag = yagmail.SMTP(myemail)


to = 'dmitriyshtrikul@gmail.com'
subj = 'YAG test'
img = 'yaglogo.jpg'
attach = 'UML Classroom.pdf'
body = f"""<h1>Nice lib</h1><br>
<img src=https://www.python.org/static/community_logos/python-logo.png>"""
yag.send(to, subj, [body, img])

print('yagged')