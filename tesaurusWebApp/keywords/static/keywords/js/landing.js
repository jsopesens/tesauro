// LANDING PAGE -> CLICK ON LI MAKE REDIRECT TO KEYWORD PAGE
// EVENT DELEGATION!
// At clicking on svg element, we aren't redirected
var fullKeywordList = document.getElementById('fullListKeywords')
fullKeywordList.addEventListener('click', e => {
    if (e.target && e.target.matches('li.keyword')) {
        e.target.children[0].click()
    }
})

// click on svg to ajax call childs
fullKeywordList.addEventListener('click', e => {
    if (e.target && e.target.matches('svg.showMore')) {
        let fatherKeyword = e.path[1]
        let svg = e.path[0]
        let innerList = fatherKeyword.querySelector('ul')
        let endpoint = '/keywords/getSonsOf/'
        let keywordName = e.path[1].id
        
        rotateSVG(svg)

        if (!innerList) {
            // generate content and show it
            fetch(endpoint + keywordName)
                .then(response => response.json())
                .then(data => showSons(fatherKeyword, data))
        }
        if(innerList){
            // only need to hide or show it
            displayListContent(innerList)
        }
    }
})

function displayListContent(list){
    const currentDisplay = list.style.display 
    list.style.display = currentDisplay == 'block' ? 'none': 'block'
}

function rotateSVG(svg) {
    const rotation = svg.getAttribute('transform')
    svg.setAttribute('transform', rotation == 'rotate(0)' ? 'rotate(90)' : 'rotate(0)')
}

function showSons(fatherKeyword, data) {
    const lu = document.createElement('ul')
    lu.style.display = 'block'
    fatherKeyword.appendChild(lu)
    data['topConcepts'].forEach(element => {
        const li = document.createElement('li')
        const a = document.createElement('a')
        li.classList = 'keyword'
        a.href = element
        a.innerHTML = element
        li.appendChild(a)
        lu.appendChild(li)
    });
}