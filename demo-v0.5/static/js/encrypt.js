/****************************************************/
/*filename:encrypt.js
/*date:20200722
/*author:elegance
/****************************************************/

function encrypt(){
    $("#source").val(CryptoJS.AES.encrypt($("#source").val(),$("#encryptkey").val()));
}

function get_tips(){
    alert("Keep the Encrypt Key in your mind, and you would need it one day!!!");
}