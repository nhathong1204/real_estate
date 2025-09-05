$(document).ready(function() {
    $(document).on("click",".change_language",function(e){
        language = $(this).data("language");
        $("#language-input").val(language);

        // Submit the form
        $("#language-form").submit();

        // Toggle visibility of the images
        if (language === "zh-hans") {
            $(".china-image").hide();
            $(".vietnam-image").show();
        } else {
            $(".china-image").show();
            $(".vietnam-image").hide();
        }
    });

    var current_language = $("#current_language").val()
    console.log("Current language:", current_language);

    // Check current language and set the initial visibility of the images
    if (current_language === "zh-hans") {
        $(".china-image").hide();
        $(".vietnam-image").show();
    } else {
        $(".china-image").show();
        $(".vietnam-image").hide();
    }

    $(document).on("submit","#contact-form-ajax",function(e){
        e.preventDefault()
        $('#btn_submit').attr("disabled", 'disabled');
        $('#btn_submit').text("Đang gửi tin nhắn");
        console.log("Submited...")
        let full_name = $("#full_name").val()
        let email = $("#email").val()
        let phone = $("#phone").val()
        let message = $("#message").val()
        console.log(full_name, email, phone, message)

        $.ajax({
            url: "/ajax-contact-form",
            data: {
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "message": message,
            },
            dataType: "json",
            success: function(res) {
                console.log("Sent data to server...")
                if(res.success == true) {
                    alert("Tin nhắn gửi thành công. Cảm ơn bạn rất nhiều!")
                    location.reload();
                }
            }
        })
    })
})
