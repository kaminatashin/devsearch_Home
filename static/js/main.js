  //get search form and page link
  let searchForm=document.getElementById('searchForm')
  let pageLink=document.getElementsByClassName('page-link')

  //ensure search FORM exists
  if(searchForm){
    for(let i= 0; pageLink.length >i;i++){
      pageLink[i].addEventListener('click',function(e){
        e.preventDefault()
        //Get Data Attribute
        let page=this.dataset.page
        console.log('PAGE:',page)
        //add hidden search input to form
        searchForm.innerHTML+=`<input value=${page} name="page" hidden/>`

        //submit form
        searchForm.submit()
      })

    }

  }
