from apartment import Apartment


class ApartmentForSale(Apartment):
    def __init__(self,
                 address: str,
                 rooms_num: float,
                 parking_type: str,
                 size_in_sq_meters: float,
                 floor: int,
                 has_balcony: bool,
                 is_penthouse: bool,
                 is_villa: bool,
                 monthly_municipal_tax: float,
                 sale_price: float,
                 deal_state: float):
        super().__init__(address, rooms_num, parking_type, size_in_sq_meters, floor, has_balcony, is_penthouse,
                         is_villa, monthly_municipal_tax, deal_state)
        self._sale_price = sale_price

    def get_agency_fee(self):
        return self._sale_price * 0.02
