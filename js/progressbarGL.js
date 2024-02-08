const progress = document.querySelector('.progress')

window.addEventListener('scroll' , progressBar);

function progressBar(e){
    let windowscroll = document.body.scrollTop || document.documentElement.scrollTop;
    let windowheight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    let per = windowscroll / windowheight * 100;
    
    progress.style.width = per + '%';

}