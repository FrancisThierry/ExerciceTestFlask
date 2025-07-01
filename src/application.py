from flask import Flask, jsonify
from src.business_logic.mendeleev_management import MendeleevManagement

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/element/<int:atomic_number>', methods=['GET'])
def get_element_by_atomic_number(atomic_number):
    try:
        mm = MendeleevManagement()
        element = mm.get_element_by_atomic_number(atomic_number)
        print(f"Retrieved element: {element}")
        #1 H Hydrogen returning element details
        # Assuming element has attributes: number, element symbol, name
        # turn 1 H Hydrogen into a JSON response by splitting the string
        # and returning a dictionary with the relevant information
        
        
        return element, 200
    except Exception as e:  
        app.logger.error(f"An error occurred: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
