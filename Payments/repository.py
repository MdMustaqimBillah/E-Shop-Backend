from Repository.base_repository import BaseRepository
from Payments.models import Payment_Billing
class PaymentBillingRepository(BaseRepository):
    def __init__(self):
        super().init(Payment_Billing)