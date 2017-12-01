/**
 * Created by imurphy on 7/24/17.
 */

window.addEventListener("load", function () {
    Message.install();
    Toast.init();

    try{
        eval("let a=`${1+2}`;if(a!=='3')throw 0");
    }catch (e){
        Toast.pop('Browser Incompatible', 'This browser doesn\'t support features required by this application.  Try using the latest version of Chrome or Firefox', 'negative', -1);
    }
});

const Message = {

    create:function(header, content, status, loading){
        if(loading) loading = '<i class="notched circle loading icon"></i>';
        else loading = '';
        return `<div class="ui ${status} message">${loading}<i class="close icon"></i><div class="content"><div class="header">${header}</div>${content}</div></div>`;
    },

    show:function (id, header, content, status) {
        if(status === "loading"){
            status = "icon";
        }
        let messageContainer = document.getElementById(id);
        messageContainer.innerHTML = Message.create(header, content, status);
        Message.install();
    },

    prepend:function (id, header, content, status) {
        let messageContainer = document.getElementById(id);
        messageContainer.innerHTML = Message.create(header, content, status) + messageContainer.innerHTML;
        Message.install();
    },

    install:function () {
        $('.message .close').on('click', function () {
            $(this).closest('.message').transition('fade');
        });
    },

    map:function (id) {
        return function (data) {
            Message.show(id, data.header, data.content, data.status);
        };
    }
};

let Toast = {
    baseNode:null,
    current:null,
    init:function () {
        var templateNode = document.getElementById('toast-template');
        Toast.baseNode = templateNode.cloneNode(true);
        templateNode.parentNode.removeChild(templateNode);

    },
    pop:function (header, content, className, duration) {
        var toast = Toast.baseNode.cloneNode(true);
        toast.querySelector('.content').innerHTML += content;
        toast.querySelector('.header').innerHTML += header;
        if(className && className.length > 0)
            toast.classList.add(className);
        toast.classList.add('toast-message');

        document.body.appendChild(toast);
        toast.classList.add('fly-on');
        if(duration > 0){
            setTimeout(function () {
                Toast.remove();
            }, duration);
        }
        Toast.remove();
        Toast.current = toast;
        Message.install();
    },
    remove:function(){
        if(Toast.current) {
            document.body.removeChild(Toast.current);
            Toast.current = null;
        }
    }
};


function Form2Object(form){
    let data = $(form).serializeArray();
    let obj = {};
    
    $.each(data, function (i, param) {
        obj[param.name] = param.value;
    });
    return obj;
}

function escapeHtml(unsafe) {
    return unsafe
         .replace(/&/g, "&amp;")
         .replace(/</g, "&lt;")
         .replace(/>/g, "&gt;")
         .replace(/"/g, "&quot;")
         .replace(/'/g, "&#039;");
 }



