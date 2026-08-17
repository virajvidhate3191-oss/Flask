from flask import Flask
app = Flask(__name__)
@app.route('/')
def college():
    return """
<h1>College Details</h1>
<hr>
<b>College Name :</b> ABC College of Engineering<br><br>
<b>Address :</b> Shivaji Nagar, Pune<br><br>
<b>Principal :</b> Dr. Rajesh Sharma<br><br>
<b>Courses :</b>
<ul>
<li>BCA</li>
<li>BBA</li>
<li>B.Sc Computer Science</li>
<li>MCA</li>
</ul>
<b>Contact Number :</b> 9876543210<br><br>
<b>Email :</b> info@abccollege.com<br><br>
<b>Website :</b> www.abccollege.com
"""
if __name__ == "__main__":
    app.run(debug=True)