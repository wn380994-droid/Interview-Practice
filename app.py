from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_mail import Mail, Message
import pymysql
import re
import hashlib
import secrets
import string
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Flask-Mail
mail = Mail(app)


def get_db_connection():
    """Create database connection"""
    try:
        connection = pymysql.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB'],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except Exception as e:
        print(f"Database connection error: {e}")
        return None


def initialize_database():
    """Create database and table if they don't exist"""
    try:
        connection = pymysql.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS interview_practice_db")
            print("✅ Database created/checked")

            cursor.execute("USE interview_practice_db")

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    phone VARCHAR(20),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            print("✅ Users table created/checked")

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS positions (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(100) NOT NULL UNIQUE,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            print("✅ Positions table created/checked")

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS interview_questions (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    position_id INT,
                    language ENUM('English', 'Myanmar') NOT NULL,
                    question_text TEXT NOT NULL,
                    difficulty ENUM('Easy', 'Medium', 'Hard') DEFAULT 'Medium',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (position_id) REFERENCES positions(id) ON DELETE CASCADE
                )
            """)
            print("✅ Interview questions table created/checked")

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS question_answers (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    question_id INT,
                    answer_text TEXT NOT NULL,
                    is_correct BOOLEAN DEFAULT FALSE,
                    explanation TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (question_id) REFERENCES interview_questions(id) ON DELETE CASCADE
                )
            """)
            print("✅ Question answers table created/checked")

            cursor.execute("SELECT COUNT(*) as cnt FROM positions")
            if cursor.fetchone()['cnt'] == 0:
                positions = [
                    ('Software Engineer', 'Backend, Frontend, Full-stack development'),
                    ('Data Analyst', 'Data analysis, visualization, and reporting'),
                    ('Project Manager', 'Project planning and team management'),
                    ('UX Designer', 'User experience and interface design'),
                    ('Marketing Specialist', 'Digital marketing and campaign management'),
                    ('Sales Executive', 'Sales strategies and client relationships'),
                    ('HR Manager', 'Human resources and talent management'),
                    ('Finance Analyst', 'Financial analysis and planning')
                ]
                for name, desc in positions:
                    cursor.execute("INSERT INTO positions (name, description) VALUES (%s, %s)", (name, desc))
                print("✅ Default positions inserted")

        connection.commit()
        connection.close()
        print("✅ Database initialization complete!")

    except Exception as e:
        print(f"❌ Database initialization error: {e}")


def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()


def generate_random_password(length=8):
    """Generate a random alphanumeric password"""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))


# -------------------- ROUTES --------------------
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name'].strip()
        email = request.form['email'].strip().lower()
        password = request.form['password']
        phone = request.form['phone'].strip()

        if not name or not email or not password or not phone:
            flash('All fields are required!', 'error')
            return redirect(url_for('signup'))

        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            flash('Invalid email format!', 'error')
            return redirect(url_for('signup'))

        if len(password) < 6:
            flash('Password must be at least 6 characters long!', 'error')
            return redirect(url_for('signup'))

        phone_clean = phone.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
        if not re.match(r'^(\+?959|09)\d{7,9}$', phone_clean):
            flash('Please enter a valid Myanmar phone number (e.g., 09XXXXXXXX or +959XXXXXXXX)', 'error')
            return redirect(url_for('signup'))

        connection = get_db_connection()
        if connection is None:
            flash('Database connection error!', 'error')
            return redirect(url_for('signup'))

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
                existing_user = cursor.fetchone()

                if existing_user:
                    flash('Email already registered! Please login.', 'error')
                    return redirect(url_for('signup'))

                hashed_password = hash_password(password)

                cursor.execute(
                    "INSERT INTO users (name, email, password, phone) VALUES (%s, %s, %s, %s)",
                    (name, email, hashed_password, phone)
                )

                connection.commit()
                flash('Registration successful! Please login.', 'success')
                return redirect(url_for('login'))

        except Exception as e:
            print(f"Signup error: {e}")
            flash('Registration failed. Please try again!', 'error')
            return redirect(url_for('signup'))
        finally:
            connection.close()

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email'].strip().lower()
        password = request.form['password']

        if not email or not password:
            flash('Please enter both email and password!', 'error')
            return redirect(url_for('login'))

        connection = get_db_connection()
        if connection is None:
            flash('Database connection error!', 'error')
            return redirect(url_for('login'))

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
                user = cursor.fetchone()

                if user:
                    hashed_password = hash_password(password)
                    if user['password'] == hashed_password:
                        session['user_id'] = user['id']
                        session['user_name'] = user['name']
                        session['user_email'] = user['email']
                        flash(f'Welcome back, {user["name"]}!', 'success')
                        return redirect(url_for('select_lang_pos'))
                    else:
                        flash('Invalid password!', 'error')
                else:
                    flash('Email not registered! Please sign up first.', 'error')

        except Exception as e:
            print(f"Login error: {e}")
            flash('Login failed. Please try again!', 'error')
        finally:
            connection.close()

    return render_template('login.html')


