import json

class OrderForm:
    def __init__(self, form_data):
        self.fullname = form_data.get('fullname', '')
        self.file = form_data.get('file', '')
        self.quantity = form_data.get('quantity', '')

    def save_to_json(self, filename='order_data.json'):
        order_data = {
            "fullname": self.fullname,
            "file": self.file,
            "quantity": self.quantity
        }
        
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.append(order_data)

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)