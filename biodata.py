from flask import Flask
app = Flask(__name__)
@app.route('/')
def biodata():
    return """
<h1>Student Biodata</h1>
<hr>
Name : Rahul Patil<br><br>
Roll Number : 101<br><br>
Class : TYBCA<br><br>
Department : Computer Science<br><br>
Email : rahul@gmail.com<br><br>
Mobile Number : 9876543210<br><br>
City : Pune
"""
if __name__ == "__main__":
    app.run(debug=True)