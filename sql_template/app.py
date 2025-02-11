from flask import Flask
from flask import render_template
from flask import request
import sqlite3

# connect to our SQLite database
def get_db_connection():
    conn = sqlite3.connect('students.db')  # This will create a new file called students.db
    return conn

# initialise the database
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# add a student to the database
def add_student(name, age, grade):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO students (name, age, grade)
        VALUES (?, ?, ?)
    ''', (name, age, grade))
    conn.commit()
    conn.close()
    print(f"Student {name} added successfully!")

# view all students in the database
def view_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()

    if students:
        print("ID | Name | Age | Grade")
        for student in students:
            print(f"{student[0]} | {student[1]} | {student[2]} | {student[3]}")
    else:
        print("No students found.")

# handle user interaction
def main():
    init_db()  # Initialise the database (create table if not exists)
    
    while True:
        print("\nStudent Database")
        print("1. Add student")
        print("2. View students")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            grade = input("Enter student's grade: ")
            add_student(name, age, grade)
        
        elif choice == '2':
            view_students()
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
