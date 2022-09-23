function sendcommenttext(articleId) {
    var comment=$('#comment_text').val()
    var parentId=$('#parent_id').val()
    $.get('/articles/add-article-comment',{
        article_comment:comment,
        article_id:articleId,
        parent_id:parentId
    }).then(res=>{
        console.log(res)
        // location.reload()
        $('#comments_area').html(res)
        $('#comment_text').val('')
        $('#parent_id').val('')
        if(parentId !== null && parentId !== ''){
            document.getElementById('single_comment_box_'+parentId).scrollIntoView({behavior:"smooth"})
        }
        else{
            document.getElementById('comments_area').scrollIntoView({behavior:"smooth"})
        }
    })
}
function fillparentid(parentId) {
    $("#parent_id").val(parentId)
    document.getElementById('comment_form').scrollIntoView({behavior:"smooth"})
}
function filterProduct(){
    const filterPrice= $('#sl2').val()
    const start_price=filterPrice.split(',')[0]
    const end_price=filterPrice.split(',')[1]
    $('#start_price').val(start_price)
    $('#end_price').val(end_price)
    $('#filter-form').submit()
}
function fillPage(page) {
    $('#page').val(page)
    $('#filter-form').submit()

}
function showLargeImage(image) {
    $('#main_image').attr('src',image);
}

function addProductToBasket(productId) {
    const count=$('#product_count').val()
    $.get('/order/add_to_basket?product_id='+productId+'&count='+count).then(res=>{
        Swal.fire({
            title: 'اعلان',
            text:res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: '#3085d6',
            confirmButtonText: res.confirmButtonText
          }).then((result)=>{
            if(result.isConfirmed && res.status==='not_authenticated'){
                window.location.href='/login'
            }
          })
    })
}
function remove_order_detail(detailId) {
    $.get('/user/remove_order_detail?detail_id='+detailId).then(res=>{
        if(res.status==='success'){
            $('#order_detail_content').html(res.body )
        }
    })
}
function changeOrderDetailCount(detailId,state){
    // $.get('/user/change_order_detail?detail_id='+detailId+'&state='+state).then(res=>{
    //     if(res.status==='success'){
    //         $('#order_detail_content').html(res.body )
    //     }
    // })
}
