/****************************************************/
/*filename:time.js
/*date:20200721
/*author:elegance
/****************************************************/

var secEl = document.getElementById('sec');
if (secEl) {
    var sec = parseInt(secEl.innerHTML);
    setInterval(function(){
        sec--;
        if (sec >= 0) {
            secEl.innerHTML = sec;
        } else {

        }
    },1000);
}