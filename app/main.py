from fastapi import FastAPI

app = FastAPI(
    title="Enterprise AI Support Agent",
    description="Backend API for an AI-powered enterprise support system",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "Enterprise AI Support Agent API",
        "version": "0.1.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    return {
        "id": order_id,
        "customer_id": 1001,
        "status": "PAYMENT_PENDING",
        "payment_status": "FAILED",
        "shipping_status": "NOT_STARTED"
    }