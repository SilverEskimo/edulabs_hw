class Branch:

    def __init__(self, branch_id: int, branch_name: str, branch_address: str, branch_city: str):
        self._branch_id = branch_id
        self._branch_name = branch_name
        self._branch_address = branch_address
        self._branch_city = branch_city

    def set_address(self, new_address: str) -> None:
        self._branch_address = new_address
