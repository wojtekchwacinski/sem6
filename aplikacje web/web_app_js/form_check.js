


function isEmpty(znaki){
    if (znaki.length == false){
        return true;
    }
    return false;
}

function validate(form){
    let imie = form.elements["f_imie"];
    let nazwiska = form.elements["f_nazwisko"];
    let kod = form.elements["f_kod"];
    let ulica = form.elements["f_ulica"];
    let miasto = form.elements["f_miasto"];
    let email = form.elements["f_email"];
    //let x = isEmpty(odp);
    
    if (checkStringAndFocus(imie, "Podaj, imie!", isWhiteSpaceOrEmpty) == false){
        return false;
    }
    if (checkStringAndFocus(nazwiska, "Podaj, nazwisko!", isWhiteSpaceOrEmpty) == false){
        return false;
    }
    if (checkStringAndFocus(email, "Podaj właściwy e-mail", checkEmail) == false){
        return false;
    }
    if (checkStringAndFocus(kod, "Podaj, kod!", isWhiteSpaceOrEmpty) == false){
        return false;
    }
    if (checkStringAndFocus(ulica, "Podaj, ulice!", isWhiteSpaceOrEmpty) == false){
        return false;
    }
    if (checkStringAndFocus(miasto, "Podaj, miasto!", isWhiteSpaceOrEmpty) == false){
        return false;
    }


    return true
    
}

function isWhiteSpaceOrEmpty(str) {
    return /^[\s\t\r\n]*$/.test(str);
    }


function checkString(znaki, wiadomosc){
    let z = isWhiteSpaceOrEmpty(znaki);
    if (z == true){
        alert(wiadomosc);
        return false;
    }
    else {
        return true;
    }
}

function checkEmail(str) {
    
    return /^[a-zA-Z_0-9\.]+@[a-zA-Z_0-9\.]+\.[a-zA-Z][a-zA-Z]+$/.test(str);
    }


function checkStringAndFocus(obj, msg, fun_wali) {
    let x = fun_wali
    let str = obj.value;
    let errorFieldName = "e_" + obj.name.substr(2, obj.name.length);
 
    if (x == checkEmail){
        if (!fun_wali(str)) {
            document.getElementById(errorFieldName).innerHTML = msg;
            obj.focus();
            return false;
        }
        else {
            document.getElementById(errorFieldName).innerHTML = " ";
            obj.focus();
            return true;
        }
    }


    if (fun_wali(str)) {
        document.getElementById(errorFieldName).innerHTML = msg;
        obj.focus();
        return false;
    }
    else {
        document.getElementById(errorFieldName).innerHTML = " ";
        obj.focus();
        return true;
    }
}

function checkEmailAndFocus(obj, msg) {
    let str = obj.value;
    let errorFieldName = "e_" + obj.name.substr(2, obj.name.length);
    if (checkEmail(str) == false) {
        document.getElementById(errorFieldName).innerHTML = msg;
        obj.focus();
        return false;
    }
    else {
        document.getElementById(errorFieldName).innerHTML = " ";
        obj.focus();
        return true;
    }
}

function showElement(e) {
    document.getElementById(e).style.visibility = 'visible';
    }
function hideElement(e) {
    document.getElementById(e).style.visibility = 'hidden';
    }




    function alterRows(i, e) {
  
        if (e) {
            if (i % 2 == 1) {
                e.setAttribute("style", "background-color: Aqua;");
            }
        e = e.nextSibling;
        while (e && e.nodeType != 1) {
            e = e.nextSibling;
        }
        alterRows(++i, e);
        }
    }
var x = document.getElementsByTagName('table')[1]
alterRows(1, x.getElementsByTagName('tr')[0])
        

function nextNode(e) {
    while (e && e.nodeType != 1) {
            e = e.nextSibling;
    }
    return e;
    }
function prevNode(e) {
    while (e && e.nodeType != 1) {
        e = e.previousSibling;
    }
    return e;
    }
function swapRows(b) {
    let tab = prevNode(b.previousSibling);
    let tBody = nextNode(tab.firstChild);
    let lastNode = prevNode(tBody.lastChild);
    tBody.removeChild(lastNode);
    let firstNode = nextNode(tBody.firstChild);
    tBody.insertBefore(lastNode, firstNode);
    }

    function cnt(form, msg, maxSize) {
        if (form.value.length > maxSize)
        form.value = form.value.substring(0, maxSize);
        else
        msg.innerHTML = maxSize - form.value.length;
        }
    