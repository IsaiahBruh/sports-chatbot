from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

sport_info = {
    "Soccer": {
        "rules": "Soccer is played with two teams of 11 players. The goal is to score by kicking the ball into the opponent's net.",
        "famous_players": "Lionel Messi, Cristiano Ronaldo, Pelé, Diego Maradona",
        "history": "Soccer originated in England in the 19th century and is now the most popular sport in the world.",
        "beginner_tips": "Start by practicing dribbling, passing, and shooting. Watch professional games to learn tactics."
    },
    "Basketball": {
        "rules": "Basketball is played with two teams of 5 players. The goal is to score points by shooting the ball into the hoop.",
        "famous_players": "Michael Jordan, LeBron James, Kobe Bryant, Stephen Curry",
        "history": "Basketball was invented by James Naismith in 1891 in the USA.",
        "beginner_tips": "Work on dribbling, shooting, and passing. Try practicing free throws and layups regularly."
    },
    "Tennis": {
        "rules": "Tennis is played between two players (singles) or four players (doubles). The goal is to hit the ball over the net and win points.",
        "famous_players": "Roger Federer, Rafael Nadal, Serena Williams, Novak Djokovic",
        "history": "Tennis has origins in 12th-century France but became modernized in England in the 19th century.",
        "beginner_tips": "Practice your serves and backhands. Start with slow rallies and improve your footwork."
    },
    "Cricket": {
        "rules": "Cricket is played between two teams of 11 players. One team bats, trying to score runs, while the other bowls and fields.",
        "famous_players": "Sachin Tendulkar, Virat Kohli, Don Bradman, MS Dhoni",
        "history": "Cricket originated in England in the 16th century and is hugely popular in South Asia and Australia.",
        "beginner_tips": "Learn how to hold the bat properly, practice bowling line and length, and understand field placements."
    },
    "Baseball": {
        "rules": "Baseball is played with two teams of 9 players. The goal is to hit the ball and run around bases to score.",
        "famous_players": "Babe Ruth, Jackie Robinson, Derek Jeter, Shohei Ohtani",
        "history": "Baseball was developed in the USA in the 19th century and became a major sport worldwide.",
        "beginner_tips": "Work on your batting stance, practice throwing and catching, and learn base running strategies."
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_sport_info', methods=['POST'])
def get_sport_info():
    sport = request.json.get("sport")
    if sport in sport_info:
        return jsonify(sport_info[sport])
    else:
        return jsonify({"error": "Sport not found. Please try again."})

if __name__ == '__main__':
    app.run(debug=True)
