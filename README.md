# Database Class

This is a simple `Database` class for managing SQLite databases using Python. It provides methods for creating tables, adding data, retrieving data, updating records, deleting entries, exporting to Excel, and checking for the existence of records.

## Features

- Create tables with specified columns
- Insert new records into tables
- Retrieve records with optional filtering
- Update existing records
- Delete records based on conditions
- Export table data to Excel files
- Check for the existence of records

## Installation

Make sure you have the following packages installed:

```bash
pip install pandas
```

## Usage

### 1. Initialize the Database

To start using the `Database` class, you need to create an instance of it by specifying the database name:

```python
from your_module import Database

db = Database('example.db')
```

### 2. Create a Table

You can create a new table by specifying its name and the columns it should contain:

```python
db.create_table('users', '(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')
```

### 3. Add Records

You can insert new records into the table using the `add` method:

```python
db.add('users', (1, 'Alice', 30))
db.add('users', (2, 'Bob', 25))
```

### 4. Retrieve Records

To fetch all records or specific records based on a condition, use the `get` method:

```python
# Get all records
all_users = db.get('users')
print(all_users)

# Get users older than 25
older_users = db.get('users', 'age > 25')
print(older_users)
```

### 5. Update Records

You can update existing records using the `update` method:

```python
db.update('users', 'age = 31', 'name = "Alice"')
```

### 6. Delete Records

To delete records that match a certain condition, use the `delete` method:

```python
db.delete('users', 'name = "Bob"')
```

### 7. Export to Excel

You can export the contents of a table to an Excel file:

```python
db.export_to_excel('users')
```

### 8. Check for Existence

To check if a record exists based on a condition, you can use the `exists` method:

```python
user_exists = db.exists('users', 'name = "Alice"')
print(user_exists)  # True if Alice exists
```

### 9. Close the Database Connection

Finally, don't forget to close the database connection when you're done:

```python
db.close()
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you want to contribute, please fork the repository and submit a pull request. Any contributions are welcome!
