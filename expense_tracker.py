import argparse  # for parsing command arguments, cli
import datetime 
import json  # for storage
import pandas as pd

class Details:
    # Initialize the class
    def __init__(self, ID, Date, Description, Amount):
        self.id = ID
        self.date = Date  # Store the specific date value
        self.description = Description
        self.amount = Amount

    def display(self):
        # Create a DataFrame for each detail
        data = pd.DataFrame([{
            'ID': self.id,
            'Date': self.date,
            'Description': self.description,
            'Amount': self.amount
        }])
        return data

class DetailsManager:
    def __init__(self, storage_file='expense_track.json'):
        self.storage_file = storage_file
        self.details_dict = self.load_details()

    def load_details(self):
        try:
            with open(self.storage_file, 'r') as f:
                file_content = f.read().strip()
                if not file_content:
                    return {}
                data = json.loads(file_content)
                return {
                    detail['id']: Details(
                        ID=detail['id'],
                        Date=datetime.datetime.strptime(detail['date'], '%Y-%m-%d').date(),  # Convert the date back to a datetime.date object
                        Description=detail['description'],
                        Amount=detail['amount']
                    ) for detail in data
                }
        except FileNotFoundError:
            return {}

    '''In load_details(), the date is converted back to a datetime.date object using strptime().'''
    
    '''Python's json module cannot serialize datetime.date objects by default. You need to convert the date object to a string (e.g., YYYY-MM-DD) before saving it to a JSON file. In the save_details method, convert the date to a string before dumping the data into JSON.'''

    def save_details(self):
        with open(self.storage_file, 'w') as f:
            data = [{
                'id': detail.id,
                'date': detail.date.strftime('%Y-%m-%d'),  # Convert date back to string format before saving to JSON
                'description': detail.description,
                'amount': detail.amount
            } for detail in self.details_dict.values()]
            json.dump(data, f, indent=4)
            print(f'Details saved')

    def add_details(self, ID, Date, Description, Amount):
        if ID in self.details_dict:
            print(f"Detail with ID {ID} already exists")
            return
        try:
            # Convert date string to a datetime.date object
            date_obj = datetime.datetime.strptime(Date, '%Y-%m-%d').date()
        except ValueError:
            print(f"Invalid date format: {Date}. Use YYYY-MM-DD.")
            return
        self.details_dict[ID] = Details(ID, date_obj, Description, Amount)
        print(f'Details added successfully (ID: {ID})')
        self.save_details()

    def update_details(self, ID, Date, new_Description, new_Amount):
        if ID in self.details_dict:
            detail_to_update = self.details_dict[ID]
            if Date:
                try:
                    # Convert date string to a datetime.date object
                    detail_to_update.date = datetime.datetime.strptime(Date, '%Y-%m-%d').date()
                except ValueError:
                    print(f"Invalid date format: {Date}. Use YYYY-MM-DD.")
                    return
            if new_Description:
                detail_to_update.description = new_Description
            if new_Amount:
                detail_to_update.amount = new_Amount
            print(f'Details updated successfully (ID: {ID})')
            self.save_details()
        else:
            print(f"(ID: {ID}) not found")

    def delete_details(self, ID):
        if ID in self.details_dict:
            del self.details_dict[ID]
            self.save_details()
            print(f"Detail with ID {ID} deleted successfully")
        else:
            print(f"(ID: {ID}) not found")

    def view(self):
        if not self.details_dict:
            print("No details to display.")
            return
        
        # data in dictionary form
        '''print("Listing details:")
        for detail in self.details_dict.values():
            data = detail.display()
            print(data)'''
        
        #data in data frame form:
        all_data = []
        for detail in self.details_dict.values():
            # Get DataFrame from each detail
            data = detail.display()
            all_data.append(data)
        # Concatenate all the DataFrames together if you have multiple details
        if all_data:
            # Concatenate all data into a single DataFrame
            full_data = pd.concat(all_data, ignore_index=True)
            print(full_data)
        else:
            print("No details found.")

def main():
    manager = DetailsManager()

    parser = argparse.ArgumentParser(prog='expenses-cli')
    parser.add_argument('command', choices=['add', 'update', 'delete', 'view'])
    parser.add_argument('ID', nargs='?', default=None)
    args = parser.parse_args()

    if args.command == 'add':
        ID = input("Enter ID: ")
        Date = input("Enter Date (YYYY-MM-DD): ")
        Description = input("Enter Description: ")
        Amount = input("Enter Amount: ")
        manager.add_details(ID, Date, Description, Amount)

    elif args.command == 'update':
        ID = input("Enter ID to update: ")
        Date = input("Enter new Date (YYYY-MM-DD) or press Enter to skip: ")
        new_Description = input("Enter new Description or press Enter to skip: ")
        new_Amount = input("Enter new Amount or press Enter to skip: ")
        if Date:
            date_obj = datetime.datetime.strptime(Date, '%Y-%m-%d').date()
        else:
            date_obj = None
        manager.update_details(ID, date_obj, new_Description, new_Amount)

    elif args.command == 'delete':
        ID = input("Enter ID to delete: ")
        manager.delete_details(ID)

    elif args.command == 'view':
        manager.view()

'''The main function parses user input, converts the date string to a date object, and correctly updates the data.'''

if __name__ == '__main__':
    main()
