from fastapi import FastAPI, APIRouter

router = APIRouter()


@router.get("/orders")
def get_orders():
    return {"message": "Order Route is working fine...."}
