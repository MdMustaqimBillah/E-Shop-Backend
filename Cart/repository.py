from Repository.base_repository import BaseRepository
from Cart.models import Cart

class CartRepository(BaseRepository):
    def __init__(self):
        super().__init__(Cart)