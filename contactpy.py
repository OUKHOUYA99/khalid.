import cgi

form = cgi.FieldStorage()

name = form.getvalue("name")
email = form.getvalue("email")
message = form.getvalue("message")

print("Content-Type: text/html\n")
print("<html><body>")
print("<h2>Form Submission Successful</h2>")
print("<p>Name: {}</p>".format(name))
print("<p>Email: {}</p>".format(email))
print("<p>Message: {}</p>".format(message))
print("</body></html>")