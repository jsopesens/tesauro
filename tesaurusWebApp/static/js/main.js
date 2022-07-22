var searchInput = document.getElementById('searchQueryInput')
var endpoint    = '/keywords/getMatchKeywords/'


searchInput.addEventListener('input', function () {
    showMatchKeywords(searchInput.value);
})
// SEARCHBAR -> CLICK ON LI ELEMENT MAKE REDIRECT TO KEYWORD PAGE
var keyword_list = document.getElementById('keywords_list')
keyword_list.addEventListener('click', e =>
    e.target.children[0].click()
)
// SEARCHBAR -> ON CLICK OUT, HIDE SUGGESTION LIST
searchInput.addEventListener('focusout', () => {
    // Make it wait in order to redirect instead of simply hide element
    setTimeout(()=>{
        keyword_list.style.display = 'none';
    }, 200)
})

searchInput.addEventListener('focusin', () => 
    keyword_list.style.display = 'block'
)


function showMatchKeywords(searchText) {
    let keywordsList = document.getElementById('keywords_list')
    let keywordsContainer = document.getElementById('navBarContainer')
    // GET MODE
    // search input with only whitespaces generates errors on the HTTP request
    if (searchText.trim() != '') {
        fetch(endpoint + searchText)
            .then(keywordsList.innerHTML = '')
            .then(response => response.json())
            .then(data => convertToListElements(data.keywords))
    } else
        keywordsContainer.style.display = 'none'
    // POST MODE
    // input = this.value,
    // fetch( endpoint+this.value,{
    //     method: "POST",
    //     headers:{
    //         "X-CSRFToken": csrf,
    //     },
    //     body: JSON.stringify(input)
    // }).then(response => response.json())
    // .then(data=>{
    //     console.log(data)
    // })
}

function convertToListElements(data) {
    data.forEach(element => {
        const li = document.createElement('li')
        const a = document.createElement('a')
        li.classList.add('keyword_suggestion')
        a.href = element
        a.innerHTML = element
        li.appendChild(a)
        document.getElementById('keywords_list').appendChild(li)
    });
    // I SUSPECT THAT THERE IS NOT THE BEST PLACE FOR THIS FUNCTION.
    // I HAVE TO TRY TO CHANGE HIS PLACE
    showSuggestions()
}

function showSuggestions() {
    const keywordDOM = document.getElementById('navBarContainer')
    const keywordsList = document.getElementById('keywords_list')

    keywordDOM.style.display =
        (keywordsList.childElementCount === 0 || searchInput.value == '') ?
            'none' :
            'block'
}
