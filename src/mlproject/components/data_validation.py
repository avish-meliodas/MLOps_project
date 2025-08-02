import os
from mlproject import logger
import pandas as pd
from mlproject.config.configuration import DataValidationConfig
from pathlib import Path

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self)->bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            logger.exception(e)

    def check_file_size(self)->bool:
        try:
            df = pd.read_csv(Path(self.config.unzip_data_dir))
            file_size = df.shape[0]

            if(file_size > 50):
                validation_status = True
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation status: {validation_status}")
            else:
                validation_status = False
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation status: {validation_status}")
        except Exception as e:
            logger.exception(e)

