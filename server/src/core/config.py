from pydantic_settings import SettingsConfigDict,BaseSettings
from pathlib import Path

ENV_FILE = Path(__file__).resolve().parent.parent.parent/".env"

class DBSettings(BaseSettings):
    DB_URL : str

    model_config = SettingsConfigDict(env_file=ENV_FILE)

db_settings = DBSettings()

