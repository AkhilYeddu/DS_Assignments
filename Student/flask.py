from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'registration_db'

mysql = MySQL(app)

# Root endpoint to render registration form
@app.route('/')
def registration_form():
    return render_template('register.html')

# Register endpoint to handle form submission
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        # Fetch form data
        student_name = request.form['student_name']
        father_name = request.form['father_name']
        mother_name = request.form['mother_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        date_of_birth = request.form['date_of_birth']
        address = request.form['address']
        blood_group = request.form['blood_group']
        department = request.form['department']
        course = request.form['course']
        password = generate_password_hash(request.form['password'])  # Hash the password

        # Cursor creation
        cur = mysql.connection.cursor()

        # Execute query to insert data into database
        cur.execute(
            "INSERT INTO users (student_name, father_name, mother_name, phone_number, email, date_of_birth, address, blood_group, department, course, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (student_name, father_name, mother_name, phone_number, email, date_of_birth, address, blood_group, department, course, password)
        )

        # Commit transaction
        mysql.connection.commit()

        # Close connection
        cur.close()

        return redirect('/')  # Redirect to root endpoint after successful registration

# Run the application
if __name__ == '__main__':
    app.run(debug=True)