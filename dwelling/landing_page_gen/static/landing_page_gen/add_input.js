$(document).ready(function () {

    var service_template = $(".service")[0]
    var testimonial_template = $(".testimonial")[0]
    var faq_template = $(".faq")[0]


    $(function add_input(){
        $("#add-service").click(function() {
            
            $(service_template).clone().appendTo("#services")
        })

        $("#add-testimonial").click(function() {
            
            $(testimonial_template).clone().appendTo("#testimonials")
        })

        $("#add-faq").click(function() {
            
            $(faq_template).clone().appendTo("#faqs")
        })
    })



    $(function remove_service(){
        $("#dynamic_components").on('click','.remove',function(){
            console.log($(this).parent())
            $(this).parent().remove()
        })
    })



})