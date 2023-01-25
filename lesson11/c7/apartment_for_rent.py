from apartment import Apartment


class ApartmentForRent(Apartment):
    def __init__(self,
                 rent_price_per_month: float,
                 address: str,
                 rooms_num: float,
                 parking_type: str,
                 size_in_sq_meters: float,
                 floor: int,
                 has_balcony: bool,
                 is_penthouse: bool,
                 is_villa: bool,
                 monthly_municipal_tax: float,
                 deal_state: float,
                 pets_allowed: bool):
        super().__init__(address, rooms_num, parking_type, size_in_sq_meters, floor, has_balcony, is_penthouse,
                         is_villa, monthly_municipal_tax, deal_state)
        self._rent_price_per_month = rent_price_per_month
        self._pets_allowed = pets_allowed

    def get_annual_rent_price(self):
        return self._rent_price_per_month * 12

    def get_agency_fee(self):
        return self._rent_price_per_month






