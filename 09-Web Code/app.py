import os
import secrets
import numpy as np
from flask import Flask, render_template, request, redirect, session, flash, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as keras_image
import mysql.connector
import datetime
from PIL import Image

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Database connections
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aNIKEt@45",
    database="user_database"
)

db1 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aNIKEt@45",
    database="plants"
)

UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load your .h5 model (assuming the model is trained on 224x224 images)
model = load_model('/Users/aniketanilpalse/Downloads/Vishwakarma_University_(VU) /Sem-VI/Z_(Hackaton, Mega Project)/02_Mega_Project/Z_Code/Main Code/vgg16_plant_identification_model.h5')

# Define image preprocessing function
def preprocess_image(image_path):
    img = Image.open(image_path).convert('RGB')
    img = img.resize((224, 224))  # Resize image to match model input size
    img_array = np.array(img) / 255.0  # Normalize image (if your model was trained this way)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Route for index (login) page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        if user and password == user['password']:
            session['user'] = user
            session['reward_points'] = user.get('reward_points', 0)
            flash("Login successful!", "success")
            return redirect('/home')
        else:
            flash("Invalid email or password.", "error")
            return redirect('/')

    return render_template('index.html')

# Route for home page
@app.route('/home', methods=['GET'])
def home():
    user = session.get('user')
    if not user:
        flash("User not found", "error")
        return redirect('/')
    return render_template('home.html', user_name=user['username'], reward_points=session['reward_points'])

# Route for identifying plants
@app.route('/identify', methods=['GET', 'POST'])
def identify():
    if 'user' not in session:
        flash("You must be logged in to identify plants.", "error")
        return redirect('/')

    if request.method == 'POST':
        image = request.files['image']

        if image:
            # Save the uploaded image temporarily
            filename = secrets.token_hex(10) + os.path.splitext(image.filename)[1]
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)

            # Process the image to identify the plant using the loaded model
            plant_name = process_image(image_path)

            # Update reward points
            user = session['user']
            username = user['username']
            session['reward_points'] += 10

            cursor = db.cursor()
            query = "UPDATE users SET reward_points = %s WHERE username = %s"
            cursor.execute(query, (session['reward_points'], username))
            db.commit()

            # Save identification history
            query_history = "INSERT INTO history (username, plant_name, time) VALUES (%s, %s, %s)"
            cursor.execute(query_history, (username, plant_name, datetime.datetime.now()))
            db.commit()

            # Fetch plant details
            cursor_plant = db1.cursor(dictionary=True)
            query_details = "SELECT * FROM plant_info WHERE plant_name = %s"
            cursor_plant.execute(query_details, (plant_name,))
            plant_details = cursor_plant.fetchone()

            return render_template('identified.html', plant_name=plant_name, image_path='/' + image_path, plant=plant_details)

    return render_template('identify.html')

# Function to process the image and predict the plant name using the loaded model
def process_image(image_path):
    img_array = preprocess_image(image_path)
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)[0]

    # Map the predicted class index to plant name (Assuming you have a class to name mapping)
    class_labels = ['Adulsa', 'Alovera', 'Amla', 'Banana', 'BeetelLeaf(Pan)', 'Brahmi', 'CurryLeaves', 'Drumstick', 'Eranda', 'Gokarna', 'Hibiscus', 'Jamun(IndianBlackberry)', 'Mango', 'Neem', 'Onion', 'Panfuti', 'Papaya', 'Satynashi', 'Shatavari', 'Sugarcane', 'Tandulja', 'TouchMeNot']
    plant_name = class_labels[predicted_class]
    return plant_name

# Route for displaying plant categories
@app.route('/category', methods=['GET'])
def category():
    # Fetch plant names from the database
    cursor = db1.cursor(dictionary=True)
    query = "SELECT DISTINCT plant_name FROM plant_info"
    cursor.execute(query)
    plant_names = cursor.fetchall()

    # Extract plant names from the query result
    plant_names = [row['plant_name'] for row in plant_names]

    return render_template('category.html', plant_names=plant_names)

# Route for displaying plant details
@app.route('/details/<string:plant_name>', methods=['GET'])
def plant_details(plant_name):
    # Fetch plant details from the database
    cursor_plant = db1.cursor(dictionary=True)
    query = "SELECT * FROM plant_info WHERE plant_name = %s"
    cursor_plant.execute(query, (plant_name,))
    plant = cursor_plant.fetchone()

    if not plant:
        flash("Plant details not found.", "error")
        return redirect('/category')  # Redirect back to categories if no details are found

    return render_template('details.html', plant=plant)

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if 'user' not in session:
        flash("You must be logged in to edit your profile.", "error")
        return redirect('/')

    user = session['user']  # Retrieve the user data from the session
    if request.method == 'POST':
        username = request.form['name']  # Get the updated username (previously 'name')
        email = request.form['email']  # Get the updated email
        
        # Update the user profile in the database (only username and email)
        cursor = db.cursor()
        query = "UPDATE users SET username = %s, email = %s WHERE id = %s"
        cursor.execute(query, (username, email, user['id']))
        db.commit()

        # Update session with new user details (only username and email)
        session['user'] = {'id': user['id'], 'username': username, 'email': email}
        
        flash("Profile updated successfully!", "success")
        return redirect('/home')

    return render_template('edit.html', user=user)



# Route for signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        cursor = db.cursor()
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash("Email is already registered. Please log in.", "error")
            return redirect('/')

        query_insert = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query_insert, (username, email, password))
        db.commit()
        flash("Signup successful! You can now log in.", "success")
        return redirect('/')

    return render_template('signup.html')

# Route for displaying user history
@app.route('/history', methods=['GET'])
def history():
    if 'user' not in session:
        flash("You must be logged in to view history.", "error")
        return redirect('/')

    username = session['user']['username']
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM history WHERE username = %s ORDER BY time DESC"
    cursor.execute(query, (username,))
    history_records = cursor.fetchall()

    return render_template('history.html', history_records=history_records)

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']

        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        if user:
            # Generate a reset token (for simplicity using a random token here)
            reset_token = secrets.token_hex(16)
            expiration_time = datetime.datetime.now() + datetime.timedelta(hours=1)  # 1 hour expiration

            # Store the reset token and its expiration in the database
            cursor.execute("UPDATE users SET reset_token = %s, reset_token_expiry = %s WHERE email = %s",
                           (reset_token, expiration_time, email))
            db.commit()
            
            flash("Password reset link has been sent to your email.", "success")
            return redirect('/')
        else:
            flash("No account found with that email address.", "error")
            return redirect('/forgot_password')

    return render_template('forgot_password.html')

# Route for logout
@app.route('/logout')
def logout():
    session.clear()
    flash("You have logged out successfully.", "success")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)