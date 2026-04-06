from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Mock DB (replace with real DB in production)
ratings_db = []

@app.route('/ratings', methods=['POST'])
def create_or_update_rating():
    data = request.json

    user_id = data.get('userId')
    port = data.get('port')
    section = data.get('section')
    rating = data.get('rating')
    comment = data.get('comment', '')

    # Check if rating already exists
    existing = next(
        (r for r in ratings_db if r['userId'] == user_id and r['port'] == port and r['section'] == section),
        None
    )

    if existing:
        existing['rating'] = rating
        existing['comment'] = comment
        return jsonify({"message": "Rating updated", "data": existing})

    new_rating = {
        "userId": user_id,
        "port": port,
        "section": section,
        "rating": rating,
        "comment": comment
    }

    ratings_db.append(new_rating)
    return jsonify({"message": "Rating created", "data": new_rating})


@app.route('/ratings', methods=['GET'])
def get_rating():
    user_id = request.args.get('userId')
    port = request.args.get('port')
    section = request.args.get('section')

    rating = next(
        (r for r in ratings_db if r['userId'] == user_id and r['port'] == port and r['section'] == section),
        None
    )

    if rating:
        return jsonify(rating)

    return jsonify({"message": "No rating found"}), 404


if __name__ == '__main__':
    app.run(debug=True)