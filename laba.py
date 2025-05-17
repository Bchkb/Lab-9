from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///baza.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    term = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {"id": self.id, "company": self.company, "term": self.term}

with app.app_context():
        db.create_all()

@app.route("/")
def index():
    return render_template("idexlaba.html")

@app.route("/api/places", methods=["GET"])
def get_places():
    places = Place.query.all()
    return jsonify([place.to_dict() for place in places])

@app.route("/api/places", methods=["POST"])
def add_company():
    data = request.get_json()
    new_place = Place(company=data["company"], term=data["term"])
    db.session.add(new_place)
    db.session.commit()
    return jsonify(new_place.to_dict()), 201

if __name__ == "__main__":
    app.run(debug=True)