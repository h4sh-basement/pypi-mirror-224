import os
import psycopg2
import re
from typing import Dict, List

from rich.console import Console

from lumaCLI.utils import run_command


console = Console()


def create_conn(username, password, host, port, database):
    return psycopg2.connect(
        user=username, password=password, host=host, port=port, dbname=database
    )


def generate_pg_dump_content(
    username: str,
    database: str,
    password: str,
    host: str = "localhost",
    port: str = "5432",
) -> str:
    """
    Dump the specified PostgreSQL database schema information, table names,
    column information, row counts, and other details to a dump file.
    """
    original_pgpassword_env = os.getenv("PGPASSWORD")
    os.environ["PGPASSWORD"] = password
    command = f"pg_dump -h {host} -p {port} -U {username} -d {database} --column-inserts --rows-per-insert=1 --no-password"
    result = run_command(command, capture_output=True)
    os.environ["PGPASSWORD"] = original_pgpassword_env
    return result


def get_pg_dump_tables_info(content) -> List[Dict]:
    # Find table creation statements
    table_creations = re.findall(
        r"CREATE TABLE (.*?)\.(.*?) \((.*?)\);", content, re.DOTALL
    )

    # Find row counts and table sizes
    row_counts = re.findall(
        r"-- Name: (.*?); Type: TABLE;.*?-- Total rows: (\base_dict+)", content
    )
    table_sizes = re.findall(
        r"-- Name: (.*?); Type: TABLE;.*?-- Size: (.*?)\n", content
    )

    # Find table owners
    table_owners = re.findall(r"ALTER TABLE (.*?)\.(.*?) OWNER TO (.*?);", content)

    # Find column defaults
    column_defaults = re.findall(
        r"ALTER TABLE ONLY (.*?)\.(.*?) ALTER COLUMN (.*?) SET DEFAULT (.*?);", content
    )

    # Find primary keys
    primary_keys = re.findall(
        r"ALTER TABLE ONLY (.*?)\.(.*?)\s+ADD CONSTRAINT (.*?) PRIMARY KEY \((.*?)\);",
        content,
    )

    # Find foreign keys
    foreign_keys = re.findall(
        r"ALTER TABLE ONLY (.*?)\.(.*?)\s+ADD CONSTRAINT (.*?) FOREIGN KEY \((.*?)\) REFERENCES (.*?)\.(.*?)\(id\);",
        content,
    )

    # Initialize the dictionary
    tables_list = []

    # Process each table
    for table_schema, table_name, table_definition in table_creations:
        # Extract column names and types
        columns = re.findall(r"(\w+)\s+([\w\s()]+)(?:,|\))", table_definition)

        # Store column names and types in a dictionary
        columns_dict = {
            column_name: column_type.strip() for column_name, column_type in columns
        }

        # Find row count for the table
        row_count = next((count for name, count in row_counts if name == table_name), 0)

        # Find table size (in MB) for the table
        table_size = next(
            (size for name, size in table_sizes if name == table_name), "Unknown"
        )

        # Find table owner
        table_owner = next(
            (owner for schema, name, owner in table_owners if name == table_name),
            "Unknown",
        )

        # Find column defaults
        column_default_dict = {
            column_name: default_value
            for schema, table, column_name, default_value in column_defaults
            if table == table_name
        }

        # Find primary key
        primary_key = next(
            (key for schema, name, _, key in primary_keys if name == table_name), None
        )

        # Find foreign keys
        foreign_keys_list = [
            {"constraint_name": name, "column": column, "ref_table": ref_table}
            for schema, table, name, column, ref_schema, ref_table in foreign_keys
            if table == table_name
        ]

        # Add the table details to the schema dictionary
        tables_list.append(
            {
                "table_name": table_name,
                "table_schema": table_schema,
                "columns": columns_dict,
                "row_count": int(row_count),
                "table_size": table_size,
                "owner": table_owner,
                "column_defaults": column_default_dict,
                "primary_key": primary_key,
                "foreign_keys": foreign_keys_list,
            }
        )

    return tables_list


def get_pg_dump_views_info(content) -> List[Dict]:
    # Find view creation statements
    view_creations = re.findall(
        r"CREATE VIEW (.*?)\.(.*?) AS(.*?);", content, re.DOTALL
    )

    # Initialize the list for storing view information
    views_list = []

    # Process each view
    for view_schema, view_name, view_definition in view_creations:
        # Remove newline characters and extra spaces
        view_definition = re.sub(r"\s+", " ", view_definition)

        # Extract column names and aliases
        columns = re.findall(r"(\w+)\s+AS\s+(\w+)", view_definition)

        # Store column names and aliases in a dictionary
        columns_dict = {
            column_name: column_alias for column_name, column_alias in columns
        }

        # Add the view details to the list
        views_list.append(
            {
                "view_name": view_name,
                "view_schema": view_schema,
                "columns": columns_dict,
            }
        )

    return views_list


def get_tables_size_info(
    username: str,
    database: str,
    password: str,
    host: str = "localhost",
    port: str = "5432",
):
    """
    Get size information of the specified PostgreSQL database, tables, and indexes.
    """

    conn = create_conn(username, password, host, port, database)
    cur = conn.cursor()
    cur.execute(
        """
        SELECT table_schema, 
               table_name,
               pg_size_pretty(pg_total_relation_size(('"' || table_schema || '"."' || table_name || '"'))) AS table_size
        FROM information_schema.tables
        ORDER BY pg_total_relation_size(('"' || table_schema || '"."' || table_name || '"')) DESC;
    """
    )
    rows = cur.fetchall()

    table_size_dict = {}

    for table_schema, table_name, table_size in rows:
        table_size_dict[(table_schema, table_name)] = table_size
    return table_size_dict


def get_tables_row_counts(
    username: str,
    database: str,
    password: str,
    host: str = "localhost",
    port: str = "5432",
):
    """
    Get row counts for all tables in the specified PostgreSQL database.
    """
    conn = create_conn(username, password, host, port, database)
    cur = conn.cursor()
    cur.execute(
        """
        SELECT schemaname,relname,n_live_tup 
        FROM pg_stat_user_tables 
        ORDER BY n_live_tup DESC;
    """
    )
    rows = cur.fetchall()
    row_count_dict = {}

    for table_schema, table_name, row_count in rows:
        row_count_dict[(table_schema, table_name)] = row_count
    return row_count_dict


def get_db_metadata(
    username: str,
    database: str,
    password: str,
    host: str = "localhost",
    port: str = "5432",
) -> Dict[str, List[Dict]]:
    dump_content: str = generate_pg_dump_content(
        username=username, database=database, host=host, port=port, password=password
    )
    # Transform SQL dump to dictionary
    tables_info: List[Dict] = get_pg_dump_tables_info(dump_content)

    # Get row count information
    row_count_dict: dict = get_tables_row_counts(
        username=username, database=database, host=host, port=port, password=password
    )

    # Get table size information:
    table_size_dict: dict = get_tables_size_info(
        username=username, database=database, host=host, port=port, password=password
    )

    for table in tables_info:
        key = (table["table_schema"], table["table_name"])
        table["row_count"] = row_count_dict.get(key, 0)
        table["table_size"] = table_size_dict.get(key, 0)

    views_info: List[Dict] = get_pg_dump_views_info(dump_content)

    database_metadata = {"tables": tables_info, "views": views_info}

    return database_metadata


if __name__ == "__main__":
    pass
