const $guessInput = $('#guess');
const $submitForm = $('.guess-form');
const submitRoute = 'http://127.0.0.1:5000/submit-guess';
let score = 0;

$submitForm.on('submit', async function(e) {
    e.preventDefault();
    removeScoreAndStatus();

    let guess = $guessInput.val();
    let msg = null;
    let $h3_status_message = $('<h3 class="d-inline mr-3"></h3>');
    let $h3_score_message = $('<h3 class="d-inline"></h3>');

    data = JSON.stringify({ guess })
    const response = await axios.post(
        'http://127.0.0.1:5000/submit-guess',
        data,
        {headers: {'Content-Type': 'application/json'}}
    )
    placeStatusOnPage($h3_status_message, response)
    updateScore(`Status: ${response.data.result}`, guess)
    placeScoreOnPage($h3_score_message, score)
})

function updateScore(message, word) {
    if (message === 'Status: ok') {
        score += word.length
    }
}

function placeStatusOnPage(h3, resp) {
    text = 'Status: ' + resp.data.result;
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
