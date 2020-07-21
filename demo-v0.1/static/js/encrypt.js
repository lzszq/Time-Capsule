/****************************************************/
/*filename:encrypt.js
/*date:20200721
/*author:elegance
/****************************************************/

function encrypt(){
    $("#source").val(CryptoJS.AES.encrypt($("#source").val(),$("#encryptkey").val()));
}