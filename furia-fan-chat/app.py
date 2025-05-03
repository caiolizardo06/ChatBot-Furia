from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

# Respostas simuladas
RESPONSES = {
    "quando é o próximo jogo da fúria?": "Você pode saber sobre o próximo jogo da Fúria nesse link: https://draft5.gg/equipe/330-FURIA/proximas-partidas",
    "qual é a escalação da fúria?": "A escalação atual da FÚRIA: FalleN, yuurih, KSCERATO, molodoy e YEKINDAR.",
    "quando o time de cs:go da fúria foi criado?": "O time de CS:GO da FÚRIA foi criado em 2017.",
    "quantos títulos de cs:go a fúria conquistou?": "A FÚRIA conquistou mais de 10 títulos importantes no cenário nacional e internacional.",
    "vamos fúria": "VAMOOO FÚRIAAAA 🔥🔥🔥"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get('message', '').lower()
    response = RESPONSES.get(user_message, "Não entendi, mas estamos juntos pela FÚRIA! 🖤")
    timestamp = datetime.datetime.now().strftime("%H:%M")
    return jsonify({'response': response, 'timestamp': timestamp})

if __name__ == '__main__':
    app.run(debug=True)
