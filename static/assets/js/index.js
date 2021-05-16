let x=brd_hisPly;
function upload(){
let image=document.getElementById('customFile').files[0];
if(image){
    console.log('hello');
    document.getElementById('up').style.display='none';
    let board=document.getElementById('chessBoard');
    board.src=URL.createObjectURL(image);
    $('#chess').css('display','block');
    $('#chess').addClass('d-md-flex');
}
}
document.getElementById('analyze').onclick= async (e) => {
    e.preventDefault();
    e.stopPropagation();
    let image=document.getElementById('customFile').files[0];
    let formData = new FormData();
    formData.append('file',image);
    formData.append('flip',flip);
    let response = await fetch('/upload', {
        method: 'POST',
        body: formData,
    });
    $('#exampleModal').modal('hide');
    let result=await response.json();
    console.log(result);
    let castle="",K=$('#K'),Q=$('#Q'),k=$('#k'),q=$('#q');
    if(K.is(':checked')) castle+=K.val();
    if(Q.is(':checked')) castle+=Q.val();
    if(k.is(':checked')) castle+=k.val();
    if(q.is(':checked')) castle+=q.val();

    console.log(castle);
    result+=" ";
    if(side==0)result+='w';
    else result+='b';
    result+=" ";
    if(castle!="") result+=castle;
    else result+='-';
    result+=" ";
    result+='-';
    result+=" ";
    result+="0";
    result+=" ";
    result+='1';
    console.log(result);
    setFromFen(result,side);
    $('#up').css('display','block');
     $('#chess').css('display','none');
    $('#chess').removeClass('d-md-flex');

}
