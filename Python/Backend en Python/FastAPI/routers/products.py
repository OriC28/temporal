from fastapi import APIRouter

router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses={404: {"messaje": "No encontrado"}})

products = [
    "Producto 1",
    "Producto 2",
    "Producto 3",
    "Producto 4",
    "Producto 5"
]

@router.get("/")
async def get_products():
    return products

@router.get("/{id}")
async def get_products(id: int):
    return products[id]