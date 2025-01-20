import os

from dotenv import load_dotenv

load_dotenv(
    dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
)

port = os.getenv("PORT", "8000")
uri = "ws://localhost:" + str(port)
