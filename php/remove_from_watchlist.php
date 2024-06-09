<?php
session_start(); // Start the session to access session variables

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Check if selected checkboxes exist and if any checkboxes are selected
    if (isset($_POST['selected']) && !empty($_POST['selected'])) {
        // Connect to your database
        $servername = "localhost";
        $username = "root";
        $password = "";
        $dbname = "loginpage";

        $conn = new mysqli($servername, $username, $password, $dbname);

        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        // Prepare a SQL statement to delete selected items from the watchlist
        $stmt = $conn->prepare("DELETE FROM watchlist WHERE stock_name = ? AND name = ?");

        // Bind parameters
        $stmt->bind_param("ss", $stock_name, $name);

        // Get the name from the last entry in the login table
        $sql = "SELECT name FROM login ORDER BY id DESC LIMIT 1";
        $result = $conn->query($sql);

        if ($result && $result->num_rows > 0) {
            // Fetch the row
            $row = $result->fetch_assoc();
            // Assign the name from the last entry to the $name variable
            $name = $row['name'];
        } else {
            // Handle if no rows are returned
            $name = ""; // or any default value
        }

        // Get the user_id from the session
        $user_id = $_SESSION['name'];

        // Loop through selected checkboxes
        foreach ($_POST['selected'] as $selected) {
            $stock_name = $selected;

            // Execute the statement
            $stmt->execute();
        }

        // Close statement
        $stmt->close();

        // Close connection
        $conn->close();

        // Redirect back to the page where the form was submitted
        header("Location: ../watchlist.php");
        exit();
    } else {
        // If no checkboxes are selected, you can redirect back to the page or perform any other action
        header("Location: ../watchlist.php");
        exit();
    }
}
?>
