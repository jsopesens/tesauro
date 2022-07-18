var searchInput = document.getElementById('searchQueryInput')
var csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
var endpoint = '/keywords/getMatchKeywords/'
console.log(endpoint)
searchInput.addEventListener('input', getMatchKeywords)

function getMatchKeywords(){
    var payload={
        input: this.value,
    }

    fetch( endpoint+this.value,{
        method: "POST",
        headers:{
            "X-CSRFToken": csrf,
        },
        body: JSON.stringify(payload)
    }).then(response => response.json())
    .then(data=>{
        console.log(data)
    })
}