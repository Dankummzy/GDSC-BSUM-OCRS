<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title></title>
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">

</head>
<body>
    <div class="container">
        <div class="register_form">
            <form action="../includes/signup.inc.php" method="POST">
                <h1>Register</h1>
                <hr>
                <div class="form-group">
                    <label>First Name</label>
                    <input type="text" name="f_name" class="form-control" placeholder="Enter your First Name" required/>
                </div>
                <div class="form-group">
                    <label>Last Name</label>
                    <input type="text" name="l_name" class="form-control" placeholder="Enter your Last Name" required/>
                </div>
                <div class="form-group">
                    <label>Email</label>
                    <input type="email" name="email" class="form-control" placeholder="Someone@mail.com" required/>
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <input type="password" name="password" class="form-control" placeholder="Choose a Password" required/>
                </div>
                <div class="form-group">
                    <label>Confirm Password</label>
                    <input type="password" name="c_password" class="form-control" placeholder="Confirm your password" required/>
                </div>
                <div class="cta">
                    <button type="submit" name="reg_user" class="btn btn-primary">Create Account</button>
                    <p>Already have an Account? <a href="#">Login Instead</a> </p>
                </div>
            </form>
        </div>
    </div>



    <!-- JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>