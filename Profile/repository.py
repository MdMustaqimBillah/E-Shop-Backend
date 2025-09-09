from Base_Repository.base_repository import BaseRepository
from Profile.models import UserProfile

class ProfileRepository(BaseRepository):
    def __init__(self):
        super().__init__(UserProfile)