@app.route('/forgot-password', methods=['POST'])
def forgot_password():
    """Handle forgot password request: generate new password, update DB, send email."""
    data = request.get_json()
    email = data.get('email', '').strip().lower()

    if not email or not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return jsonify({'success': False, 'message': 'Invalid email format.'}), 400

    connection = get_db_connection()
    if not connection:
        return jsonify({'success': False, 'message': 'Database error.'}), 500

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()
            if not user:
                return jsonify({'success': False, 'message': 'Email not registered.'}), 404

            # Generate new password
            new_password = generate_random_password(8)
            hashed = hash_password(new_password)

            # Update database
            cursor.execute("UPDATE users SET password = %s WHERE id = %s", (hashed, user['id']))
            connection.commit()

            # Send email
            msg = Message(
                subject="Password Reset - Interview Practice",
                recipients=[email],
                body=f"""
Hello {user['name']},

Your password has been reset. You can now log in with the following temporary password:

Temporary Password: {new_password}

Please change your password after logging in for security reasons.

Best regards,
Interview Practice Team
                """
            )
            mail.send(msg)

            return jsonify({'success': True, 'message': 'A new password has been sent to your email.'})

    except Exception as e:
        print(f"Forgot password error: {e}")
        return jsonify({'success': False, 'message': 'Failed to process request. Please try again.'}), 500
    finally:
        connection.close()


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out!', 'info')
    return redirect(url_for('home'))


@app.route('/start-free')
def start_free():
    return redirect(url_for('signup'))


@app.route('/select-lang-pos', methods=['GET', 'POST'])
def select_lang_pos():
    if 'user_id' not in session:
        flash('Please login first!', 'error')
        return redirect(url_for('login'))

    if request.method == 'POST':
        language = request.form.get('language')
        position = request.form.get('position')

        if not language or not position:
            flash('Please select both language and position!', 'error')
            return redirect(url_for('select_lang_pos'))

        session['selected_language'] = language
        session['selected_position'] = position
        session['interview_answers'] = []
        session['questions_ids'] = []

        flash(f'Selected: {language} language, {position} position', 'success')
        return redirect(url_for('interview_section'))

    return render_template('select_lang_pos.html')


@app.route('/interview-section')
def interview_section():
    if 'user_id' not in session:
        flash('Please login first!', 'error')
        return redirect(url_for('login'))

    if 'selected_language' not in session or 'selected_position' not in session:
        flash('Please select language and position first!', 'error')
        return redirect(url_for('select_lang_pos'))

    return render_template('interview.html',
                           selected_language=session['selected_language'],
                           selected_position=session['selected_position'])


# -------------------- API ENDPOINTS --------------------
@app.route('/api/next-question', methods=['GET'])
def api_next_question():
    if 'user_id' not in session:
        return jsonify({'error': 'Not logged in'}), 401
    if 'selected_language' not in session or 'selected_position' not in session:
        return jsonify({'error': 'Position/language not selected'}), 400

    data, err = fetch_next_question()
    if err:
        return jsonify({'error': err}), 500
    return jsonify(data)


