from Repository.base_repository import BaseRepository
from Orders.models import Order

class OrderRepository(BaseRepository):
    def __init__(self):
        super().__init__(Order)