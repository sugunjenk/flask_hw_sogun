from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://sumagunawan:sugunjenk10@ac-pig4g6g-shard-00-00.lm8jmgi.mongodb.net:27017,ac-pig4g6g-shard-00-01.lm8jmgi.mongodb.net:27017,ac-pig4g6g-shard-00-02.lm8jmgi.mongodb.net:27017/?ssl=true&replicaSet=atlas-w3dsec-shard-0&authSource=admin&retryWrites=true&w=majority&appName=AtlasApp')
db = client.dbsumagunawan

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    # Dapatkan data dari permintaan POST
    data = request.get_json()
    name = data['name']
    email = data['email']
    message = data['message']

    # Simpan data ke database MongoDB
    messages = db.messages
    new_message = {
        'name': name,
        'email': email,
        'message': message
    }
    messages.insert_one(new_message)

    # Anda dapat memberikan respons ke klien jika diperlukan
    response = {'message': 'Pesan telah berhasil disimpan ke database.'}
    return jsonify(response)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
