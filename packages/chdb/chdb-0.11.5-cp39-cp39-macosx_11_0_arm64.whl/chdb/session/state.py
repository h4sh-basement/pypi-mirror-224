import tempfile
import shutil

from chdb import query_stateful


class Session():
    """
    Session will keep the state of query. All DDL and DML state will be kept in a dir.
    Dir path could be passed in as an argument. If not, a temporary dir will be created.

    If path is not specified, the temporary dir will be deleted when the Session object is deleted.
    Otherwise path will be kept.
    
    Note: The default database is "_local" and the default engine is "Memory" which means all data 
    will be stored in memory. If you want to store data in disk, you should create another database.
    """

    def __init__(self, path=None):
        if path is None:
            self._cleanup = True
            self._path = tempfile.mkdtemp()
        else:
            self._cleanup = False
            self._path = path

    def __del__(self):
        if self._cleanup:
            self.cleanup()

    def cleanup(self):
        shutil.rmtree(self._path)

    def query(self, sql, fmt="CSV"):
        """
        Execute a query.
        """
        return query_stateful(sql, fmt, path=self._path)
