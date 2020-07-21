/****************************************************/
/*filename:decrypt.js
/*date:20200721
/*author:elegance
/****************************************************/

function decrypt(){
    $("#source").val(CryptoJS.AES.decrypt($("#source").val(),$("#decryptkey").val()).toString(CryptoJS.enc.Utf8));
}