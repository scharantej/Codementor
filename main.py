 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tutorial/<int:tutorial_id>')
def tutorial(tutorial_id):
    return render_template('tutorial.html', tutorial_id=tutorial_id)

@app.route('/exercise/<int:exercise_id>')
def exercise(exercise_id):
    return render_template('exercise.html', exercise_id=exercise_id)

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run()


## Deployment

The application can be deployed to a production server using the following command:


gunicorn app:app


The application can then be accessed by visiting the following URL:


http://<your-server-ip>:5000
