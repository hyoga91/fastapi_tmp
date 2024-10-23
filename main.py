from fastapi import FastAPI

from utils.create_admin import register_user
from dotenv import load_dotenv
from router.main import router

load_dotenv()

app = FastAPI()
app.include_router(router)
register_user()

@app.get('/health')
def health_check():
	return "ok"
