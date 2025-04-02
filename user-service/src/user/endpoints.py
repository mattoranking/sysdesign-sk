from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/",
    summary="Get all users",
    response_description="List of all users",
)
def list() -> dict:
    return {"message": "List of all users"}
