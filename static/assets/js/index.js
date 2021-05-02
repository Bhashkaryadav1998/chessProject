function upload(){
let image=document.getElementById('customFile').files[0];
if(image){
    console.log('hello');
    document.getElementById('up').style.display='none';
    let board=document.getElementById('chessBoard');
    board.src=URL.createObjectURL(image);
    $('#chess').css('display','block');
}
}
document.getElementById('analyze').onclick= async (e) => {
    e.preventDefault();
    e.stopPropagation();
    let image=document.getElementById('customFile').files[0];
    let formData = new FormData();
    formData.append('file',image);
    let response = await fetch('/upload', {
        method: 'POST',
        body: formData,
    });
    $('#exampleModal').modal('hide');
    let result = await response.json();
    console.log(result);
}