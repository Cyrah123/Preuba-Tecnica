# Preuba-Tecnica
Preuba Tecnica para BCN


Este proyecyo implementa un Sistema de Alerta para instituciones eucativas utilizando Machine Learning. El Objectivo es predecir la probabilidad de que en estudiante conplete un curso y basandose en un umbral de riesgo.

Objetivo Principal es para construir un modelo de clasificacion binario que prediga:
- Completed = 1, significando que el estudiante completara el curso
- Completed = 0 , riesgo de no completar el curso.

Componentes Principales
1. Modelado ML - scikit-learn, XGBoost fueron utilisados por el desarollo, entrenamiento y evaluacion de modelos de clasificacion.
2. Preprocesamiento - pipeline y ColumnTransformer fueron utlisados, manejando los datos faltantes y escalando variables numericas.
3. Persistencia - joblib fue usado para la serializacion del modelo entrenado para su uso en producion.


Instalacion y Ejecucion
1. Clonar el repositorio
git clone https://github.com/usuario/course-completion-prediction.git
cd course-completion-prediction

2. Instalar dependencias
pip install -r requirements.txt

3. Ejecutar el notebook
jupyter notebook

4. Ejecutar la API
python app.py


Conclusion
El proyecto es un Sistema de Alerta Temprana que emplea un modelo de aprendizaje automático (Machine Learning) entrenado con un pipeline sólida para anticipar la posibilidad de que un alumno termine con éxito un curso. La decisión técnica fundamental fue implementar este modelo serializado a través de una API RESTful creada con Flask, lo cual posibilita la integración en tiempo real con sistemas externos. El aspecto fundamental de la solución es que la API no solamente devuelve una probabilidad, sino que también establece un umbral de intervención específico para convertir el dato estadístico en una sugerencia de acción directa y ejecutable para los educadores, designando a los alumnos con alto riesgo como "incompletos".
