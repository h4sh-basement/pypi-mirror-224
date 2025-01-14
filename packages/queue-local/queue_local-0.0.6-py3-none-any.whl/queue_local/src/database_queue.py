from datetime import datetime, timezone

from circles_local_database_python.connection import Connection
from logger_local.LoggerLocal import logger_local

from .our_queue import OurQueue

QUEUE_LOCAL_COMPONENT_ID = 155
TABLE = "queue_item"


class DatabaseQueue(OurQueue):
    def __init__(self):
        self.logger = logger_local  # maybe we'll replace to logger remote in the future.
        self.logger.init(object={'component_id': QUEUE_LOCAL_COMPONENT_ID})
        self.conn = Connection("queue")
        self.conn.connect()

    def push(self, entry: dict) -> None:
        """Pushes a new entry to the queue.
        `entry` should have the following format:
        {"item": "xyz", "action_id": 0} """
        created_user_id = 0  # TODO
        if not isinstance(entry, dict) or any(x not in entry for x in ("item", "action_id", "parameters_json")):
            self.logger.warn("push to the queue database invalid argument")
            raise ValueError("You must provide item, action_id and parameters_json inside `entry`")
        try:
            self.logger.start("Pushing entry to the queue database", object={"entry": entry})
            escaped_parameters_json = entry['parameters_json'].replace("'", "\\'")
            sql = f"INSERT INTO queue.{TABLE + '_table'} (item, action_id, parameters_json, created_user_id) " \
                  f"VALUES (%s, %s, %s, %s)"
            values = (entry['item'], entry['action_id'], escaped_parameters_json, created_user_id)
            self.conn.execute(sql, values)
            self.logger.end("Entry pushed to the queue database successfully")
        except Exception as e:
            self.logger.exception("Error while pushing entry to the queue database", object=e)

    def get(self) -> dict:
        """Returns the first item from the queue and marks it as taken"""
        updated_user_id = 0  # TODO
        row = {}
        try:
            self.logger.start("Getting entry from the queue database")
            row = self.peek()
            if row:
                end_timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
                sql = f"UPDATE queue.{TABLE + '_table'} SET end_timestamp = %s, updated_user_id = %s WHERE queue_item_id = %s"
                values = (end_timestamp, updated_user_id, row['queue_item_id'])
                self.conn.execute(sql, values)
                self.logger.end("Entry retrieved from the queue database successfully", object={"return": str(row)})
            else:
                self.logger.end("The queue is empty")
        except Exception as e:
            self.logger.exception("Error while getting entry from the queue database", object=e)
        return row

    def peek(self) -> dict:
        """Get the first item in the queue without changing it"""
        d = {}
        try:
            self.logger.start("Peeking entry from the queue database")

            row = self.conn.fetchone(
                f"SELECT * FROM queue.{TABLE + '_view'} WHERE end_timestamp IS NULL "
                f"ORDER BY created_timestamp LIMIT 1")
            d = self._tuple_to_dict(row)
            self.logger.end("Entry peeked from the queue database successfully" if d else "The queue is empty")
        except Exception as e:
            self.logger.exception("Error while peeking entry from the queue database", object=e)
        return d

    def get_by_action_ids(self, action_ids: tuple) -> dict:
        """Returns the first item in the queue that it's action_id is in action_ids"""
        if not isinstance(action_ids, tuple):
            self.logger.warn("get_by_action_ids (queue database) invalid argument")
            raise ValueError("`action_ids` must be a tuple")
        row = {}
        try:
            self.logger.start("Getting entry by action_ids from the queue database", object={"action_ids": action_ids})
            action_ids = action_ids if len(action_ids) != 1 else f"({action_ids[0]})"
            sql = f"SELECT * FROM queue.{TABLE + '_view'} WHERE end_timestamp IS NULL " \
                  f"AND action_id IN {action_ids} " \
                  f"ORDER BY created_timestamp LIMIT 1"

            row = self._tuple_to_dict(self.conn.fetchone(sql))
            if row:
                end_timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
                sql = f"UPDATE queue.{TABLE + '_table'} SET end_timestamp = %s WHERE queue_item_id = %s"
                values = (end_timestamp, row['queue_item_id'])
                self.conn.execute(sql, values)
            self.logger.end("Entry retrieved from the queue database by action_ids successfully", object={"return": str(row)})
        except Exception as e:
            self.logger.exception("Error while getting entry from the queue database by action_ids from database", object=e)
        return row

    def _tuple_to_dict(self, entry: tuple) -> dict:
        desc = self.conn.get_description()
        column_names = [col[0] for col in desc]
        return dict(zip(column_names, entry or tuple()))
