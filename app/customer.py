from fastapi import FastAPI, APIRouter

router = APIRouter()


@router.get("/customers")
def get_customers():
    return {"message": "Customer Route is working fine...."}
