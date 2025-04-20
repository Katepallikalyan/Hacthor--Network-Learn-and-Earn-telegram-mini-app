// Global state management
const state = {
    currentQuiz: null,
    currentQuestion: 0,
    answers: [],
    walletBalance: 0
};

// Quiz functionality
function initializeQuiz(quizData) {
    state.currentQuiz = quizData;
    state.currentQuestion = 0;
    state.answers = new Array(quizData.questions.length).fill(null);
    loadQuestion(0);
}

function loadQuestion(index) {
    const question = state.currentQuiz.questions[index];
    const quizContent = document.getElementById('quiz-content');
    
    if (!quizContent) return;

    quizContent.innerHTML = `
        <div class="question-progress">
            <p>Question ${index + 1} of ${state.currentQuiz.questions.length}</p>
        </div>
        <h3>${question.question}</h3>
        <div class="options">
            ${question.options.map((option, i) => `
                <div class="option" onclick="selectAnswer(${i})">
                    ${option}
                </div>
            `).join('')}
        </div>
    `;

    updateNavigationButtons();
}

function selectAnswer(answerIndex) {
    state.answers[state.currentQuestion] = answerIndex;
    const options = document.querySelectorAll('.option');
    options.forEach((option, i) => {
        option.classList.toggle('selected', i === answerIndex);
    });
}

function updateNavigationButtons() {
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const submitBtn = document.getElementById('submit-btn');

    if (prevBtn) {
        prevBtn.style.display = state.currentQuestion > 0 ? 'inline' : 'none';
    }
    if (nextBtn) {
        nextBtn.style.display = state.currentQuestion < state.currentQuiz.questions.length - 1 ? 'inline' : 'none';
    }
    if (submitBtn) {
        submitBtn.style.display = state.currentQuestion === state.currentQuiz.questions.length - 1 ? 'inline' : 'none';
    }
}

// Wallet functionality
function refreshWalletBalance() {
    fetch('/refresh-balance')
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                state.walletBalance = data.balance;
                updateWalletDisplay();
            }
        });
}

function updateWalletDisplay() {
    const balanceElement = document.querySelector('.balance-amount');
    if (balanceElement) {
        balanceElement.textContent = `${state.walletBalance} LNE`;
    }
}

// Governance functionality
function submitVote(pollId) {
    fetch('/api/vote', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            poll_id: pollId
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            updatePollDisplay(pollId);
        } else {
            alert('Error: ' + data.message);
        }
    });
}

function updatePollDisplay(pollId) {
    const pollCard = document.querySelector(`[data-poll-id="${pollId}"]`);
    if (pollCard) {
        const voteButton = pollCard.querySelector('.vote-button');
        if (voteButton) {
            voteButton.textContent = 'Voted';
            voteButton.disabled = true;
        }
    }
}

// Animation utilities
function showConfetti() {
    const colors = ['#6c5ce7', '#a8a4e6', '#ffffff'];
    for (let i = 0; i < 50; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        confetti.style.left = Math.random() * 100 + 'vw';
        confetti.style.animationDuration = (Math.random() * 3 + 2) + 's';
        confetti.style.opacity = Math.random();
        document.body.appendChild(confetti);
        
        setTimeout(() => {
            confetti.remove();
        }, 5000);
    }
}

// Event listeners
document.addEventListener('DOMContentLoaded', () => {
    // Initialize wallet balance if on wallet page
    if (document.querySelector('.balance-amount')) {
        refreshWalletBalance();
    }

    // Initialize quiz if on quiz page
    const quizData = document.getElementById('quiz-data');
    if (quizData) {
        initializeQuiz(JSON.parse(quizData.textContent));
    }
}); 