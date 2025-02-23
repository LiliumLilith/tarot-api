from flask import Flask, jsonify
import random

app = Flask(__name__)

# Tarot kartları listesi
tarot_cards = [
    {"name": "The Fool", "meaning": "Yeni başlangıçlar, saflık, macera"},
    {"name": "The Magician", "meaning": "Güç, yaratıcılık, kontrol"},
    {"name": "The High Priestess", "meaning": "Bilinçaltı, içgörü, gizem"},
    {"name": "The Empress", "meaning": "Bolluk, doğurganlık, doğa"},
    {"name": "The Emperor", "meaning": "Otorite, yapı, düzen"},
    {"name": "The Hierophant", "meaning": "Bilgelik, rehberlik, gelenek"},
    {"name": "The Lovers", "meaning": "Aşk, birlik, seçenekler"},
    {"name": "The Chariot", "meaning": "Zafer, kontrol, irade gücü"},
    {"name": "Strength", "meaning": "Cesaret, sabır, güç"},
    {"name": "The Hermit", "meaning": "Yalnızlık, içe dönüş, bilgelik"},
    {"name": "Wheel of Fortune", "meaning": "Kader, değişim, döngü"},
    {"name": "Justice", "meaning": "Denge, doğruluk, adalet"},
    {"name": "The Hanged Man", "meaning": "Teslimiyet, farklı bakış açısı"},
    {"name": "Death", "meaning": "Dönüşüm, değişim, yenilenme"},
    {"name": "Temperance", "meaning": "Denge, uyum, sabır"},
    {"name": "The Devil", "meaning": "Bağımlılık, materyalizm, gölge yan"},
    {"name": "The Tower", "meaning": "Ani değişim, yıkım, şok"},
    {"name": "The Star", "meaning": "Umut, ilham, iyileşme"},
    {"name": "The Moon", "meaning": "Bilinçaltı, hayaller, korkular"},
    {"name": "The Sun", "meaning": "Neşe, başarı, pozitif enerji"},
    {"name": "Judgement", "meaning": "Uyanış, karar verme, dönüşüm"},
    {"name": "The World", "meaning": "Tamamlanma, başarı, bütünlük"}
]

# Rastgele bir kart seçen endpoint
@app.route('/tarot', methods=['GET'])
def draw_tarot():
    card = random.choice(tarot_cards)
    return jsonify(card)

# Flask uygulamasını başlat
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
