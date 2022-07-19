var searchInput = document.getElementById('searchQueryInput')
var endpoint = '/keywords/getMatchKeywords/'

searchInput.addEventListener('input', function(){
    getMatchKeywords(searchInput.value)})

function getMatchKeywords(searchInput){
    // GET MODE
    fetch(endpoint+searchInput)
    .then(response => response.json())
    .then(data=>{
        var allLinks
        data.keywords.forEach(element => {
            allLinks +='<li><a href="'+element+'">'+element+'</a></li>'            
        });
        document.getElementById("keywords").innerHTML = allLinks
    })

    keywordsDOM = document.getElementById('keywords')
    keywordsDOM.style.display = !searchInput ? 'none': 'block'

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