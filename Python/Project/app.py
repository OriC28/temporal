from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from routers import user

app = FastAPI()

# work whenever a request is made
@app.middleware('http')
async def http_error_handler(request: Request, call_next):
    try:
        print("Middleware is running...")
        return await call_next(request)
    except Exception as e:
        content = f"detail: {str(e)}"
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return JSONResponse(content=content, status_code=status_code)

# add router user
app.include_router(prefix="/users", router=user.user)