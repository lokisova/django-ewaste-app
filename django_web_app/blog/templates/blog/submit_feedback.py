import cgi
import cgitb
import os

# Enable debugging
cgitb.enable()

# Get data from the form
form = cgi.FieldStorage()
name = form.getvalue('name')
email = form.getvalue('email')
feedback = form.getvalue('feedback')

# Define the file path
feedback_file = 'feedback.txt'

# Save the feedback to a local file
with open(feedback_file, 'a') as file:
    file.write(f"Name: {name}\n")
    file.write(f"Email: {email}\n")
    file.write(f"Feedback: {feedback}\n")
    file.write("\n")

# Print HTML response
print("Content-type: text/html\n")
print("<html><body>")
print("<h2>Thank you for your feedback!</h2>")
print("</body></html>")
