from fastapi import FastAPI, Cookie, Body
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()

# @app.get("/products/recommendations")
# async def get_recommendation(session_id : Annotated[str | None, Cookie()]= None):
#     if session_id:
#         return {"message" : f"Rcommendations for session {session_id}", "session_id" : session_id}
#     return {"message" : "No message ID provided, showing default recommendation"}

# ***************************** COOKIE PARAMETER WITH PYDANTIC MODEL *********************
# class ProductCookie(BaseModel):
#     session_id : str
#     preferred_category : str | None = None
#     tracking_id : str |None = None
# @app.get("/product/recommendations")
# async def get_recommendation(cookies : Annotated[ProductCookie, Cookie()]):
#     response = {"session_id" : cookies.session_id}
#     if cookies.preferred_category:
#         response["message"] = f"Recommendations for {cookies.preferred_category} products"
#     else:
#         response["message"] = f"Default recommandation for session {cookies.session_id}"
#     if cookies.tracking_id:
#         response["tracking_id"] = cookies.tracking_id
#     return response

class ProductCookie(BaseModel):
    model_config = {"extra": "forbid"}
    session_id : str = Field(title="session ID", description="user session identifier")
    preferred_category : str | None = Field(default=None, title="Preferred Category", description="User preferred product category")
    tracking_id : str |None = None

class PriceFilter(BaseModel):
    min_price : float = Field(ge=0, title="Minimum Price", 
    description= "Minimum price of recommandation")
    max_price: float | None = Field(default= None, title="Maximum Price", description="Maximum Price for recommendations")
@app.post("/product/recommendations")
async def get_recommendation(
    cookies : Annotated[ProductCookie, Cookie()],
    price_filter: Annotated[PriceFilter, Body(embed=True)]
    ):
    response = {"session_id" : cookies.session_id}
    if cookies.preferred_category:
        response["category"] = cookies.preferred_category
    response["price_range"] = {
        "min_price" : price_filter.min_price,
        "max_price" : price_filter.max_price
    }
    response["message"] = f"Recommendation for session {cookies.session_id} with price range {price_filter.min_price} to {price_filter.max_price or 'unlimited'}"
    return response