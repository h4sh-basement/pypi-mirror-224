# DetectaFace - Detecção de Rostos em Imagens e Vídeos usando OpenCV

Este é um pacote Python que permite a detecção de rostos em imagens individuais, em um conjunto de imagens dentro de uma pasta e a captura de rostos em tempo real usando a webcam, utilizando a biblioteca OpenCV.

## Funcionalidades

O pacote `DetectaFace` oferece as seguintes funcionalidades:

1. **Detectar Rostos em Imagens Individuais:** Carregue uma imagem e identifique rostos presentes nela.

2. **Detectar Rostos em um Conjunto de Imagens:** Processa várias imagens em uma pasta e detecta os rostos em cada uma delas.

3. **Capturar Rostos em Tempo Real pela Webcam:** Capture rostos em tempo real utilizando a webcam do seu dispositivo.

## Requisitos

Antes de começar, certifique-se de ter o OpenCV instalado em seu ambiente Python. Se ainda não tiver, instale-o com o seguinte comando:

```bash
pip install opencv-python
```

## Uso

A classe `DetectaFace` oferece um conjunto de métodos para diferentes tipos de detecção de rostos. Abaixo estão exemplos de como usar cada um deles:

### 1. Detectar Rostos em Imagens Individuais

```python
from detecta_face import DetectaFace
import cv2 as cv

# Carregue uma imagem
imagem = cv.imread('caminho_para_imagem.jpg')

# Crie uma instância da classe DetectaFace
detector = DetectaFace(imagem)

# Carregue o classificador de rostos
face_cascade = detector.load_face_cascade()

# Detecte rostos na imagem
imagem_resultado, num_faces = detector.detect_faces(imagem, face_cascade)

# Exiba a quantidade de rostos detectados
print('Quantidade de rostos:', num_faces)

# Exiba a imagem com retângulos ao redor dos rostos
cv.imshow('Rostos Detectados', imagem_resultado)
cv.waitKey(0)
cv.destroyAllWindows()

```

### 2. Detectar Rostos em um Conjunto de Imagens

```python
# Importar as bibliotecas necessárias
from detecta_face import DetectaFace
import os

# Crie uma instância da classe DetectaFace
detector = DetectaFace()

# Carregue o classificador de rostos
face_cascade = detector.load_face_cascade()

# Especifique o caminho para a pasta de imagens
caminho_pasta = 'caminho_para_pasta_de_imagens'

# Chame o método para processar imagens na pasta
detector.processar_pasta_imagens(caminho_pasta, face_cascade)
```

### 3. Capturar Rostos em Tempo Real pela Webcam

```python
# Importar as bibliotecas necessárias
from detecta_face import DetectaFace

# Crie uma instância da classe DetectaFace
detector = DetectaFace()

# Capture rostos em tempo real
detector.video_capture_face()
```
