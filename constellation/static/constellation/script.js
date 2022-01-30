function submitthis(consname) {
    document.querySelector("#possform")['solution'].value = consname
    console.log(document.querySelector("#possform")['solution'])
    document.querySelector("#possform").submit()
    document.querySelector
}

function getcontent(solname) {
    $ajaxUtils.sendGetRequest("{% static 'star-data.json'%}", 
    function(res){
        consname = res[solname].name
        conscontent = res[solname].desc
        document.querySelector(".header").innerHTML = consname
        document.querySelector(".content").innerHTML = conscontent
    })
}
