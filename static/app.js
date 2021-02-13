const $userGuess = $('#guess')
const $submitForm = $('.guess-form')
let formValue

$submitForm.on('submit', function(e) {
    e.preventDefault()
    formValue = $userGuess.val()
})