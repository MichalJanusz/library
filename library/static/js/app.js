let table = $('#table-results')
let csrf_token = $('#csrf_token').val()

table.hide()

function googleBookSearch() {
    let search = $('#ajax-search').val().replace(/\s+/g, '+')

    let results = $('#tbody-results')
    results.html('')
    table.show()

    $.ajax({
        url: `https://www.googleapis.com/books/v1/volumes?q=${search}&maxResults=20&printType=books`,
        dataType: 'json'
        })
        .done(function (data) {

            for (let i = 0; i < data.items.length; i++) {

                let imageLinks = data.items[i].volumeInfo.imageLinks
                let thumbnail
                if (typeof imageLinks !== 'undefined') {
                    thumbnail = imageLinks.thumbnail
                } else {
                    thumbnail = ''
                }

                let pageCount = data.items[i].volumeInfo.pageCount
                if (typeof pageCount === 'undefined') {
                    pageCount = ''
                }

                let publishedDate = data.items[i].volumeInfo.publishedDate
                if (typeof publishedDate === 'undefined') {
                    publishedDate = ''
                }

                let industryIdentifiers = data.items[i].volumeInfo.industryIdentifiers
                if (typeof industryIdentifiers === 'undefined') {
                    continue
                }

                results.append(
                    `<tr><form method="post" id="import-form${i}"><input name="csrfmiddlewaretoken" form="import-form${i}" type="hidden" value="${csrf_token}"></form>
                     <th scope="row">${i + 1}</th>
                     <td><input name="title" type="hidden" form="import-form${i}" readonly class="form-control-plaintext" value="${data.items[i].volumeInfo.title}">${data.items[i].volumeInfo.title}</td>
                     <td><input name="author" type="hidden" form="import-form${i}" readonly class="form-control-plaintext" value="${data.items[i].volumeInfo.authors[0]}">${data.items[i].volumeInfo.authors[0]}</td>
                     <td><input name="pub_date" type="hidden" form="import-form${i}" readonly class="form-control-plaintext" value="${publishedDate.split('-')[0]}">${publishedDate.split('-')[0]}</td>
                     <td><input name="isbn" type="hidden" form="import-form${i}" readonly class="form-control-plaintext" value="${industryIdentifiers[0].identifier.replace(/\D/g, '')}">${industryIdentifiers[0].identifier.replace(/\D/g, '')}</td>
                     <td><input name="pages" type="hidden" form="import-form${i}" readonly class="form-control-plaintext" value="${pageCount}">${pageCount}</td>
                     <td><img src="${thumbnail}" alt="book cover missing"><input name="cover" type="hidden" form="import-form${i}" value="${thumbnail}"></td>
                     <td><input name="lang" type="hidden" form="import-form${i}" readonly class="form-control-plaintext" value="${data.items[i].volumeInfo.language}">${data.items[i].volumeInfo.language}</td>
                     <td><input type="submit" class="btn btn-success" form="import-form${i}" value="Import"></td>
                </tr>`
                )
            }

        });
}

document.getElementById('ajax-button').addEventListener('click', googleBookSearch, false)