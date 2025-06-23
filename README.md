## Dataset

-  Nombre: [`Fresh and Stale Images of Fruits and Vegetables`](https://www.kaggle.com/datasets/raghavrpotdar/fresh-and-stale-images-of-fruits-and-vegetables)
- Contiene imágenes en carpetas separadas por clase, como:
  - `fresh_apple`, `stale_banana`, y otros tipos de frutas y verduras tanto frescas como en descomposición.

## Modelos implementados

1. **MobileNetV2**  
   - Transfer Learning usando pesos preentrenados.
   - Congelación parcial de capas.
   - Ajustado para clasificación binaria.
2. **CNN personalizada**
   - Arquitectura creada desde cero.
   - Menor cantidad de parámetros.
   - Entrenada completamente sobre el dataset original.
Ambos modelos fueron **comparados en términos de precisión, arquitectura y desempeño**.

## Descarga de los modelos

el modelo MobileNetv2 y del CNN se puede obtener al hacer correr el archivo 'prediccion_frutas_verduras',
dentro del archivo poder guardarlos una vez hecho el entrenamiento e importarlos en el `steamlit`.

## Recomendacion de hacerlos correr por Jupyter Notebooks o Google Colab, nosotros utilizamos este ultimo mencionado.
