## Requisitos
desde la terminal bash utilizar:

pip install -r requirements.txt

> Se uso Python 3.11.x(probado con la version 3.11.9)

## Cómo ejecutar la app
en la terminal:
`streamlit run app_streamlit.py`

## Interfaz gráfica
- Permite **cargar una imagen local**.
- Clasifica automáticamente la imagen en una de las siguientes clases:
  - **Fresh** (fresca)
  - **Stale** (en descomposición)
- Muestra:
  - La imagen cargada
  - La **probabilidad de predicción**
  - El **resultado** de la clasificación
- Permite elegir entre los dos modelos disponibles:
  - `MobileNetV2`
  - `CNN personalizada`

## Modelos
**Ambos modelos deben de descargarse desde el archivo `Prediccion_frutas_verduras.ipynb` al hacer el entrenamiento**
**ya que estos pesaban mas de lo establecido por GitHub**
