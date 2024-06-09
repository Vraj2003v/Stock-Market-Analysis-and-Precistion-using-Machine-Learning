<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Establish database connection
    $conn = new mysqli('localhost', 'root', '', 'loginpage');
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Retrieve username and password from POST data
    $name = $_POST['name'];
    $password = $_POST['password'];

    // Check if user already exists in the database
    $query = "SELECT * FROM signup WHERE name = ? AND password = ?";
    $stmt = $conn->prepare($query);

    // Check if the prepare statement was successful
    if (!$stmt) {
        die("Prepare failed: " . $conn->error);
    }

    // Bind parameters
    $stmt->bind_param('ss', $name, $password);
    
    // Execute query
    if (!$stmt->execute()) {
        die("Execute failed: " . $stmt->error);
    }

    // Store result
    $result = $stmt->get_result();

    // Get number of rows returned
    $count = $result->num_rows;

    // Fetch the email associated with the provided username and password
    if ($count > 0) {
        $row = $result->fetch_assoc();
        $email = $row['email']; // Get the email from the signin table
    }

    // Close the prepared statement
    $stmt->close();

    // Check if there is a matching user
    if ($count > 0) {
        // Prepare and execute insert statement for login table
        $insertQuery = "INSERT INTO login (name, password, email) VALUES (?, ?, ?)";
        $insertStmt = $conn->prepare($insertQuery);

        // Check if the prepare statement was successful
        if (!$insertStmt) {
            die("Prepare failed: " . $conn->error);
        }

        // Bind parameters
        $insertStmt->bind_param('sss', $name, $password, $email);

        // Execute the prepared statement
        if (!$insertStmt->execute()) {
            die("Execute failed: " . $insertStmt->error);
        }

        // Close the prepared statement
        $insertStmt->close();

        // Redirect to index2.html upon successful signup
        header("Location: ../index2.html");
        exit(); // Stop further execution
    } else {
        // Display alert message using JavaScript
        echo '<script type="text/javascript">
                alert("User not registered. Please sign up first.");
                window.location.href = "../signin.html";
              </script>';
        exit(); // Stop further execution
    }

    // Close database connection
    $conn->close();
} else {
    // Handle the case where it's not a POST request
    echo "Invalid request method!";
}
?>
