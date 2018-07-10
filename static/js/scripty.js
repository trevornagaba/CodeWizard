$(document).ready(function(){
    console.log("loaded")
    $.material.init();

    $(document).on("submit","#register-form",function(e){
        e.preventDefault();
        console.log("form submitted");
        var form = $("#register-form").serialize();
        $.ajax({
             url: '/postregistration',
            type: 'POST',
            data: form,
            success: function(response){
                console.log(response);
            }
        });
    });

    $(document).on("submit","#login-form",function(e){
        e.preventDefault();
        console.log("form submitted");
        var form = $("#login-form").serialize();
        $.ajax({
             url: '/checklogin',
            type: 'POST',
            data: form,
            success: function(response){
                if (response == "error"){
                    alert("Could not login in");
                }else{
                    console.log("Logged in as ", response);
                    window.location.href = "/"
                }
            }
        });
    });

    $(document).on("click","#logout-link",function(e){
        e.preventDefault();
        console.log("logged out");
        $.ajax({
            url: "/logout",
            type: "GET",
            success: function(res){
                if (res == "success"){
                    window.location.href = "/"
                }
            }
        })
    })

    $(document).on("submit","#post-activity",function(e){
        e.preventDefault();
        console.log("Activity posted");
        form = $("#post-activity").serialize();
        $.ajax({
            url: "/postactivity",
            type: "POST",
            data: form,
            success: function(res){
                if (res == "success"){
                    window.location.href = window.location.href;
                }
            }
        })
    })
});

