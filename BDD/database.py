class Database:
    def __init__(self):
        self.records = []

    def clear(self):
        self.records = []

    def add_record(self, data):
        if not data:
            raise ValueError("Некорректные данные.")
        self.records.append(data)

    def edit_record(self, old_data, new_data):
        if old_data in self.records:
            index = self.records.index(old_data)
            self.records[index] = new_data

    def delete_record(self, data):
        if data in self.records:
            self.records.remove(data)

    def record_exists(self, data):
        return data in self.records