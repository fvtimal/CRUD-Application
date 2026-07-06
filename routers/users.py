from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post("/register")
async def register():
    return{
        "message": "Registration endpoint working"
    }