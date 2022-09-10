// // Invoke Functions Call on Document Loaded
// document.addEventListener('DOMContentLoaded', function () {
//     hljs.highlightAll();
//   });
  
  
  let alertWrapper = document.querySelector('.alert')
  let alertClose = document.querySelector('.alert__close')

  if (alertWrapper) {
    alertClose.addEventListener('click',function(e){
     e.preventDefault()
     console.log("kamin message clicked")
     alertWrapper.style.display = 'none'
    }
	 )
   

  }
  
