import sqlite3

def insert_sample_data(database_name):
    conn = sqlite3.connect(database_name)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    print('Inserting data into database')

    # Inserting data into the users table
    print('Inserting data into users table')
    users = [
        (1, "John Doe", "john@example.com", "password123", "2023-09-01"),
        (2, "Jane Smith", "jane@example.com", "password456", "2023-09-05"),
        (3, "Michael Brown", "michael@example.com", "password789", "2023-09-10"),
        (4, "Emily Davis", "emily@example.com", "pass987", "2023-09-15"),
        (5, "David Wilson", "david@example.com", "abc123", "2023-09-18"),
        (6, "Olivia Johnson", "olivia@example.com", "pwd987", "2023-09-22"),
        (7, "Lucas Lee", "lucas@example.com", "passpass", "2023-09-25"),
        (8, "Sophia Miller", "sophia@example.com", "12345abc", "2023-09-30"),
        (9, "James Garcia", "james@example.com", "pass333", "2023-10-02"),
        (10, "Ava Martinez", "ava@example.com", "secret123", "2023-10-05")
    ]
    cursor.executemany('INSERT INTO users (User_ID, Name, Email, Password, Registration_Date) VALUES (?, ?, ?, ?, ?);', users)

    # Inserting data into suppliers table
    print('Inserting data into suppliers table')
    suppliers = [
        (1, "ABC Supplies", "contact@abc.com", "555-1234", "123 Supply St."),
        (2, "XYZ Distributors", "sales@xyz.com", "555-5678", "456 Market Ave."),
        (3, "Global Goods", "info@globalgoods.com", "555-9876", "789 Commerce Blvd."),
        (4, "Local Vendors", "support@localvendors.com", "555-4321", "321 Business Park"),
        (5, "Premium Parts", "sales@premiumparts.com", "555-2468", "654 Parts Lane"),
        (6, "FastTrack Supplies", "info@fasttrack.com", "555-7531", "987 Fast St."),
        (7, "Reliable Goods", "contact@reliable.com", "555-3698", "369 Trust Ave."),
        (8, "Innovative Solutions", "info@innovative.com", "555-8523", "852 Ideas Way"),
        (9, "Elite Distributors", "sales@elite.com", "555-1597", "159 Elite Road"),
        (10, "Budget Suppliers", "support@budget.com", "555-7539", "753 Saver St.")
    ]
    cursor.executemany('INSERT INTO suppliers (Supplier_ID, Name, Email, Phone, Address) VALUES (?, ?, ?, ?, ?);', suppliers)

    # Inserting data into categories table
    print('Inserting data into categories table')
    categories = [
        (1, "Electronics"),
        (2, "Office Supplies"),
        (3, "Furniture"),
        (4, "Groceries"),
        (5, "Clothing"),
        (6, "Sports Equipment"),
        (7, "Tools"),
        (8, "Health & Beauty"),
        (9, "Toys & Games"),
        (10, "Automotive")
    ]
    cursor.executemany('INSERT INTO categories (Category_ID, Name) VALUES (?, ?);', categories)

    # Inserting data into products table
    print('Inserting data into products table')
    products = [
        (1, "Laptop", 1, 1, 999.99),
        (2, "Printer", 1, 2, 199.99),
        (3, "Desk", 3, 1, 150.00),
        (4, "Chair", 3, 1, 85.50),
        (5, "Notebook", 2, 2, 3.50),
        (6, "Pen Set", 2, 2, 9.99),
        (7, "T-shirt", 5, 3, 19.99),
        (8, "Tennis Racket", 6, 4, 75.99),
        (9, "Hammer", 7, 5, 12.99),
        (10, "Shampoo", 8, 6, 5.50),
    ]
    cursor.executemany('INSERT INTO products (Product_ID, Name, Category_ID, Supplier_ID, Price) VALUES (?, ?, ?, ?, ?);', products)

    # Inserting data into orders table
    print('Inserting data into orders table')
    orders = [
        (1, 1, "2024-01-15", "Shipped"),
        (2, 2, "2024-01-20", "Processing"),
        (3, 3, "2024-02-05", "Delivered"),
        (4, 4, "2024-02-10", "Cancelled"),
    ]
    cursor.executemany('INSERT INTO orders (Order_ID, User_ID, Order_Date, Status) VALUES (?, ?, ?, ?);', orders)

    # Inserting data into order_items table
    print('Inserting data into order_items table')
    order_items = [
        (1, 1, 1, 2),
        (2, 1, 5, 10),
        (3, 2, 3, 1),
        (4, 2, 7, 2),
        (5, 3, 4, 4),
    ]
    cursor.executemany('INSERT INTO order_items (Order_Item_ID, Order_ID, Product_ID, Quantity) VALUES (?, ?, ?, ?);', order_items)

    # Inserting data into reviews table
    print('Inserting data into reviews table')
    reviews = [
        (1, 1, 1, 5, "Great product! Highly recommended."),
        (2, 2, 2, 4, "Works well, but could be cheaper."),
        (3, 3, 3, 3, "Decent, but the quality could be better."),
        (4, 4, 4, 5, "Comfortable chair!"),
    ]
    cursor.executemany('INSERT INTO reviews (Review_ID, Product_ID, User_ID, Rating, Comment) VALUES (?, ?, ?, ?, ?);', reviews)

    conn.commit()
    conn.close()