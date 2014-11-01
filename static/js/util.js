'use strict';


function majax(url,data,successf) {
    // console.log(data)
    $.ajax({
        url: url,
        type: 'POST',
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify(data),
        success: function(ret) {
            console.log(ret);
            // location.href = '/user/'
        },
        error: function(err) { console.log(err); }
    });
}


function login(name, pwd) {
    majax('/login/', { name:name, pwd:pwd }, function(ret) {
        // if (ret.state === 0) {
            // location.href = '/mood/';
        // } else {
            // console.log(ret);
        // }
        console.log(ret)
    })
}

function register(name, pwd) {
    majax('/reg/', {'name':name, 'pwd':pwd}, function(ret) {
        console.log(ret);
        // if (ret.state === 0) {
        //     location.href = '/mood/';
        // } else {
        //     console.log(ret);
        // }
    })
}

function getDataURL(imageFile) {
    return URL.createObjectURL(imageFile);
}