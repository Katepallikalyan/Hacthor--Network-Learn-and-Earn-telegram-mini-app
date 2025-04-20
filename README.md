# Learn & Earn - Web3 Learning Platform

A browser-based Web3 educational platform that rewards users with tokens for completing quizzes and participating in governance.

## Features

- Interactive quizzes with token rewards
- Wallet integration with Hathor Network
- Governance voting system
- Modern, responsive UI
- Token rewards for quiz completion
- Bonus tokens for voting and completing voted topics

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/learn-and-earn.git
cd learn-and-earn
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
learn-and-earn-app/
├── app.py                        # Main Flask app
├── requirements.txt              # Python dependencies
├── contracts/
│   └── LearnAndEarn.sol          # Smart contract
├── templates/
│   ├── home.html                 # Home UI
│   ├── quiz.html                 # Quiz interface
│   ├── result.html              # Quiz results
│   ├── wallet.html              # Wallet interface
│   └── governance.html          # Voting interface
├── static/
│   ├── style.css                # CSS styling
│   └── webapp.js                # Frontend logic
└── utils/
    └── wallet.py                # Wallet & blockchain helpers
```

## Usage

1. **Taking Quizzes**
   - Click "Start Quiz" on the home page
   - Select a quiz topic
   - Answer questions to earn tokens
   - Pass mark is 60%

2. **Managing Wallet**
   - View your token balance
   - Check transaction history
   - Export wallet address

3. **Governance**
   - Vote on upcoming quiz topics
   - Earn bonus tokens for voting
   - Complete voted topics for extra rewards

## Development

- The application uses Flask for the backend
- Frontend is built with HTML, CSS, and JavaScript
- Hathor Network integration for token management
- No database required (stateless design)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Hathor Network for blockchain integration
- Flask for the web framework
- All contributors and users of the platform 