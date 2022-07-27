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
        let keywordName = e.path[1].id
        
        rotateSVG(svg)

        if (!innerList) {
            // generate content and show it
            fetch('/keywords/getChildrenOf/' + keywordName)
                .then(response => response.json())
                // .then(data => showSons(fatherKeyword, data))
                .then(function(data){
                    console.log(data)
                    // showSons(fatherKeyword, data)
                })
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

    Object.entries(data['sons']).forEach(([key, value]) => {
        const li = document.createElement('li')
        const a = document.createElement('a')
        li.classList = 'keyword'
        li.id = key
        a.href = key
        a.innerHTML = key
        li.appendChild(a)
        if (value == 1){
            addTriangleSVG(li)
        }
        lu.appendChild(li)
    })
}

function addTriangleSVG(li){
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    const path = document. createElementNS("http://www.w3.org/2000/svg", "path")

    svg.setAttribute('width', 20)
    svg.setAttribute('height', 20)
    svg.setAttribute('fill', 'currentColor')
    svg.setAttribute('viewBox', '0 0 15 15')
    svg.setAttribute('transform', 'rotate(0)')
    svg.classList = 'showMore'
    path.setAttributeNS(null, "d", "M6 12.796V3.204L11.481 8 6 12.796zm.659.753 5.48-4.796a1 1 0 0 0 0-1.506L6.66 2.451C6.011 1.885 5 2.345 5 3.204v9.592a1 1 0 0 0 1.659.753z")
    
    svg.appendChild(path)
    li.appendChild(svg)
}