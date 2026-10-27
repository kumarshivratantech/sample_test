from fastapi import FastAPI, APIRouter, HTTPException, Depends
from app.customer import router as customer_router
from app.order import router as order_router


def register_routers(app: FastAPI):
    app.include_router(
        customer_router,
        prefix="/v1/customer",
        tags=["Customer"],
        dependencies=[Depends(validate_user_token)],
    )
    app.include_router(
        order_router,
        prefix="/v1/order",
        tags=["Order"],
        dependencies=[Depends(validate_user_token)],
    )


def validate_user_token(token: str = "demo-token"):
    if token != "demo-token":
        raise HTTPException(status_code=401, detail="Invalid Token")
