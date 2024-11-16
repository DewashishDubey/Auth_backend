from pathlib import Path

class settings():
    db_url = 'postgresql://avnadmin:AVNS_ntHGcvKjKUKUSDGuaMK@pg-edf2e13c-80c1-4f50-a46c-1a73263469ef-auth2469057047-choreo-o.l.aivencloud.com:16359/defaultdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    allow_auto_generate_tables = True
    # base_path: str = str(Path(__file__).parent.absolute())
    # host: str = "0.0.0.0"
    # port: int = 7986