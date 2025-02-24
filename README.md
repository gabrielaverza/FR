# Reconhecimento Facial em Imagens de Baixa Qualidade
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

3. **Executar o Script**:
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
