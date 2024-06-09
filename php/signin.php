<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Database Connection
    $conn = new mysqli('localhost', 'root', '', 'loginpage');
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    } else {
        $stmt = $conn->prepare("INSERT INTO signup (name, email, password) VALUES (?, ?, ?)");
        
        // Check if preparation succeeded
        if ($stmt === false) {
            echo "Error: " . $conn->error;
        } else {
            $stmt->bind_param('sss', $name, $email, $password); // Bind the parameters with 's' standing for string
            $stmt->execute(); // Execute the prepared statement
            
            $stmt->close();
            
            // Redirect to signin.html upon successful signup
            header("Location: ../signin.html");
            exit(); // Ensure no further execution after redirection
        }
        $conn->close();
    }
} else {
    // Handle the case where it's not a POST request
    echo "Invalid request method!";
}
?>
