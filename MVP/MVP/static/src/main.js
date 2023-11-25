$(".files").css('display','none');
$(".update").css('display','none');

var namefileUpadet="";
var namefileObr="";
var namefileUpadetF;
var namefileObrF;

$(".button_collection div").click(function(){
    $(".button_collection").css('top','100px');
})

$(".button_overfitting").click(function(){
    $(".files").css('display','none');
    $(".update").css('display','block');
    $('.files .result p').html("Здесь будет отабражён результат");
})

$(".button_workforal").click(function(){
    $(".update").css('display','none');
    $(".files").css('display','block');
    $('.update .result p').html("Здесь будет отабражён результат");
})


$(".update .upload-file__wrapper input[type='file']").change(function(){
    $(".update .upload-file__wrapper .upload-file__label").empty().append(this.files[0].name);
    namefileUpadet=this.files[0].name;
    namefileUpadetF=this.files[0];
});

$(".files .upload-file__wrapper input[type='file']").change(function(){
    $(".files .upload-file__wrapper .upload-file__label").empty().append(this.files[0].name);
    namefileObr=this.files[0].name;
    namefileObrF=this.files[0];
});


$(document).ready(function (e) {
    $('.files #upload').on('click', function () {
        var form_data = new FormData();
        
        if(namefileObr == "") {
            $('.files .result p').html('Файл не выбран.');
            return;
        }else{
            $('.files .result p').html("Файл успешно отправлен на обработку.<br>Пожалуйста ожидайте");
        }
        
        form_data.append("files[]", namefileObrF);
        
        csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
        
        //console.log(csrf_token);
        
        form_data.append("csrfmiddlewaretoken", csrf_token);
        
        $.ajax({
            url: 'uploadreles/', // point to server-side URL
            dataType: 'json', // what to expect back from server
            cache: false,
            contentType: false,
            processData: false,
            //data: {'data': form_data, 'csrfmiddlewaretoken': csrf_token},
            data: form_data,
            type: 'post',
            success: function (response) { // display success response
                $('.files .result p').html(response.msg);
            },
            error: function (response) {
                $('.files .result p').html(response.message); // display error response
            }
        });
    });

    $('.update #upload').on('click', function () {
        var form_data = new FormData();
        
        if(namefileUpadet == "") {
            $('.update .result p').html('Файл не выбран.');
            return;
        }else{
            $('.update .result p').html("Файл успешно отправлен на обработку.<br>Пожалуйста ожидайте");
        }
        
        form_data.append("files[]", namefileUpadetF);
        
        csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
        
        //console.log(csrf_token);
        
        form_data.append("csrfmiddlewaretoken", csrf_token);
        
        $.ajax({
            url: 'uploaddatacheck/', // point to server-side URL
            dataType: 'json', // what to expect back from server
            cache: false,
            contentType: false,
            processData: false,
            //data: {'data': form_data, 'csrfmiddlewaretoken': csrf_token},
            data: form_data,
            type: 'post',
            success: function (response) { // display success response
                $('.update .result p').html(response.msg);
            },
            error: function (response) {
                $('.update .result p').html(response.message); // display error response
            }
        });
    });
});