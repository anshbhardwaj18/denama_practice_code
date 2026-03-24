# from fastapi import FastAPI, Form
# from fastapi.responses import HTMLResponse
# from typing import Annotated
# from pydantic import BaseModel, Field
# app = FastAPI()


# # SIMPLE HTML FORM FOR TESTING
# @app.get("/", response_class=HTMLResponse)
# async def get_data():
#     return """
#     <html>
#         <body>
#             <h2>Login Form</h2>
#             <form action= "/login/" method="post">
#                 <label for= "username">Username:</label><br>
#                 <input type="text" id="username"
#                 name= "username"><br>
#                 <label for="password">Password:</label><br>
#                 <input type="password" id="password"
#                 name= "password"><br><br>
#                 <input type= "Submit" value="Submit">
#             </form>
#         </body>
#     </html>
#     """ 

# @app.post("/login/")
# async def login_user(
#     username: Annotated[str, Form(min_length=3)],
#     password: Annotated[str, Form(min_length=3, max_length=5)]
#     ):
#     return {"username" : username, "password-length" : len(password)}

# USING PYDANTIC MODEL
# class FormData(BaseModel):
#     username: str
#     password: str

# class FormData(BaseModel):
#     username: str = Field(min_length=3)
#     password: str = Field(min_length=3, max_length=10)

# @app.post("/login")
# async def login_user(data : Annotated[FormData, Form()]):
#     return data