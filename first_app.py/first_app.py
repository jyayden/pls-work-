import sqlite3
import scripts.create_database as create_db  
import scripts.insert_data as db_insert
from bottle import route, run, template, static_file, request, redirect

# Connect to the database
CONN = sqlite3.connect('project_company.db')
CONN.row_factory = sqlite3.Row
CURSOR = CONN.cursor()

# Create database route
@route('/create_database')
def create_database():
    create_db.create_empty_database('project_company.db')
    return template('database_create')

# Insert sample data route
@route('/insert_data')
def insert_data():
    db_insert.insert_sample_data('project_company.db')
    return template('database_insert')

# Static file route
@route('/static/<filename>')
def static(filename):
    return static_file(filename, root='./static')

# Index route
@route('/')
def index():
    return template('index')

# Route to display all users
@route('/users')
def users():
    query = 'SELECT username, role FROM users'
    CURSOR.execute(query)
    user_list = CURSOR.fetchall()
    return template('user_details', users=user_list)

# Route to display all products
@route('/products')
def products():
    query = 'SELECT * FROM products'
    CURSOR.execute(query)
    product_list = CURSOR.fetchall()
    return template('results', records=product_list, title='All Products')

# Route to display all categories
@route('/categories')
def categories():
    query = 'SELECT * FROM categories'
    CURSOR.execute(query)
    category_list = CURSOR.fetchall()
    return template('results', records=category_list, title='All Categories')

# Route to count total users
@route('/count_users')
def count_users():
    query = 'SELECT COUNT(*) as total_users FROM users'
    CURSOR.execute(query)
    result = CURSOR.fetchone()
    return template('results', records=[result], title='Total Users')

# Route to sum up product prices
@route('/sum_product_prices')
def sum_product_prices():
    query = 'SELECT SUM(price) as total_product_price FROM products'
    CURSOR.execute(query)
    result = CURSOR.fetchone()
    return template('results', records=[result], title='Total Product Prices')

# Route to find minimum and maximum stock levels
@route('/min_max_stock')
def min_max_stock():
    query = '''
    SELECT MIN(stock) as min_stock, MAX(stock) as max_stock
    FROM products
    '''
    CURSOR.execute(query)
    result = CURSOR.fetchone()
    return template('results', records=[result], title='Min and Max Stock Levels')

# Route to update a user
@route('/update_user/<user_id:int>', method='POST')
def update_user(user_id):
    username = request.forms.get('username')
    role = request.forms.get('role')
    
    update_query = f'''
    UPDATE users
    SET username = '{username}', role = '{role}'
    WHERE user_id = {user_id};
    '''
    
    CURSOR.execute(update_query)
    CONN.commit()
    return redirect('/users')

# Route to delete a user
@route('/delete_user/<user_id:int>')
def delete_user(user_id):
    delete_query = f'''
    DELETE FROM users
    WHERE user_id = {user_id};
    '''
    
    CURSOR.execute(delete_query)
    CONN.commit()
    return redirect('/users')

# Run the Bottle app
run(host='localhost', port=8080, debug=True, reloader=True)

# Close the cursor and connection on exit
CURSOR.close()
CONN.close()
