import mysql.connector
import csv

# Database connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="saif13",
    database="bookstore"
)

cursor = connection.cursor()

# Path to the CSV file
csv_file_path = "C:\\Users\\91905\\OneDrive\\Desktop\\books.csv"  # Update the file path here

# Open and read the CSV file
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row if present
    
    # Inserting books into the database
    for row in csv_reader:
        try:
            title = row[0]
            author = row[1]
            price = float(row[2])  # Ensure price is a number
            cursor.execute("INSERT INTO books (title, author, price) VALUES (%s, %s, %s)", (title, author, price))
        except ValueError as e:
            print(f"Skipping invalid data in row: {row}")
            continue

# Commit the changes and close the connection
connection.commit()
connection.close()

print("Books added successfully!")
