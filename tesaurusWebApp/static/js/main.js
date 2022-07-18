var searchInput = document.getElementById('searchQueryInput')
var endpoint = '/keywords/getMatchKeywords/'
searchInput.addEventListener('input', getMatchKeywords)

function getMatchKeywords(){
    // GET MODE
    fetch(endpoint+this.value)
    .then(response => response.json())
    .then(data=>{
        var allLinks
        data.keywords.forEach(element => {
            allLinks +='<li><a href="'+element+'">'+element+'</a></li>'            
        });
        document.getElementById("keywords").innerHTML = allLinks
    })

    keywordsDOM = document.getElementById('keywords')
    if(this.value == '' || keywordsDOM.childElementCount==0){
        keywordsDOM.style.display = 'none'
    }else{
        keywordsDOM.style.display = 'block'
    }

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