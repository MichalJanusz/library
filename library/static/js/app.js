console.log('test')

let table = $('#table-results')

table.hide()

function googleBookSearch() {
    let title = $('#ajax-title').val()
    let author = $('#ajax-author').val()
    let isbn = $('#ajax-isbn').val()
    let result = $('#tbody-results')
    console.log(`search ${title}, ${author}, ${isbn}`)
}

document.getElementById('ajax-button').addEventListener('click', googleBookSearch, false)