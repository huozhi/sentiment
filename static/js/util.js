'use strict';


function ajax(url,data,success) {
    $.ajax({
        url: url,
        type: 'POST',
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify(data),
        success: success,
        error: function(err) { alert (err); }
    });
}


function login(name, pwd) {
    ajax('/login/', {'name':name,'pwd':pwd}, function(data) {
        console.log(data);
        if (data.state === 0) {
            location.href = '/user/';
        }
    })
}

function register(name, pwd) {
    ajax('/reg/', {'name':name, 'pwd':pwd}, function(data) {
        console.log(data);
        if (data.state === 0) {
            location.href = '/user/';
        }
    })
}

function getDataURL(imageFile) {
    return URL.createObjectURL(imageFile);
}