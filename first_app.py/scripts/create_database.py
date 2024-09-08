import sqlite3

def create_empty_database(database_name):
    conn = sqlite3.connect(database_name)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    print('creating empty database')
    # Update database settings
    print('Update PRAGMA to support foreign keys')
    cursor.execute('PRAGMA foreign_keys = ON')

    # Drop tables in the correct order 
    print('Drop tables if they exist')
    cursor.execute('DROP TABLE IF EXISTS order_items;')
    cursor.execute('DROP TABLE IF EXISTS orders;')
    cursor.execute('DROP TABLE IF EXISTS reviews;')
    cursor.execute('DROP TABLE IF EXISTS products;')
    cursor.execute('DROP TABLE IF EXISTS categories;')
    cursor.execute('DROP TABLE IF EXISTS suppliers;')
    cursor.execute('DROP TABLE IF EXISTS users;')

    # Create tables
    print('create users table')
    cursor.execute('''
        CREATE TABLE users (
            user_id INTEGER PRIMARY KEY,
            username TEXT(50) NOT NULL,
            password TEXT(255) NOT NULL,
            role TEXT(50) NOT NULL,
            user_created_at DATE(15) NOT NULL
        );
    ''')

    print('create suppliers table')
    cursor.execute('''
        CREATE TABLE suppliers (
            supplier_id INTEGER PRIMARY KEY,
            name TEXT(100) NOT NULL,
            contact_name TEXT(100) NOT NULL,
            contact_email TEXT(100) NOT NULL,
            contact_phone TEXT(15),
            supplier_created_at DATE(15) NOT NULL
        );
    ''')

    print('create categories table')
    cursor.execute('''
        CREATE TABLE categories (
            category_id INTEGER PRIMARY KEY,
            name TEXT(100) NOT NULL,
            description TEXT(255),
            category_created_at DATE(15) NOT NULL
        );
    ''')

    print('create products table')
    cursor.execute('''
        CREATE TABLE products (
            product_id INTEGER PRIMARY KEY,
            name TEXT(100) NOT NULL,
            description TEXT(255),
            price DECIMAL(10, 2) NOT NULL,
            category_id INTEGER,
            supplier_id INTEGER,
            product_created_at DATE(15) NOT NULL,
            FOREIGN KEY (category_id) REFERENCES categories(category_id),
            FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
        );
    ''')

    print('create orders table')
    cursor.execute('''
        CREATE TABLE orders (
            order_id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            order_date DATE(15) NOT NULL,
            status TEXT(50),
            total DECIMAL(10, 2),
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        );
    ''')

    print('create order_items table')
    cursor.execute('''
        CREATE TABLE order_items (
            order_item_id INTEGER PRIMARY KEY,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        );
    ''')

    print('create reviews table')
    cursor.execute('''
        CREATE TABLE reviews (
            review_id INTEGER PRIMARY KEY,
            product_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            rating INTEGER NOT NULL,
            comment TEXT,
            created_at DATE(15) NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products(product_id),
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        );
    ''')

    conn.commit()
    cursor.close()
    conn.close()
    print('empty database created')

create_empty_database("project_company.db")
