const $guessInput = $('#guess')
const $submitForm = $('.guess-form')
const submitRoute = 'http://127.0.0.1:5000/submit-guess'
let guess

$submitForm.on('submit', async function(e) {
    e.preventDefault()
    guess = $guessInput.val()
    data = JSON.stringify({ guess })
    await axios({
        method: 'post',
        url: 'http://127.0.0.1:5000/submit-guess',
        data,
        headers: {'Content-Type': 'application/json'}
    })
})

$submitForm.on('submit', async function(e) {
    e.preventDefault()
    guess = $guessInput.val()
    data = JSON.stringify({ guess })
    await axios({
        method: 'post',
        url: 'http://127.0.0.1:5000/submit-guess',
        data,
        headers: {'Content-Type': 'application/json'}
    })
})