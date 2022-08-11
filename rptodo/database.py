import configparser
from pathlib import Path
from rptodo import DB_WRITE_ERROR, SUCCESS

DEFAULT_DB_FILE_PATH = Path.home().joinpath(
    "." + Path.home().stem + "_todo.json"
)

def get_database_path(config_file: Path) -> Path:
    """Return the current path to the to-do database"""
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    return Path(config_parser["General"]["Database"])

def init_database(db_path: Path) -> int:
    """Create the to-do database"""
    try:
        db_path.write_text("[]") # Empty list
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR