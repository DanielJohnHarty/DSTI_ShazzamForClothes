import boto3
import pymysql
from ShazzamForClothes.config import LOADED_CONFIG

__all__ = ['Database']


class Database:
    """Database connection class."""

    def __init__(self, config = LOADED_CONFIG):
        self.host = config.get("aws_rds_parameters", "endpoint")
        self.username = config.get("aws_rds_parameters", "admin_user")
        self.password = config.get("aws_rds_parameters", "admin_password")
        self.port = config.get("aws_rds_parameters", "database_port")
        self.dbname = config.get("aws_rds_parameters", "database_name")
        self.conn = None

    def open_connection(self):
        """Connect to MySQL Database."""
        try:
            if self.conn is None:
                self.conn = pymysql.connect(
                    self.host,
                    user=self.username,
                    passwd=self.password,
                    db=self.dbname,
                    connect_timeout=5,
                )
        except pymysql.MySQLError as e:
            print(e)
            sys.exit()
        finally:
            print("Connection opened successfully.")

    def run_query(self, query):
        """Execute SQL query."""
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
                if "SELECT" in query:
                    records = []
                    cur.execute(query)
                    result = cur.fetchall()
                    for row in result:
                        records.append(row)
                    cur.close()
                    return records
                else:
                    result = cur.execute(query)
                    self.conn.commit()
                    affected = f"{cur.rowcount} rows affected."
                    cur.close()
                    return affected
        except pymysql.MySQLError as e:
            print(e)
        finally:
            if self.conn:
                self.conn.close()
                self.conn = None
                print("Database connection closed.")

    def add_raw_image(self, src_link):
        self.run_query(
            'INSERT INTO `RAW_IMAGES`(src_link,is_dead) VALUES("{}",FALSE)'.format(
                src_link
            )
        )

    def get_list_RAW_IMAGES(self):
        results = self.run_query("SELECT * FROM RAW_IMAGES;")
        return results

    def create_RAW_IMAGES_table(self):
        self.run_query(
            "CREATE TABLE RAW_IMAGES(id INT AUTO_INCREMENT PRIMARY KEY,src_link TEXT NOT NULL,is_dead BOOLEAN)"
        )


# db = Database()
# db.add_raw_image(src_link)
# r=db.get_list_RAW_IMAGES()