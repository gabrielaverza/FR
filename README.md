# Avaliação do Impacto de Técnicas de Pré-Processamento no Reconhecimento Facial em Imagens de Baixa Qualidade
Este projeto avalia o impacto de diferentes técnicas de pré-processamento no reconhecimento facial em imagens de baixa qualidade.

## Instruções de Uso

### Dependências

Para executar este projeto, você precisará das seguintes bibliotecas Python:

- **OpenCV**: Para processamento de imagens.
- **Dlib**: Para detecção de landmarks faciais.
- **face_recognition**: Para reconhecimento facial.
- **numpy**: Para operações matemáticas.
- **pandas**: Para manipulação de dados.

### Instalação das Dependências

Você pode instalar as dependências usando pip:
  ```
pip install requirements.txt
  ```

### Execução do Código

1. **Clonar o Repositório**:
  ```
git clone https://github.com/seu-usuario/reconhecimento-facial.git
  ```

2. **Executar o Script**:
- Coloque as imagens que deseja comparar na pasta `Img/`.
- Edite as variáveis `img1_path` e `img2_path` no arquivo `fr.py` para apontar para as imagens desejadas.
- Execute o script com Python:
  ```
  python fr.py
  ```

3. **Análise dos Resultados**:
- Os resultados serão impressos no terminal, mostrando a similaridade entre as imagens para diferentes configurações de pré-processamento.

### Configurações de Pré-Processamento

O script permite testar diferentes combinações de pré-processamento:

- **Escala de Cinza**: Conversão da imagem para escala de cinza.
- **Filtro Bilateral**: Aplicação de filtro bilateral para suavizar a imagem.
- **Landmarks**: Uso de landmarks faciais para alinhar o rosto.

Essas configurações são aplicadas automaticamente em todas as combinações possíveis.

---

# Evaluating the Impact of Preprocessing Techniques on Face Recognition in Low-Quality Images

This project evaluates the impact of different **preprocessing techniques** on **face recognition** in **low-quality images**.

## 📌 Usage Instructions

### Dependencies

To run this project, you'll need the following Python libraries:

* **OpenCV**: For image processing
* **Dlib**: For facial landmark detection
* **face\_recognition**: For face recognition
* **numpy**: For mathematical operations
* **pandas**: For data manipulation

### Installing Dependencies

You can install all dependencies using pip:

```bash
pip install -r requirements.txt
```

### Running the Code

1. **Clone the Repository**:

```bash
git clone https://github.com/your-username/face-recognition.git
```

2. **Run the Script**:

* Place the images you want to compare in the `Img/` folder.
* Edit the `img1_path` and `img2_path` variables in the `fr.py` file to point to the desired images.
* Execute the script using Python:

```bash
python fr.py
```

3. **Analyze the Results**:

* The results will be printed in the terminal, showing the similarity between images for different preprocessing configurations.

### Preprocessing Configurations

The script allows testing various combinations of preprocessing techniques:

* **Grayscale**: Converts the image to grayscale
* **Bilateral Filter**: Applies a bilateral filter to smooth the image
* **Landmarks**: Uses facial landmarks to align the face

These configurations are automatically applied in all possible combinations.

