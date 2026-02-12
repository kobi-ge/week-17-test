from fastapi import FastAPI

app = FastAPI()
@app.get("/analytics/top-customers")
def get_top_10():
    pass

@app.get("/analytics/customers-without-orders")
def get_inactive_customers():
    pass

@app.get("/analytics/zero-credit-active-customers")
def get_no_credit_customers():
    pass


