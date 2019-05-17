import psycopg2


def create_tables():
    commands = (
        """
       CREATE TABLE students (
               student_id serial PRIMARY KEY NOT NULL, 
               student_name character varying(100) NOT NULL, 
               gpa numeric(10, 2), 
               birth timestamp with time zone
               )
        """,
        """ CREATE TABLE course (
                course_id SERIAL PRIMARY KEY NOT NULL,
                course_name character varying(100) NOT NULL
               )
        """,
        """ CREATE TABLE course_students (
                        student_id INTEGER NOT NULL,
                        course_id INTEGER NOT NULL,
                        PRIMARY KEY (student_id , course_id),
                        FOREIGN KEY(student_id)
                            REFERENCES students (student_id)
                            ON UPDATE CASCADE ON DELETE CASCADE,
                        FOREIGN KEY(course_id)
                            REFERENCES students (student_id)
                            ON UPDATE CASCADE ON DELETE CASCADE
               )
        """)
    conn = None
    try:
        conn = psycopg2.connect(
  database="postgres",
  user="postgres",
  password="123456789",
  host="127.0.0.1",
  port="5432"
)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def get_students(students):
    sql = ("""SELECT * FROM students;
        """)
    conn = None
    try:
        conn = psycopg2.connect(
  database="postgres",
  user="postgres",
  password="123456789",
  host="127.0.0.1",
  port="5432"
)
        cur = conn.cursor()
        cur.execute(sql, (students,))
        row = cur.fetchall()
        while row is not None:
            print(row)
            row = cur.fetchone()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def add_student(student_list):
    sql = ("""INSERT INTO students(student_name, gpa, birth) 
           VALUES(%s, %s, %s) RETURNING student_id;
           """)
    conn = None
    student_id = None
    try:
        conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="123456789",
            host="127.0.0.1",
            port="5432"
        )
        cur = conn.cursor()
        cur.executemany(sql, student_list)
        student_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return student_id


def add_students(student_list, course_name):
    insert_course = "INSERT INTO course(course_name) VALUES(%s) RETURNING course_id;"
    assign_student = "INSERT INTO course_students(student_id,course_id) VALUES(%s,%s);"
    conn = None
    try:
        conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="123456789",
            host="127.0.0.1",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(insert_course, (course_name,))
        course_id = cur.fetchone()[0]
        for student_id in student_list:
            cur.execute(assign_student, (student_id, course_id))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def get_student(course_id):
    command = ("""
    CREATE FUNCTION get_student_course(id integer)
       RETURNS TABLE(course_id INTEGER, course_name character varying(100)) AS
       $$
    BEGIN
       RETURN QUERY
       SELECT course.course_id, course.course_name
       FROM course
       INNER JOIN course_students on course_students.course_id = course.course_id
       WHERE student_id = id;
    END; $$
    LANGUAGE plpgsql;
    """
    )
    conn = None
    try:
        conn = psycopg2.connect(
  database="postgres",
  user="postgres",
  password="123456789",
  host="127.0.0.1",
  port="5432"
)
        cur = conn.cursor()
        cur.execute(command)
        cur.callproc('get_student_course', (course_id,))
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    student_list = [('Markov', '4', '01.09.1990')]
    create_tables()
    add_student(student_list)