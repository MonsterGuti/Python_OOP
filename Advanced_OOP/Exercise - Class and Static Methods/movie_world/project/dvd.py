class DVD:
    MONTHS = {
        "01": "January", "1": "January",
        "02": "February", "2": "February",
        "03": "March", "3": "March",
        "04": "April", "4": "April",
        "05": "May", "5": "May",
        "06": "June", "6": "June",
        "07": "July", "7": "July",
        "08": "August", "8": "August",
        "09": "September", "9": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }

    def __init__(self, name: str, dvd_id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = dvd_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, dvd_id: int, name: str, date: str, age_restriction: int):
        day, month, year = date.split(".")
        month_name = cls.MONTHS.get(month, "Unknown")
        return cls(name, dvd_id, int(year), month_name, age_restriction)

    def __repr__(self):
        status = "rented" if self.is_rented else "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}"
