const p1=document.getElementById('pas1');
const p2=document.getElementById('pas2');
const password=document.getElementById('password');
function ShowPassword(){
    if (password.type==='password'){
        password.type='text';

    }else{
        password.type='password';
    }
}

function ShowPasswordinSignUp(){
    if (p1.type==='password' && p2.type=='password' ){
        p1.type='text';
        p2.type='text';
    }
    else{

        p2.type='password';
        p2.type='password';
    }
}