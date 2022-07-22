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
        console.log(e)
    }
})
