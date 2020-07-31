/****************************************************/
/*filename:decrypt.js
/*date:20200722
/*author:elegance
/****************************************************/

function decrypt(){
    $("#source").val(CryptoJS.AES.decrypt($("#source").val(),$("#decryptkey").val()).toString(CryptoJS.enc.Utf8));
}

function get_tips(){
    alert('When it comes to error code, maybe you encrypted it.');
}