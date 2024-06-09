<?php
// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
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

    // Process selected images
    if(isset($_POST['images'])) {
        // Retrieve the last entry from the login table to get the username of the logged-in user
        $last_login_query = "SELECT name FROM login ORDER BY id DESC LIMIT 1";
        $last_login_result = $conn->query($last_login_query);
        $row = $last_login_result->fetch_assoc();
        $username = $row['name'];

        foreach($_POST['images'] as $stock_name) {
            // Check if the stock_name already exists in the watchlist table for the user
            $check_query = "SELECT * FROM watchlist WHERE stock_name = '$stock_name' AND name = '$username'";
            $check_result = $conn->query($check_query);

            if ($check_result->num_rows == 0) {
                // Insert stock name and username into the database
                $sql = "INSERT INTO watchlist (stock_name, name) VALUES ('$stock_name', '$username')";
                if ($conn->query($sql) === TRUE) {
                    // Insertion successful
                } else {
                    echo "Error: " . $sql . "<br>" . $conn->error;
                }
            } else {
                echo "Stock '$stock_name' is already in the watchlist for user '$username'.<br>";
            }
        }
    }
    
    // Close database connection
    $conn->close();
    
    // Refresh the current page
    header("Location: ../watchlist.php");
    exit();
}
?>
