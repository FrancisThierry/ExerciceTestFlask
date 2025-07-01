# src/business_logic/mendeleev_management.py

from flask import jsonify
from mendeleev import element

class MendeleevManagement:
    def get_element_by_atomic_number(self, atomic_number):
        """
        Retrieve element details by atomic number.
        
        :param atomic_number: The atomic number of the element.
        :return: A dictionary containing element details.
        """
        try:
            elem = element(atomic_number)
            split_element = str(elem).split()
            if len(split_element) < 3:
                return jsonify({"error": "Invalid element data"}), 500
            element_data = {
                "atomic_number": split_element[0],
                "symbol": split_element[1],
                "name": ' '.join(split_element[2:])
            }
            return jsonify(element_data)
        except Exception as e:
            raise ValueError(f"Error retrieving element with atomic number {atomic_number}: {e}")