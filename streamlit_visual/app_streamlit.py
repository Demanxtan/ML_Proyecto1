import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Mapa de clases
class_names = ['Fresh', 'Stale']

# Título de la aplicación
st.title(" Clasificador de Frutas y Verduras")
st.subheader("Selecciona el modelo y sube una imagen para predecir si está fresca o podrida")

# Selector de modelo
modelo_opcion = st.selectbox("Selecciona el modelo de clasificación:", ["MobileNetV2", "CNN Personalizada"])

# Cargar el modelo seleccionado
@st.cache_resource
def cargar_modelo(nombre):
    if nombre == "MobileNetV2":
        return tf.keras.models.load_model("modelo_fresh_vs_stale_mobilenet.h5")
    else:
        return tf.keras.models.load_model("modelo_fresh_vs_stale_cnn.h5")

modelo = cargar_modelo(modelo_opcion)

# Subir imagen
archivo = st.file_uploader(" Sube una imagen (JPG, PNG)", type=["jpg", "jpeg", "png"])

if archivo is not None:
    imagen = Image.open(archivo).convert("RGB")
    st.image(imagen, caption=" Imagen cargada", use_column_width=True)

    # Preprocesamiento
    img = imagen.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predicción
    pred_prob = modelo.predict(img_array)[0][0]
    pred_clase = 1 if pred_prob > 0.5 else 0
    confianza = pred_prob if pred_clase == 1 else 1 - pred_prob

    # Mostrar resultado
    st.markdown(f"###  Resultado: **{class_names[pred_clase]}**")
    st.markdown(f" Precisión estimada: `{confianza*100:.2f}%`")
