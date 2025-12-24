import os
import mlflow

from dotenv import load_dotenv

mlflow.litellm.autolog()

load_dotenv()

Config = {
  "cerebras": {
    "api_key": os.environ["CEREBRAS_API_KEY"],
  },
}
