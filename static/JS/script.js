document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var log  = "{% url 'go-log' %}";
    var log_go  = "{% url 'login' %}";
  

    var username1 = document.getElementById('username').value;
    var email1= document.getElementById('email').value;
    var type1 = document.getElementById('type').value;
    var password1 = document.getElementById('password').value;
    var retypePassword1 = document.getElementById('retype_password').value;
  
    // Simple validation for demonstration
    if (password1 !== retypePassword1) {
      alert("Passwords do not match!");
      return;
    }
  
    // Simulate registration submission (replace this with actual form submission)
    console.log("Registration Form Submitted:");
    console.log("Username:", username1);
    console.log("Email:", email1);
    console.log("Type:", type1);
    console.log("Password:", password1);

    myData={username:username1,email:email1,type:type1,password:password1};

      


    
  
    // Redirect to login page
    $.ajax({
      url: log, // URL of the Django endpoint
      type: 'POST',
      data: {
          'my_data': myData // Data to be sent to the server
      },
      success: function(response) {
          window.location.href = log_go; // Redirect to the next page
      },
      error: function(xhr, status, error) {
          console.error(error); // Handle error
      }
  });

    
  });

  
  document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var loginUrl = this.dataset.loginUrl;
  
    var email = document.getElementById('login_email').value;
    var password = document.getElementById('login_password').value;
  
    // Simple validation for demonstration
    if (!email || !password) {
      alert("Please fill in all fields!");
      return;
    }
  
    // Simulate login submission (replace this with actual form submission)
    console.log("Login Form Submitted:");
    console.log("Email:", email);
    console.log("Password:", password);
  
    // Redirect to dashboard or home page
    window.location.href=loginUrl;
  });
  