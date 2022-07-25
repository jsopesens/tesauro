// LANDING PAGE -> CLICK ON LI MAKE REDIRECT TO KEYWORD PAGE
// EVENT DELEGATION!
// At clicking on svg element, we aren't redirected
var fullKeywordList = document.getElementById('fullListKeywords')
fullKeywordList.addEventListener('click', e => {
    if(e.target && e.target.matches('li.keyword')){
        e.target.children[0].click()
    }
})

// click on svg to ajax call childs
fullKeywordList.addEventListener('click', e =>{
    if(e.target && e.target.matches('svg.showMore')){
        let father    = e.path[1]
        let svg       = e.path[0]
        let innerList = father.querySelector('ul')
        let endpoint = '/keywords/getSonsOf/'
        let keyword  = e.path[1].id

        // is list of sons visible?
        // if it is, hide it
        if(innerList && innerList.style.display == 'block'){
            svg.setAttribute('transform', 'rotate(0)')
            innerList.style.display = 'none'
        }
        // isn't visible, so show it
        else{
            // First Deployment? so do ajax call
            if(!innerList){
                fetch(endpoint + keyword)
                .then(response => response.json())
                .then(data => showSons(e, data))
            }

            // not first deployment, only need to show it
            svg.setAttribute('transform', 'rotate(90)')
            innerList.style.display = 'block' 
        }
    }
})

function showSons(e, data){
    parentElement = e.path[1]
    const lu = document.createElement('ul')
    parentElement.appendChild(lu)
    data['topConcepts'].forEach(element => {
        const li = document.createElement('li')
        const a  = document.createElement('a')
        li.classList = 'keyword'
        a.href      = element
        a.innerHTML = element
        li.appendChild(a)
        lu.appendChild(li)
    });
}