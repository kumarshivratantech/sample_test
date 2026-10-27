from fastapi import FastAPI, APIRouter, Depends, HTTPException
from app.router import register_routers


app = FastAPI(title="My Azure FastAPI Application")

register_routers(app)


def depends_method():
    return {"depends_message": "Here is the message"}


def validate_token() -> bool:
    return False


@app.get("/")
def home(data: dict = Depends(depends_method)):
    return {"message": "FastAPI is successfully running", "depends_message": data}


@app.get("/validate_user")
def validate_user(data: bool = Depends(validate_token)):
    return {"message": "I can access the application without any problem"}


def pass_parameter_on_depends(customer_id: int):
    return {"customer_id": customer_id}


@app.get("/parameter")
def pass_parameter(data: dict = Depends(pass_parameter_on_depends)):
    raise HTTPException(status_code=209, detail=f"{data['customer_id']}")
