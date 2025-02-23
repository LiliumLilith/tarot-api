from flask import Flask, jsonify
import random

app = Flask(__name__)  # BU SATIR ÖNEMLİ!

# Tarot kartları
tarot_cards = [
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
    "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
    "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
    "The Devil", "The Tower", "The Star", "The Moon", "The Sun",
    "Judgement", "The World", "Ace of Wands", "Two of Wands", "Three of Wands",
    "Four of Wands", "Five of Wands", "Six of Wands", "Seven of Wands", "Eight of Wands",
    "Nine of Wands", "Ten of Wands", "Page of Wands", "Knight of Wands",
    "Queen of Wands", "King of Wands", "Ace of Cups", "Two of Cups", "Three of Cups",
    "Four of Cups", "Five of Cups", "Six of Cups", "Seven of Cups", "Eight of Cups",
    "Nine of Cups", "Ten of Cups", "Page of Cups", "Knight of Cups",
    "Queen of Cups", "King of Cups", "Ace of Swords", "Two of Swords", "Three of Swords",
    "Four of Swords", "Five of Swords", "Six of Swords", "Seven of Swords", "Eight of Swords",
    "Nine of Swords", "Ten of Swords", "Page of Swords", "Knight of Swords",
    "Queen of Swords", "King of Swords", "Ace of Pentacles", "Two of Pentacles",
    "Three of Pentacles", "Four of Pentacles", "Five of Pentacles", "Six of Pentacles",
    "Seven of Pentacles", "Eight of Pentacles", "Nine of Pentacles", "Ten of Pentacles",
    "Page of Pentacles", "Knight of Pentacles", "Queen of Pentacles", "King of Pentacles"
]

# 3 kart çeken fonksiyon
def draw_tarot():
    deck = tarot_cards.copy()
    random.shuffle(deck)
    spread = [(card, random.choice(["Düz", "Ters"])) for card in deck[:3]]
    return spread

# API Endpoint: Kullanıcı /tarot adresine giderse açılım yap
@app.route('/tarot', methods=['GET'])
def tarot_reading():
    spread = draw_tarot()
    response = {"cards": [{"name": card, "position": position} for card, position in spread]}
    return jsonify(response)

# Flask sunucusunu başlat
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Merhaba Dünya! Flask çalışıyor!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render'ın belirlediği PORT'u kullan
    app.run(host="0.0.0.0", port=port, debug=True)
