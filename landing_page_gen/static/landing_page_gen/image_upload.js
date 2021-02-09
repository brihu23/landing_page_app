var loadFile = function(event, target) {
  var reader = new FileReader();
  reader.onload = function(){
    var output = document.getElementById(target + "-target")
    var clear = `<button type = "button" id="clear-${target}" class = "mt-2 btn btn-dark"> clear </button>`
    if (target === "gallery"){
      
      var img_preview = `
      <div class = "col-3 my-2"> 
        <img src = ${reader.result} class = "img-thumbnail mb-2 rounded float-left img-fluid" id = "${target}-target"></img>
        <button type = "button" class = "remove-${target} d-block mx-auto btn btn-dark"> remove </button>
      </div>
      `
      $("#" + target + "-wrapper").append(img_preview)
      $("#" + target).val("")
      

    } else {
      var img_preview = `<img src = ${reader.result} class = "img-thumbnail rounded float-left img-fluid" id = "${target}-target"></img>`
      $("#" + target + "-wrapper").empty()
      $("#" + target).val("")
      $("#" + target + "-wrapper").append(img_preview)
      $("#" + target + "-wrapper").append(clear)

      if (target === "cover"){
        // console.log("disable unsplash")
        // console.log($("#unsplash-search"))
        $("#unsplash-search").prop("disabled", true)
        
      }
      
    } 
        
    
    $("#clear-" + target ).on('click',function () {
      if (target === "cover"){
        $("#unsplash-search").prop("disabled", false)
      }
      $("#" + target + "-wrapper").empty()
      $("#" + target).val("")
    })

    $(".remove-" + target ).on('click',function () {
     $(this).parent().remove()
    })
  };

  reader.readAsDataURL(event.target.files[0]);
};



