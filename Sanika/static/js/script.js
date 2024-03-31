const body = document.querySelector("body")
 sidebar = body.querySelector(".sidebar"),
 toggle = body.querySelector(".toggle"),
 searchBtn = body.querySelector(".searchBtn"),
 modeSwitch= body.querySelector(".toggle-switch"),
 modeText = body.querySelector(".mode-text"),


 toggle.addEventListener("click", () =>{
    sidebar.classList.toggle("close");
 });
 toggle.addEventListener("click", () =>{
    sidebar.classList.remove("close");
 });


 modeSwitch.addEventListener("click", () =>{
    body.classList.toggle("dark");

    if(body.classList.contains("dark")){
        modeText.innerText = "Light Mode"
    }else{
        modeText.innerText = "Dark Mode"
    }

   

    

 });

