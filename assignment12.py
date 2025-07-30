import sqlite3

def create_database():
    conn = sqlite3.connect("school.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_students():
    students = [
        (1, 'Alice', 14, '8A'),
        (2, 'Bob', 15, '9B'),
        (3, 'Charlie', 13, '7C'),
        (4, 'Diana', 14, '8A'),
        (5, 'Ethan', 16, '10B')
    ]
    conn = sqlite3.connect("school.db")
    cur = conn.cursor()
    cur.executemany("INSERT OR IGNORE INTO students (id, name, age, grade) VALUES (?, ?, ?, ?)", students)
    conn.commit()
    conn.close()

def fetch_all_students():
    conn = sqlite3.connect("school.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    for row in cur.fetchall():
        print(row)
    conn.close()

def search_by_grade(grade):
    conn = sqlite3.connect("school.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE grade = ?", (grade,))
    results = cur.fetchall()
    if results:
        for student in results:
            print(student)
    else:
        print(f"No students found in grade {grade}")
    conn.close()

def update_age(student_id, new_age):
    conn = sqlite3.connect("school.db")
    cur = conn.cursor()
    cur.execute("UPDATE students SET age = ? WHERE id = ?", (new_age, student_id))
    conn.commit()
    print(f"Updated student ID {student_id} age to {new_age}")
    conn.close()

def delete_student(student_id):
    conn = sqlite3.connect("school.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print(f"Deleted student ID {student_id}")
    conn.close()

create_database()
insert_students()

print("All Students:")
fetch_all_students()

print("\nStudents in Grade '8A':")
search_by_grade('8A')

print("\nUpdating Age of Student with ID 3:")
update_age(3, 14)

print("\nDeleting Student with ID 2:")
delete_student(2)

print("\nFinal Student List:")
fetch_all_students()
