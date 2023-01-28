class Branch:

    def __init__(self, branch_id: int, branch_name: str, branch_address: str, branch_city: str):
        self._branch_id = branch_id
        self._branch_name = branch_name.lower()
        self._branch_address = branch_address.lower()
        self._branch_city = branch_city.lower()

    def set_address(self, new_address: str) -> None:
        self._branch_address = new_address

    def get_branch_city(self):
        return self._branch_city

    def __str__(self):
        return f"Branch ID: {self._branch_id}\nBranch Name: {self._branch_name.title()},\
               \nBranch Address: {self._branch_address.title()},{self._branch_city.title()}"

