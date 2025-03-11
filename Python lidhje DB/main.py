import mysql.connector
from mysql.connector import Error


def get_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='gym'
        )
        return connection
    except Error as e:
        print("Error while connecting to MySQL: ", e)
        return None

def select_data():
    conn = get_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        query = "SELECT * FROM users"
        cursor.execute(query)
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print("No records found. ")
    except Error as e:
        print("Error selecting data: ", e)
    finally:
        cursor.close()
        conn.close()
def insert_data():
    conn = get_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        emri = input("Enter Emri: ")
        mbiemri = input("Enter Mbiemri: ")
        mosha = input("Enter Mosha(Integer): ")
        email = input("Enter Email: ")

        query = "INSERT INTO users (emri, mbiemri, mosha, email) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (emri, mbiemri, mosha, email))

        conn.commit()
        print("Data inserted successfully!")
    except Error as e:
        print("Error inserting data: ", e)
    finally:
        cursor.close()
        conn.close()

def update_data():
    conn = get_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        user_id = input("Enter User ID to update: ")
        new_email = input("Enter new Email: ")

        query = "UPDATE users SET email = %s WHERE id = %s"
        cursor.execute(query, (new_email, user_id))

        conn.commit()
        print("Data updated successfully!")
    except Error as e:
        print("Error updating data: ", e)
    finally:
        cursor.close()
        conn.close()

def delete_data():
    conn = get_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        user_id = input("Enter User ID to delete: ")

        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))

        conn.commit()
        print("Data deleted successfully!")
    except Error as e:
        print("Error deleting data: ", e)
    finally:
        cursor.close()
        conn.close()


def main():
    while True:
        print("\n ---Menu---")
        print("1. Select")
        print("2. Insert")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            select_data()
        elif choice == "2":
            insert_data()
        elif choice == "3":
            update_data()
        elif choice == "4":
            delete_data()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, Please try again.")


if __name__ == "__main__":
    main()
