import os
from dotenv import load_dotenv


load_dotenv()


OPEN_AI_API_KEY=os.getenv("open_ai_key")
IAM_CUSTOMER_SECRET_KEY=os.getenv("iam_customer_secret_key")
IAM_APP_IDENTIFIER=os.getenv("iam_app_identifier")
IAM_API_SERVER_URL=os.getenv("iam_api_server_url")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
LLAMA_CKPT_DIR = "/home/marktine/Desktop/AI_Layer/model"
LLAMA_TOKENIZER_PATH = "model/tokenizer.model"
