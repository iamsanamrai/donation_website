
function loginAction(){
    var inputEmail = document.querySelector("#inputEmail").value;
    var inputpwd = document.querySelector("#inputPassword").value;
    if( inputEmail =="admin@gmail.com" && inputpwd == "password")
    {
      window.location.href="/login/insides";
    } else{
      alert("Please Fill the email address / password !"); 
    }
}

function hambbar_handler() {
    const x = document.querySelector(".navigation");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
  }