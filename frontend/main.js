let logoutBtn=document.getElementById('logout-btn')
let loginBtn=document.getElementById('login-btn')

console.log('loginBtn',loginBtn)
console.log('logoutBtn',logoutBtn)
let token=localStorage.getItem('token')
if(token){
    
    loginBtn.remove() 
}else{
    
    logoutBtn.remove()
}
logoutBtn.addEventListener('click',(e)=> {
    e.preventDefault()
    localStorage.removeItem('token')
    window.location='file:///C:/Users/kamin/Desktop/frontend/login.html'
})

let projectsUrl='http://127.0.0.1:8000/api/projects/'

let getProjects= () => {
    fetch(projectsUrl)
    .then(response => response.json())
    .then(data =>{
        console.log(data)
        buildProjects(data)
    })
}
let buildProjects= (projects)=>{
    let projectswrapper=document.getElementById('projects--wrapper')
    projectswrapper.innerHTML=''
    //console.log("projects-wrapper:",projectswrapper)
    for (let i=0; projects.length > i; i++){
        let project=projects[i]
        //console.log(project)
        let projectCard=`
        <div class="project--card">
            <img src="http://127.0.0.1:8000${project.featured_image}" />
            <div>
                <div class="card--header"> 
                    <h3>${project.title}</h3>
                    <strong  class="vote--option" data-vote="up" data-project="${project.id}">&#43; </strong>
                    <strong  class="vote--option" data-vote="down" data-project="${project.id}">&#8722; </strong>
                </div>
                <i>${project.vote_ratio}% Positive feedback</i>
                <p>${project.description.substring(0,150)}</p>
            </div>
        </div>
        `
        projectswrapper.innerHTML+=projectCard
        //add in listner
       

    }
    addVoteEvents()   
}

let addVoteEvents=()=>{
    let voteBtns=document.getElementsByClassName("vote--option")
    for(let i=0; voteBtns.length>i;i++){
        voteBtns[i].addEventListener('click', (e) => {
            let vote=e.target.dataset.vote
            let project=e.target.dataset.project
            //let token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3MjQ2MDEzLCJpYXQiOjE2NjcyNDU3MTMsImp0aSI6ImZjYzMxYmE5MWNmMTQxOWE5YzFlZjEyNzY5NTQxY2Q2IiwidXNlcl9pZCI6OH0.yKRLuPoqLRXuSATbpHQi2NVZ0e6vBmIJxh1Mv8N1_Kg'
            let token=localStorage.getItem('token')
            console.log("TOKEN:",token)
           // console.log("project:",project,"vote:",vote)
           fetch(`http://127.0.0.1:8000/api/projects/${project}/vote/`,{
            method:'POST',
            headers:{
            'Content-Type':'application/json',
            Authorization:`Bearer ${token}`        
            },
            body:JSON.stringify({'value':'vote'})

           })
           .then(response =>response.json())
           .then(data=>{
            console.log('success',data)
            getProjects()
           })
        })
    }
}

getProjects()