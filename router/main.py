from fastapi import APIRouter
from router.auth.auth import auth

router = APIRouter()

router.include_router(auth)