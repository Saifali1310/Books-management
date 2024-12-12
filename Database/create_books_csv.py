import csv

# Data to be saved in CSV
books_data = [
    ["Title", "Author", "Price"],
    ["Don Quixote", "Miguel de Cervantes", 20.99],
    ["Alice's Adventures in Wonderland", "Lewis Carroll", 15.99],
    ["The Adventures of Huckleberry Finn", "Mark Twain", 10.99],
    ["The Adventures of Tom Sawyer", "Mark Twain", 12.99],
    ["Treasure Island", "Robert Louis Stevenson", 14.99],
    ["Pride and Prejudice", "Jane Austen", 18.99],
    ["Wuthering Heights", "Emily Brontë", 16.99],
    ["Jane Eyre", "Charlotte Brontë", 17.50],
    ["Moby Dick", "Herman Melville", 22.99],
    ["The Scarlet Letter", "Nathaniel Hawthorne", 12.00],
    ["Gulliver's Travels", "Jonathan Swift", 13.99],
    ["The Pilgrim's Progress", "John Bunyan", 9.50],
    ["A Christmas Carol", "Charles Dickens", 14.50],
    ["David Copperfield", "Charles Dickens", 20.00],
    ["A Tale of Two Cities", "Charles Dickens", 15.50],
    ["Little Women", "Louisa May Alcott", 15.00],
    ["Great Expectations", "Charles Dickens", 15.99],
    ["The Hobbit", "J.R.R. Tolkien", 19.99],
    ["Frankenstein", "Mary Shelley", 12.99],
    ["Oliver Twist", "Charles Dickens", 11.99],
    ["Uncle Tom's Cabin", "Harriet Beecher Stowe", 10.50],
    ["Crime and Punishment", "Fyodor Dostoevsky", 19.99],
    ["Madame Bovary: Patterns of Provincial Life", "Gustave Flaubert", 14.99],
    ["The Return of the King", "J.R.R. Tolkien", 24.99],
    ["Dracula", "Bram Stoker", 14.00],
    ["The Three Musketeers", "Alexandre Dumas", 15.00],
    ["Brave New World", "Aldous Huxley", 16.99],
    ["War and Peace", "Leo Tolstoy", 22.99],
    ["To Kill a Mockingbird", "Harper Lee", 14.99],
    ["The Wizard of Oz", "L. Frank Baum", 10.50],
    ["Les Misérables", "Victor Hugo", 19.50],
    ["The Secret Garden", "Frances Hodgson Burnett", 9.99],
    ["Animal Farm", "George Orwell", 10.00],
    ["The Great Gatsby", "F. Scott Fitzgerald", 16.99],
    ["The Little Prince", "Antoine de Saint-Exupéry", 12.99],
    ["The Call of the Wild", "Jack London", 14.99],
    ["Twenty Thousand Leagues Under the Sea", "Jules Verne", 15.99],
    ["Anna Karenina", "Leo Tolstoy", 18.99]
]

# Writing to CSV
csv_file_path = "C:\\Users\\91905\\OneDrive\\Desktop\\books.csv"  # Ensure the correct path
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(books_data)

print("CSV file has been written successfully.")
