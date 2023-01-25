class Apartment:
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
                 deal_state: float):
        self._address = address,
        self._rooms_num = rooms_num,
        self._parking_type = parking_type,
        self._size_in_sq_meters = size_in_sq_meters,
        self._floor = floor,
        self._has_balcony = has_balcony,
        self._is_penthouse = is_penthouse,
        self._is_villa = is_villa,
        self._monthly_municipal_tax = monthly_municipal_tax
        self._deal_state = deal_state

    def _set_deal_state(self, deal_state: str):
        self._deal_state = deal_state

    def get_annual_municipal_tax(self):
        return self._monthly_municipal_tax * 12

    def close_deal(self):
        self._set_deal_state("closed")

    def get_agency_fee(self):
        return




