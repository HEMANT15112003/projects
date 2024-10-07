import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


class StudentManagementSystem:
    def __init__(self):
        # Establish a database connection
        self.connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_DATABASE'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        self.cursor = self.connection.cursor()

    def create_student(self):
        print("Adding a new student")
        name = input("Enter name: ")
        age = input("Enter age: ")
        grade = input("Enter grade: ")
        email = input("Enter email: ")

        insert_query = """INSERT INTO students (name, age, grade, email) 
                          VALUES (%s, %s, %s, %s)"""
        values = (name, age, grade, email)

        try:
            self.cursor.execute(insert_query, values)
            self.connection.commit()
            print("Student added successfully.")
        except mysql.connector.Error as err:
            print("Error: {}".format(err))

    def read_students(self):
        print("Fetching all students")
        select_query = "SELECT * FROM students"
        self.cursor.execute(select_query)
        rows = self.cursor.fetchall()

        print("ID | Name | Age | Grade | Email")
        print("-----------------------------")
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")

    def update_student(self, student_id):
        print("Updating details for Student ID:", student_id)
        
        name = input("Enter new name: ")
        age = input("Enter new age: ")
        grade = input("Enter new grade: ")
        email = input("Enter new email: ")

        update_query = """UPDATE students 
                          SET name = %s, age = %s, grade = %s, email = %s 
                          WHERE id = %s"""
        values = (name, age, grade, email, student_id)

        try:
            self.cursor.execute(update_query, values)
            self.connection.commit()
            print("Student details updated successfully.")
        except mysql.connector.Error as err:
            print("Error: {}".format(err))

    def delete_student(self, student_id):
        print("Deleting Student ID:", student_id)

        delete_query = "DELETE FROM students WHERE id = %s"
        values = (student_id,)

        try:
            self.cursor.execute(delete_query, values)
            self.connection.commit()
            print("Student deleted successfully.")
        except mysql.connector.Error as err:
            print("Error: {}".format(err))

    def close(self):
        self.cursor.close()
        self.connection.close()

def main():
    sms = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            sms.create_student()
        elif choice == '2':
            sms.read_students()
        elif choice == '3':
            student_id = input("Enter Student ID to update: ")
            sms.update_student(student_id)
        elif choice == '4':
            student_id = input("Enter Student ID to delete: ")
            sms.delete_student(student_id)
        elif choice == '5':
            sms.close()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
