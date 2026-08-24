from flask import Flask
app = Flask(__name__)
@app.route('/employee/<int:emp_id>/<name>/<department>')
def employee(emp_id, name, department):
    return f"""
    <h1>Employee Profile</h1>
    <hr>
    <b>Employee ID :</b> {emp_id}<br><br>
    <b>Name :</b> {name}<br><br>
    <b>Department :</b> {department}
    """
if __name__ == "__main__":
    app.run(debug=True)