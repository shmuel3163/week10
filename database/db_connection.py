import mysql.connector


class DB_connection:
    def get_connection(self):
        conn = mysql.connector.connect(
            user="root", password="1234", host="127.0.0.1", database="Intelligence_db"
        )
        return conn

    def create_database(self):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute("CREATE DATABASE if NOT EXISTS Intelligence_db")
        cur.execute("use Intelligence_db")
        conn.commit()
        cur.close()

    def create_tables(self):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute("""
CREATE TABLE if NOT EXISTS agents
(id INT AUTO_INCREMENT PRIMARY KEY,
`name` VARCHAR(50) ,
specialty VARCHAR(50),
is_active BOOLEAN DEFAULT True,
completed_missions INT DEFAULT 0,
failed_missions INT DEFAULT 0,
agent_rank ENUM('Junior','Senior','Commander') not NULL))
                    """)
        cur.execute("""
CREATE TABLE if NOT EXISTS missions(
`id` INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(100),
`description` TEXT,
`location` VARCHAR(100),
difficulty INT,
importance INT,
`status` VARCHAR(20) DEFAULT 'new',
risk_level VARCHAR(20),
assigned_agent_id INT DEFAULT NULL)""")
        conn.commit()
        cur.close()
