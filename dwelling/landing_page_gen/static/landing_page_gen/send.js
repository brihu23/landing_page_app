$(document).ready(function () {

    
   

    
    $("#main-form").submit(function(event){
        event.preventDefault()
        var company_name = $("#company-name").val()
        var company_tagline = $("#company-tagline").val()
        var phone = $("#number").val()
        var cover_unsplash = null;
        $(".unsplash-photo").each(function() {
            if ($(this).hasClass("selected")){
                cover_unsplash = $(this).data("raw")
            }
        })
        
        var cover_upload = $("#cover-target").prop('src') ? $("#cover-target").prop('src') : ""
        var about_upload = $("#about-target").prop('src') ? $("#about-target").prop('src') : ""
        var logo = $("#logo-target").prop('src') ? $("#logo-target").prop('src') : ""
        
        

        var insured = $("#insured").is(":checked")
        var bonded = $("#bonded").is(":checked")
        var emergency = $("#emergency").is(":checked")
        var veteran = $("#veteran").is(":checked")
        var family = $("#family").is(":checked")
        var local = $("local").is(":checked")
        var license = $("#license").val()
        var about = $("#about").val()
        var slug = $("#slug").val()
        

        var facebook = $("#facebook").val()
        var instagram = $("#instagram").val()
        var twitter = $("#twitter").val()
        var feature = $("#feature").val()

        var street = $("#street").val()
        var city = $("#city").val()
        var state = $("#state").val()
        var zip = $("#zip").val()
        var radius = $("#radius").val()

        // var geocoder = new google.maps.Geocoder();
        
        // var latitude
        // var longitude
        // geocoder.geocode( { 'address': address}, function(results, status) {

        //     if (status == google.maps.GeocoderStatus.OK) {
        //         latitude = results[0].geometry.location.lat();
        //         longitude = results[0].geometry.location.lng();
        //         alert(latitude, longitude);
        //         } 
        // });

        
        var address = street + "," + city + "," + state + ","
        address = address.replace(/ /g, "+")

        var services = []
        var testimonials = []
        var faqs = []

        create_dynamic_object("service", services)
        create_dynamic_object("testimonial", testimonials)
        create_dynamic_object("faq", faqs)

        function create_dynamic_object (group_name, group_array) {
            $("." + group_name).each(function() {
                var dict = {}
                console.log($('this input'))
                // console.log($(this).find(':input'))
                $(this).find("input[type=text]").each(function() {
                    dict[ $(this).attr('name') ] = $(this).val()
                })
                $(this).find("input[type=number]").each(function() {
                    dict[ $(this).attr('name') ] = $(this).val()
                })
                $(this).find("textarea").each(function() {
                    dict[ $(this).attr('name') ] = $(this).val()
                })
               
                group_array.push(dict)        
            })        

        }    

        var gallery_array = []
        $("#gallery-wrapper").children().each(function() {
        console.log($(this).find('img'))
        var image =  $(this).find('img').prop('src')
        gallery_array.push(image)
        })

        console.log(company_name);  console.log( company_tagline); console.log( phone ); console.log(cover_unsplash); console.log( cover_upload); console.log( insured); console.log( bonded); console.log( emergency); console.log( veteran); console.log( family); console.log( local); console.log( license); console.log(
            about); console.log( about_upload); console.log( facebook); console.log( instagram); console.log( twitter); console.log( feature); console.log( street); console.log( city); console.log( state); console.log( zip); console.log( radius); console.log( services); console.log( testimonials); console.log( faqs); console.log( gallery_array)
        
        fetch('/create', {
            method: 'POST',
            body: JSON.stringify({
                company_name: company_name,
                company_tagline: company_tagline,
                phone: phone,
                logo: logo,
                slug: slug,
                cover_unsplash: cover_unsplash,
                cover_upload: cover_upload,
                insured: insured,
                bonded: bonded,
                emergency: emergency,
                veteran: veteran,
                family: family,
                local: local,
                license: license,
                address: address,
                about: about,
                about_upload: about_upload,
                facebook: facebook,
                instagram: instagram,
                twitter: twitter,
                feature: feature,
                street: street,
                city: city,
                state:state,
                zip: zip,
                radius: radius,
                services: services,
                testimonials: testimonials,
                faqs: faqs,
                gallery: gallery_array    
            })
    
        })    
        .then(response => response.text())
        .then(result => {
                // Print result
                //console.log(result);
                location.replace("/" + slug)
                
            
        });  
        })

        
 



    


})