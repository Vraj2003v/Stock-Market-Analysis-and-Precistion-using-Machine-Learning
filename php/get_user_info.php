<?php
// Establish database connection
$conn = new mysqli('localhost', 'root', '', 'loginpage');
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Retrieve user information from the login table
$query = "SELECT * FROM login ORDER BY id DESC LIMIT 1"; // Assuming id is the primary key and auto-incremented
$result = $conn->query($query);

if ($result->num_rows > 0) {
    $userInfo = $result->fetch_assoc();
    // Return user information as JSON
    echo json_encode($userInfo);
} else {
    // If no user information found, return an empty JSON object
    echo json_encode(array());
}

// Close database connection
$conn->close();
?>
