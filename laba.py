from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baza.db'
db = SQLAlchemy(app)

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    term = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Place %r>' % self.id

@app.route('/')
def index():
    return render_template('idexlaba.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
