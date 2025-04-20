from flask import Flask, render_template, send_from_directory, jsonify
import os
from datetime import datetime

app = Flask(__name__, 
    static_folder='../static',
    template_folder='../templates'
)

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

@app.route('/home')
def home():
    return render_template('home.html')

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

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/refresh-balance')
def refresh_balance():
    return jsonify({
        'success': True,
        'balance': SAMPLE_BALANCE
    })

@app.route('/export-wallet')
def export_wallet():
    return jsonify({
        'success': True,
        'address': '0x1234...5678'
    })

# This is required for Vercel
app = app.wsgi_app 
