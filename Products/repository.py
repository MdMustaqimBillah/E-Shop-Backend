from Base_Repository.base_repository import BaseRepository
from Products.models import Product

class ProductRepository(BaseRepository):
    def __init__(self):
        super().__init__(Product)