import sqlite3

# Step 1: Connect to a database (creates it if it doesn't exist)
conn = sqlite3.connect('mycrudfile.db')
cursor = conn.cursor()

# Step 2: Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE NOT NULL
)
''')
conn.commit()  # Save the changes

# Step 3: Insert (Create)
def create_user(name, age, email):
    cursor.execute('''
    INSERT INTO users (name, age, email) VALUES (?, ?, ?)
    ''', (name, age, email))
    conn.commit()

# Step 4: Retrieve (Read)
def get_users():
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()

# Step 5: Update
def update_user(user_id, name=None, age=None, email=None):
    # Use a dynamic query to update fields conditionally
    fields = []
    values = []
    if name:
        fields.append("name = ?")
        values.append(name)
    if age:
        fields.append("age = ?")
        values.append(age)
    if email:
        fields.append("email = ?")
        values.append(email)
    values.append(user_id)

    query = f"UPDATE users SET {', '.join(fields)} WHERE id = ?"
    cursor.execute(query, values)
    conn.commit()

# Step 6: Delete
def delete_user(user_id):
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()

# Example Usage
create_user('Jonathan', 30, 'jonathan@example.com')
create_user('Dave Smith', 25, 'dave@example.com')

# Retrieve all users
users = get_users()
print("Users:", users)

# Update user with ID 1
update_user(1, name='Mr, Roy Ellis', age=81)

# Delete user with ID 2
delete_user(2)

# Retrieve users again
users = get_users()
print("Updated Users:", users)

# Step 7: Close the connection
conn.close()