@app.route('/api/submit-answer', methods=['POST'])
def api_submit_answer():
    if 'user_id' not in session:
        return jsonify({'error': 'Not logged in'}), 401

    data = request.get_json()
    question_id = data.get('question_id')
    answer_id = data.get('answer_id')
    confidence_data = data.get('confidence', {})

    if not question_id or not answer_id:
        return jsonify({'error': 'Missing data'}), 400

    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Database error'}), 500
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT is_correct FROM question_answers WHERE id = %s", (answer_id,))
            ans = cursor.fetchone()
            if not ans:
                return jsonify({'error': 'Answer not found'}), 404
            correct = ans['is_correct']
    except Exception as e:
        print(f"Error verifying answer: {e}")
        return jsonify({'error': 'Server error'}), 500
    finally:
        connection.close()

    answers = session.get('interview_answers', [])
    answers.append({
        'question_id': question_id,
        'answer_id': answer_id,
        'is_correct': correct
    })
    session['interview_answers'] = answers

    if confidence_data and 'avg' in confidence_data:
        session['avg_confidence'] = confidence_data['avg']

    if len(answers) >= 5:
        correct_count = sum(1 for a in answers if a['is_correct'])
        interview_score = correct_count * 20
        avg_conf = session.get('avg_confidence', 75)
        return jsonify({
            'completed': True,
            'results': {
                'correct': correct_count,
                'total': 5,
                'interview_score': interview_score,
                'confidence_score': round(avg_conf, 1)
            }
        })
    else:
        data, err = fetch_next_question()
        if err:
            return jsonify({'error': err}), 500
        return jsonify(data)


@app.route('/api/results-summary', methods=['GET'])
def api_results_summary():
    """Return summary of wrong answers with correct answers."""
    if 'user_id' not in session:
        return jsonify({'error': 'Not logged in'}), 401

    answers = session.get('interview_answers', [])
    if len(answers) < 5:
        return jsonify({'error': 'Interview not completed yet'}), 400

    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Database error'}), 500

    wrong_questions = []
    try:
        with connection.cursor() as cursor:
            for ans in answers:
                if not ans['is_correct']:
                    cursor.execute("SELECT question_text FROM interview_questions WHERE id = %s", (ans['question_id'],))
                    q = cursor.fetchone()
                    if not q:
                        continue
                    cursor.execute("SELECT answer_text FROM question_answers WHERE question_id = %s AND is_correct = TRUE", (ans['question_id'],))
                    correct_ans = cursor.fetchone()
                    wrong_questions.append({
                        'question': q['question_text'],
                        'correct_answer': correct_ans['answer_text'] if correct_ans else 'N/A'
                    })
    except Exception as e:
        print(f"Error fetching summary: {e}")
        return jsonify({'error': 'Server error'}), 500
    finally:
        connection.close()

    return jsonify({'wrong_questions': wrong_questions})


# -------------------- HELPER FUNCTIONS --------------------
def fetch_next_question():
    lang = session['selected_language']
    pos = session['selected_position']

    connection = get_db_connection()
    if not connection:
        return None, 'Database error'

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM positions WHERE name = %s", (pos,))
            pos_row = cursor.fetchone()
            if not pos_row:
                return None, 'Position not found'
            pos_id = pos_row['id']

            asked_ids = session.get('questions_ids', [])
            if asked_ids:
                placeholders = ','.join(['%s'] * len(asked_ids))
                cursor.execute(f"""
                    SELECT id, question_text, difficulty 
                    FROM interview_questions 
                    WHERE position_id = %s AND language = %s AND id NOT IN ({placeholders})
                    ORDER BY RAND() LIMIT 1
                """, (pos_id, lang, *asked_ids))
            else:
                cursor.execute("""
                    SELECT id, question_text, difficulty 
                    FROM interview_questions 
                    WHERE position_id = %s AND language = %s 
                    ORDER BY RAND() LIMIT 1
                """, (pos_id, lang))

            question = cursor.fetchone()
            if not question:
                session['questions_ids'] = []
                cursor.execute("""
                    SELECT id, question_text, difficulty 
                    FROM interview_questions 
                    WHERE position_id = %s AND language = %s 
                    ORDER BY RAND() LIMIT 1
                """, (pos_id, lang))
                question = cursor.fetchone()
                if not question:
                    return None, 'No questions available'

            cursor.execute("""
                SELECT id, answer_text, is_correct 
                FROM question_answers 
                WHERE question_id = %s 
                ORDER BY RAND()
            """, (question['id'],))
            answers = cursor.fetchall()

            session['questions_ids'] = session.get('questions_ids', []) + [question['id']]
            session['current_question_id'] = question['id']

            return {
                'question': question,
                'answers': answers,
                'total_questions': 5,
                'answered': len(session.get('interview_answers', []))
            }, None
    except Exception as e:
        print(f"Error in fetch_next_question: {e}")
        return None, 'Server error'
    finally:
        connection.close()


if __name__ == '__main__':
    print("🚀 Initializing database...")
    initialize_database()
    print("🚀 Starting Interview Practice Application...")
    print("🌐 Open: http://localhost:5000")
    app.run(debug=True, port=5000, use_reloader=False)