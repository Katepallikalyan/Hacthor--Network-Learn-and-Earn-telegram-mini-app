from flask import Flask, render_template, send_from_directory, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Sample data for testing
SAMPLE_BALANCE = 1000
SAMPLE_TRANSACTIONS = [
    {
        'type': 'reward',
        'description': 'Quiz Completion Reward',
        'date': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'amount': 50
    },
    {
        'type': 'vote',
        'description': 'Governance Vote',
        'date': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'amount': -10
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wallet')
def wallet():
    return render_template('wallet.html', 
                         balance=SAMPLE_BALANCE,
                         transactions=SAMPLE_TRANSACTIONS)

@app.route('/governance')
def governance():
    return render_template('governance.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/refresh-balance')
def refresh_balance():
    # In a real app, this would fetch the actual balance from the blockchain
    return jsonify({
        'success': True,
        'balance': SAMPLE_BALANCE
    })

@app.route('/export-wallet')
def export_wallet():
    # In a real app, this would generate or retrieve the actual wallet address
    return jsonify({
        'success': True,
        'address': '0x1234...5678'  # Sample wallet address
    })

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  
