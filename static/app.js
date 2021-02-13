const $guessInput = $('#guess')
const $submitForm = $('.guess-form')
const submitRoute = 'http://127.0.0.1:5000/submit-guess'

$submitForm.on('submit', async function(e) {
    e.preventDefault()
    $('h2').remove()
    let guess = $guessInput.val()
    let msg = null
    let $h2_message = $('<h2 class="ml-4"></h2>')

    data = JSON.stringify({ guess })
    const response = await axios.post(
        'http://127.0.0.1:5000/submit-guess',
        data,
        {headers: {'Content-Type': 'application/json'}}
    )
    
    message = response.data.result
    $h2_message.text(message)
    if ($h2_message.text() === 'ok') {
        $h2_message.css('color', 'green')
    }
    else {
        $h2_message.css('color', 'red')
    }
    $h2_message.prependTo('body')
})



