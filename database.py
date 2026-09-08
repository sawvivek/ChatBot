import sqlite3

DATABASE_NAME = "faq.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection


def initialize_database():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS faqs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_faq(question, answer):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO faqs (question, answer)
        VALUES (?, ?)
        """,
        (question, answer)
    )

    connection.commit()
    connection.close()

def get_faq_by_id(faq_id):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, question, answer FROM faqs WHERE id = ?",
        (faq_id,)
    )

    faq = cursor.fetchone()

    connection.close()

    return faq
def delete_faq(faq_id):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM faqs
        WHERE id = ?
        """,
        (faq_id,)
    )

    connection.commit()
    connection.close()
def update_faq(faq_id, question, answer):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE faqs
        SET question = ?, answer = ?
        WHERE id = ?
        """,
        (question, answer, faq_id)
    )

    connection.commit()
    connection.close()

def get_all_faqs():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, question, answer FROM faqs"
    )

    faqs = cursor.fetchall()

    connection.close()

    return faqs

def import_faqs_from_file():
    connection = get_connection()
    cursor = connection.cursor()

    with open("data/faqs.txt", "r", encoding="utf-8") as file:

        for line in file:
            line = line.strip()

            if not line:
                continue

            question, answer = line.split("|", 1)

            cursor.execute(
                """
                INSERT INTO faqs (question, answer)
                VALUES (?, ?)
                """,
                (question, answer)
            )

    connection.commit()
    connection.close()

if __name__ == "__main__":
    faqs = get_all_faqs()

    for faq in faqs:
        print(faq)