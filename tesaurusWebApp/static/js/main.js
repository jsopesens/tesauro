var searchInput = document.getElementById('searchQueryInput')
var endpoint = '/keywords/getMatchKeywords/'
searchInput.addEventListener('input', getMatchKeywords)

function getMatchKeywords(){
    input = this.value,

    // GET MODE
    fetch(endpoint+this.value)
    .then(response => response.json())
    .then(data=>{
        console.log(data)
    })

    // POST MODE
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