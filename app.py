from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os
import sys

model_file = 'pipeline_xgb_final.pkl'
Intervention_Threshold = 0.45

try: 
    if '__file__' not in locals():
        model_path = model_file
    else:
        model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), model_file)
    model = joblib.load(model_file)
    print("Modelo cargado.")
except FileNotFoundError:
    print(f"No se encontro el archivo del modelo{model_file}")
    exit(1)
app = Flask(__name__)

@app.route('/predict', methods = ['POST'])
def predict():
    """
    Endpoint para recibir datos de un nuevo estudiante y predecir
    si completará o no el curso, aplicando el umbral de intervención.
    """
    try: 
        json_data = request.get_json(force = True)
        input_data = pd.DataFrame([json_data])
        prediction_proba = model.predict_proba(input_data)[:,1]
        
        prediction_class = int(prediction_proba[0] >= Intervention_Threshold)
        if prediction_class == 1:
            status = 'Completed'
            alert_message = 'No se requiere intervencion inmediata.'
        else:
            status = 'Incomplete'
            alert_message = 'Estudiante en alto riesgo de no completar el curso.'
        response = {
            'predicted_completion_status': status,
            'probability_of_completion': round(prediction_proba[0], 4),
            'intervention_threshold_used':Intervention_Threshold,
            'intervention_recommendation': alert_message
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e), 'message':'Asegurase que todos los campos requiridos esten presentes.'}),400

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')
    