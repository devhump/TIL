//let tabLen = $('.tab-button').length;
//
//// tab 버튼 기능 구현 (반복문)
//for (let i = 0; i < tabLen ; i++){
//  
//  tabBtn.eq(i).on('click', function(){
//    tabOpen(i);
//  })
//}


$('.list').click(function(e){
  
  console.log(e.target.dataset.id);
  tabOpen(e.target.dataset.id);
})


let tabBtn = $('.tab-button');
let tabContent = $('.tab-content');

function tabOpen(idx){
    tabBtn.removeClass('orange');
    tabBtn.eq(idx).addClass('orange');

    tabContent.removeClass('show');
    tabContent.eq(idx).addClass('show');
}