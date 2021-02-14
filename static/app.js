const $guessInput = $('#guess');
const $submitForm = $('.guess-form');
const submitRoute = 'http://127.0.0.1:5000/submit-guess';
const statsRoute = 'http://127.0.0.1:5000/statistics';
const setOfSeenWords = new Set();
let score = 0;

$submitForm.on('submit', async function(e) {
    e.preventDefault();
    removeScoreAndStatus();

    let guess = $guessInput.val();
    let msg = null;
    let $h3_status_message = $('<h3 class="d-inline mr-3"></h3>');
    let $h3_score_message = $('<h3 class="d-inline"></h3>');
    const headers = {'Content-Type': 'application/json'};
    const data = JSON.stringify({ guess })
    const request = new Request(submitRoute, data, headers)
    const message = await request.getResponseMessage();

    placeStatusOnPage($h3_status_message, message);
    updateScore(message, guess);
    placeScoreOnPage($h3_score_message, score);
    setOfSeenWords.add(guess);
})

function updateScore(message, word) {
    if (message === 'ok' && !hasBeenSeen(word)) {
        score += word.length
    }
}

function placeStatusOnPage(h3, message) {
    text = 'Status: ' + message;
    h3.text(text);
    if (h3.text() === 'Status: ok') {
        h3.css('color', 'green');
    }
    else {
        h3.css('color', 'red');
    }
    h3.prependTo('body');
}

function placeScoreOnPage(scoreH3, score) {
    score_text = 'Score: ' + score;
    scoreH3.css('color', 'green').text(score_text);
    $('h3').after(scoreH3);
}

function removeScoreAndStatus() {
    $('h3').remove();
}

function hasBeenSeen(guess) {
    if (setOfSeenWords.has(guess)) {
        return true
    }
}

async function sendStatisticsToServer() {
    const data = JSON.stringify({ score })
    const headers = {'Content-Type': 'application/json'};
    const request = new Request(statsRoute, data, headers)
    await request.sendRequest();
    return;
}

setTimeout(async function() {
    $('button').attr('type', 'button');
    await sendStatisticsToServer();
}, 60000)

