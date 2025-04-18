let roundsWon = 0;
let roundsLost = 0;
let currentSum = 0;
let attemptsLeft = 3;

const startRoundButton = document.getElementById('startRound');
const playGuessButton = document.getElementById('playGuess');
const resetGameButton = document.getElementById('resetGame');
const guessInput = document.getElementById('guessInput');
const message = document.getElementById('message');
const attemptsDisplay = document.getElementById('attempts');
const historyLog = document.getElementById('historyLog');
const winsDisplay = document.getElementById('wins');
const lossesDisplay = document.getElementById('losses');

function jogue_dados() { //Gera um número aleatório entre 1 e 6, simulando o lançamento de um dado.
    return Math.floor(Math.random() * 6) + 1;
}

function comece_rodada() { //Inicia uma nova rodada, atualiza a soma dos dados, e habilita o botão de jogar.
    const die1 = jogue_dados(); 
    const die2 = jogue_dados();
    currentSum = die1 + die2;
    attemptsLeft = 3;
    
    document.getElementById('gameSection').style.display = 'block';
    guessInput.disabled = false;
    playGuessButton.disabled = false;
    message.textContent = '';
    attemptsDisplay.textContent = `Tentativas restantes: ${attemptsLeft}`;
    
    historyLog.value += `Rodada Iniciada. Adivinhe a soma dos dados.\n`;
}

function comece_adivinhar() { //Verifica o palpite do usuário e atualiza o placar e o histórico conforme necessário.
    const tentativa_usuario = parseInt(guessInput.value, 10);
    
    if (tentativa_usuario === currentSum) {
        message.textContent = 'Parabéns! Você acertou!';
        roundsWon++;//rounswon mantêm o placar do jogo.
        winsDisplay.textContent = roundsWon;
        historyLog.value += `Palpite: ${userGuess} - Acertou! Soma: ${currentSum}\n`;// currentsum guarda a soma atual dos dados.
        final_rodada();
    } else {
        attemptsLeft--;//attemptsleft controla o número de tentativas restantes.
        if (attemptsLeft > 0) {//attemptsleft controla o número de tentativas restantes.
            message.textContent = `Incorreto. Tente novamente!`;
            attemptsDisplay.textContent = `Tentativas restantes: ${attemptsLeft}`;
            historyLog.value += `Palpite: ${userGuess} - Errado. Soma: ${currentSum}\n`;// currentsum guarda a soma atual dos dados
        } else {
            message.textContent = 'Você perdeu! A soma era: ' + currentSum;// currentsum guarda a soma atual dos dados
            roundsLost++;// roundlost mantêm o placar do jogo.
            lossesDisplay.textContent = roundsLost;//roundlost mantêm o placar do jogo.
            historyLog.value += `Palpite: ${userGuess} - Errado. Soma: ${currentSum}\n`;// currentsum guarda a soma atual dos dados
            final_rodada(); 
        }
    }
}

function final_rodada() { // Desabilita os controles de entrada após o fim da rodada.
    guessInput.disabled = true;
    playGuessButton.disabled = true;//Verifica o palpite do usuário e atualiza o placar e o histórico conforme necessário.
}

function redefinir_jogo() { //Zera o placar e o histórico e oculta a seção do jogo.
    roundsWon = 0;//mantêm o placar do jogo.
    roundsLost = 0;//mantêm o placar do jogo.
    winsDisplay.textContent = roundsWon;
    lossesDisplay.textContent = roundsLost;
    historyLog.value = '';
    document.getElementById('gameSection').style.display = 'none';
}

startRoundButton.addEventListener('click', comece_rodada);//Inicia uma nova rodada quando o botão é clicado.
playGuessButton.addEventListener('click', comece_adivinhar);//Processa o palpite quando o botão é clicado.
resetGameButton.addEventListener('click', final_rodada);//Reinicia o jogo quando o botão é clicado.
