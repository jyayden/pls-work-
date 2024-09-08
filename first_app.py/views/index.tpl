<!DOCTYPE html>
<html>
    <head>
        <link type="text/css" href="/static/style.css" rel="stylesheet">
        <title>Project Company</title>
    </head>
    <body>
        <h1>Welcome to Project Company!</h1>

        <p><a href="/users">View All Users</a></p>
        <p><a href="/suppliers">View All Suppliers</a></p>
        <p><a href="/products">View All Products</a></p>
        <p><a href="/categories">View All Categories</a></p>
        <p><a href="/orders">View All Orders</a></p>
        <p><a href="/order_items">View All Order Items</a></p>
        <p><a href="/reviews">View All Reviews</a></p>

        <div class="container">
            <h2>Database Management</h2>
        
            <!-- Form to insert a new user -->
            <form action="/insert_user" method="post">
                <label for="username">Username:</label><br>
                <input type="text" id="username" name="username" required><br><br>

                <label for="role">Role:</label><br>
                <input type="text" id="role" name="role" required><br><br>

                <label for="password">Password:</label><br>
                <input type="password" id="password" name="password" required><br><br>

                <label for="created_at">Date Created:</label><br>
                <input type="date" id="created_at" name="created_at" required><br><br>
        
                <input type="submit" value="Insert User Data">
            </form>
        
            <!-- Form to delete a user -->
            <form action="/delete_user" method="post">
                <label for="user_id">User ID to Delete:</label><br>
                <input type="text" id="user_id" name="user_id" required><br><br>
        
                <input type="submit" value="Delete User Data">
            </form>
        </div>
    </body>
</html>
