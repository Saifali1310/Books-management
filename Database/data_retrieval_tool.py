import mysql.connector
from tabulate import tabulate

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="saif13",
            database="bookstore"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def fetch_books(cursor, query, params=None):
    cursor.execute(query, params if params else ())
    return cursor.fetchall()

def display_results(rows):
    print(tabulate(rows, headers=["ID", "Title", "Author", "Price"], tablefmt="grid"))

def export_to_file(rows):
    with open("books_results.txt", "w") as file:
        file.write(tabulate(rows, headers=["ID", "Title", "Author", "Price"], tablefmt="grid"))
    print("Results exported to books_results.txt")

def paginate_query(query, page_size, page_number, cursor):
    offset = (page_number - 1) * page_size
    paginated_query = f"{query} LIMIT {page_size} OFFSET {offset}"
    cursor.execute(paginated_query)
    return cursor.fetchall()

def main():
    connection = connect_to_database()
    if not connection:
        return
    cursor = connection.cursor()

    # Pagination settings
    page_size = 5  # Number of books per page
    current_page = 1  # Start at the first page

    print("Options:")
    print("1. View all books")
    print("2. Search books by title")
    print("3. Search books by author")
    print("4. Search books by price range")
    print("5. Sort books by title")
    print("6. Sort books by price")
    print("7. Update book details")
    print("8. Delete a book")
    print("9. View books with pagination")
    print("10. Search books by genre")  # Add this option

    choice = input("Enter your choice (1-10): ")

    try:
        if choice == "1":
            query = "SELECT id, title, author, price FROM Books"
            rows = fetch_books(cursor, query)
            display_results(rows)

        elif choice == "2":
            title = input("Enter the book title to search: ")
            query = "SELECT id, title, author, price FROM Books WHERE title LIKE %s"
            rows = fetch_books(cursor, query, (f"%{title}%",))
            display_results(rows)

        elif choice == "3":
            author = input("Enter the author's name to search: ")
            query = "SELECT id, title, author, price FROM Books WHERE author LIKE %s"
            rows = fetch_books(cursor, query, (f"%{author}%",))
            display_results(rows)

        elif choice == "4":
            min_price = float(input("Enter the minimum price: "))
            max_price = float(input("Enter the maximum price: "))
            query = "SELECT id, title, author, price FROM Books WHERE price BETWEEN %s AND %s"
            rows = fetch_books(cursor, query, (min_price, max_price))
            display_results(rows)

        elif choice == "5":
            query = "SELECT id, title, author, price FROM Books ORDER BY title"
            cursor.execute(query)
            rows = cursor.fetchall()
            display_results(rows)

        elif choice == "6":
            query = "SELECT id, title, author, price FROM Books ORDER BY price"
            cursor.execute(query)
            rows = cursor.fetchall()
            display_results(rows)

        elif choice == "7":
            book_id = int(input("Enter the ID of the book you want to update: "))
            new_title = input("Enter the new title: ")
            new_author = input("Enter the new author: ")
            new_price = float(input("Enter the new price: "))
    
            query = """
            UPDATE Books 
            SET title = %s, author = %s, price = %s
            WHERE id = %s
            """
            cursor.execute(query, (new_title, new_author, new_price, book_id))
            connection.commit()  # Save the changes
            print("Book details updated successfully!")

        elif choice == "8":
            book_id = int(input("Enter the ID of the book you want to delete: "))
            query = "DELETE FROM Books WHERE id = %s"
            cursor.execute(query, (book_id,))
            connection.commit()  # Save the changes
            print(f"Book with ID {book_id} deleted successfully!")

        elif choice == "9":
            query = "SELECT id, title, author, price FROM Books"
            rows = paginate_query(query, page_size, current_page, cursor)
            display_results(rows)
            user_input = input("Navigate - Next (n) / Previous (p) / Exit (e): ").lower()
            while user_input not in ['e']:
                if user_input == 'n':  # Next page
                    current_page += 1
                elif user_input == 'p':  # Previous page
                    if current_page > 1:
                        current_page -= 1
                    else:
                        print("You are already on the first page.")
                rows = paginate_query(query, page_size, current_page, cursor)
                display_results(rows)
                user_input = input("Navigate - Next (n) / Previous (p) / Exit (e): ").lower()

        elif choice == "10":  # New option for Search by Genre
            genre = input("Enter the genre of the book to search: ")
            query = "SELECT id, title, author, price FROM Books WHERE genre LIKE %s"
            rows = fetch_books(cursor, query, (f"%{genre}%",))  # Using LIKE for partial match
            display_results(rows)

        else:
            print("Invalid choice. Please try again.")

    except ValueError as ve:
        print(f"Input error: {ve}")
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()
