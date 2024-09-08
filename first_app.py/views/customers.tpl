
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Management</title>
</head>
<body>
    <h1>User Management</h1>

    <h2>User List</h2>
    <ul>
        % for user in users:
            <li>
                {{user['username']}} - {{user['role']}}
                
                <!-- Form to update user information -->
                <form action="/update_user/{{user['user_id']}}" method="post" style="display:inline;">
                    <input type="text" name="username" value="{{user['username']}}" required>
                    <input type="text" name="role" value="{{user['role']}}" required>
                    <button type="submit">Update</button>
                </form>

                <!-- Link to delete user -->
                <a href="/delete_user/{{user['user_id']}}" onclick="return confirm('Are you sure you want to delete this user?');">Delete</a>
            </li>
        % end
    </ul>
</body>
</html>
