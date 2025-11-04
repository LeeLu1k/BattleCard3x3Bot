from flask import Flask, request, jsonify, send_from_directory
import os, json

app = Flask(__name__)
DATA_FILE = "players.json"

# Загружаем игроков
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        players = json.load(f)
else:
    players = {}

@app.route('/')
def index():
    return send_from_directory('webapp', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('webapp', path)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user_id = str(data.get("id"))
    username = data.get("username", "Игрок")

    # Если новый игрок
    if user_id not in players:
        players[user_id] = {
            "username": username,
            "hero": "⚔️ Паладин",
            "level": 1,
            "gift_received": True
        }
        save_players()
        message = "Добро пожаловать! Тебе выпал герой 🎁 Паладин!"
    else:
        message = f"С возвращением, {players[user_id]['username']}!"

    return jsonify({
        "player": players[user_id],
        "message": message
    })

def save_players():
    with open(DATA_FILE, "w") as f:
        json.dump(players, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
