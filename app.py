import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the pre-trapython.ined model from a pickle file
with open('fuel.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_text = request.form.get('t1')
        
        if not input_text or not input_text.replace('.', '', 1).isdigit():
            return render_template('result.html', prediction="Invalid input. Please enter a numeric value.")
        
        input_data = [float(input_text)]  

        prediction = model.predict([input_data])[0] 

        return render_template('result.html', prediction=f"The predicted output is: {prediction}")

    except Exception as e:
       
        return render_template('result.html', prediction=f"Error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
