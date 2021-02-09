

function searchPhotos(page, same_query) {
    $("#unsplash-result").empty()
    var clientId = "_hroQ78FgqxUtAV5tp754dm3yc7ifI4cTqcT249YzjM"
    // console.log(same_query)
    if (same_query) {
        var query = same_query
    } else {
        var query = $("#search").val()
    }   
    
    var url = "https://api.unsplash.com/search/photos/?client_id=" + clientId + "&query=" + query +"&orientation=landscape&per_page=9&page=" + page 
    // console.log(url)

    fetch(url)
    .then(function (data){
        return data.json()
    })
    .then(function (data){
        // console.log(data)
        data.results.forEach(photo => {
            let result = `
            <div class = "col-4 my-2">
               <img data-raw=${photo.urls.full} style = "height:300px;" class = "img-thumbnail unsplash-photo" src = "${photo.urls.small}">
            </div>
            `
            $("#unsplash-result").append(result)

        
        })
        let clear = `<button type = "button" id="clear" class = "mx-3 btn btn-dark"> clear </button>`
        let next = `<button type = "button" id="next" class = " mx-1 btn btn-dark"> next </button>`
        let previous = `<button type = "button" id="previous" class = "mx-1 btn btn-dark"> previous </button>`
        if (page === 1){
            $("#unsplash-result").append(clear)
            $("#unsplash-result").append(next)
        } else {
            $("#unsplash-result").append(clear)
            $("#unsplash-result").append(previous)
            $("#unsplash-result").append(next)
        }

        $("#previous").on('click',function () {
            searchPhotos(page - 1, query)
        })

        $("#next").on('click',function () {
            searchPhotos(page + 1, query)
        })

        $("#clear").on('click',function () {
            $("#unsplash-result").empty()
            $("#search").val("")
            $("#cover").prop("disabled", false)
        })

        $(".unsplash-photo").on('click', function () {
            if ($(this).hasClass("selected")) {
                $(this).removeClass("selected")
                $("#cover").prop("disabled", false)
            } else {
                $(".unsplash-photo").removeClass("selected")
                $(this).addClass("selected")
                $("#cover").prop("disabled", true)
                var full_photo = $(this).data("raw")
            }
            
        })
        

       
    })
}

    



    