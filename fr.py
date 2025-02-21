import cv2
import dlib
import numpy as np
import face_recognition
import pandas as pd
from itertools import product

# Função para carregar e processar a imagem com opções de escala de cinza e filtro bilateral
def load_and_process_image(image_path, use_gray=True, use_bilateral=True):
    # Carrega a imagem original
    img = cv2.imread(image_path)
    processed_img = img.copy()
    
    # Converte a imagem para escala de cinza, se a opção estiver ativada
    if use_gray:
        processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2GRAY)
    elif not use_gray and len(processed_img.shape) == 2:
        # Se estiver em escala de cinza e a opção for desativada, volta para colorido
        processed_img = cv2.cvtColor(processed_img, cv2.COLOR_GRAY2BGR)
    
    # Aplica o filtro bilateral para suavizar a imagem, preservando as bordas
    if use_bilateral:
        processed_img = cv2.bilateralFilter(processed_img, 5, 75, 75)
    
    # Retorna a imagem original e a processada
    return img, processed_img

# Função para alinhar o rosto com base na posição dos olhos
def get_aligned_face(image, shape):
    # Calcula a posição média dos olhos esquerdo e direito
    left_eye = np.mean(shape[36:42], axis=0)
    right_eye = np.mean(shape[42:48], axis=0)
    
    # Calcula a inclinação entre os olhos
    dY = right_eye[1] - left_eye[1]
    dX = right_eye[0] - left_eye[0]
    angle = np.degrees(np.arctan2(dY, dX))
    
    # Calcula o centro entre os olhos para rotação
    eye_center = ((left_eye[0] + right_eye[0]) // 2, (left_eye[1] + right_eye[1]) // 2)
    
    # Gera a matriz de rotação e aplica à imagem
    M = cv2.getRotationMatrix2D(eye_center, angle, 1.0)
    aligned_face = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    
    return aligned_face

# Função principal para comparar duas imagens de rostos
def compare_faces(img1_path, img2_path, use_gray=False, use_bilateral=False, use_landmarks=False):
    # Carrega as imagens originais
    img1_original = cv2.imread(img1_path)
    img2_original = cv2.imread(img2_path)
    
    # Processa as imagens conforme as configurações escolhidas
    _, processed1 = load_and_process_image(img1_path, use_gray, use_bilateral)
    _, processed2 = load_and_process_image(img2_path, use_gray, use_bilateral)
    
    # Inicializa o detector de rostos e o preditor de marcos faciais (landmarks)
    face_detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
    
    # Converte as imagens processadas para RGB (necessário para o face_recognition)
    if len(processed1.shape) == 2:
        detect1 = cv2.cvtColor(processed1, cv2.COLOR_GRAY2RGB)
        detect2 = cv2.cvtColor(processed2, cv2.COLOR_GRAY2RGB)
    else:
        detect1 = cv2.cvtColor(processed1, cv2.COLOR_BGR2RGB)
        detect2 = cv2.cvtColor(processed2, cv2.COLOR_BGR2RGB)
    
    # Detecta os rostos nas duas imagens
    faces1 = face_detector(detect1)
    faces2 = face_detector(detect2)
    
    # Verifica se os rostos foram detectados em ambas as imagens
    if len(faces1) == 0 or len(faces2) == 0:
        return "Faces não detectadas em uma ou ambas as imagens"
    
    # Seleciona o primeiro rosto detectado de cada imagem
    face1 = faces1[0]
    face2 = faces2[0]
    
    # Se a opção de landmarks estiver ativada, alinha os rostos
    if use_landmarks:
        if len(processed1.shape) == 2:
            landmark_img1 = cv2.cvtColor(processed1, cv2.COLOR_GRAY2RGB)
            landmark_img2 = cv2.cvtColor(processed2, cv2.COLOR_GRAY2RGB)
        else:
            landmark_img1 = processed1
            landmark_img2 = processed2
        
        # Obtém os pontos faciais das duas imagens
        shape1 = predictor(landmark_img1, face1)
        shape2 = predictor(landmark_img2, face2)
        shape_np1 = np.array([[p.x, p.y] for p in shape1.parts()])
        shape_np2 = np.array([[p.x, p.y] for p in shape2.parts()])
        
        # Alinha os rostos com base na posição dos olhos
        img1_final = get_aligned_face(img1_original, shape_np1)
        img2_final = get_aligned_face(img2_original, shape_np2)
    else:
        # Se não usar landmarks, mantém as imagens originais
        img1_final = img1_original
        img2_final = img2_original
    
    # Converte as imagens finais para RGB para o reconhecimento facial
    img1_rgb = cv2.cvtColor(img1_final, cv2.COLOR_BGR2RGB)
    img2_rgb = cv2.cvtColor(img2_final, cv2.COLOR_BGR2RGB)
    
    # Extrai os vetores de características faciais das duas imagens
    encoding1 = face_recognition.face_encodings(img1_rgb)
    encoding2 = face_recognition.face_encodings(img2_rgb)
    
    # Verifica se as características foram extraídas com sucesso
    if not encoding1 or not encoding2:
        return "Não foi possível extrair características faciais"
    
    # Calcula a distância entre os vetores faciais
    distance = np.linalg.norm(encoding1[0] - encoding2[0])
    
    # Converte a distância em uma porcentagem de similaridade
    similarity = (1 - min(distance, 1)) * 100
    
    return similarity

# Função para testar diferentes combinações de parâmetros e gerar um DataFrame com os resultados
def run_analysis(img1_path, img2_path):
    # Gera todas as combinações possíveis de parâmetros
    params = list(product(
        [True, False],  # use_gray: com ou sem escala de cinza
        [True, False],  # use_bilateral: com ou sem filtro bilateral
        [True, False]   # use_landmarks: com ou sem alinhamento facial
    ))
    
    results = []  # Lista para armazenar os resultados
    
    # Testa cada combinação de parâmetros
    for use_gray, use_bilateral, use_landmarks in params:
        try:
            # Compara as imagens com os parâmetros atuais
            similarity = compare_faces(
                img1_path, 
                img2_path,
                use_gray=use_gray,
                use_bilateral=use_bilateral,
                use_landmarks=use_landmarks
            )
            
            # Adiciona os resultados à lista
            results.append({
                'Escala de Cinza': use_gray,
                'Filtro Bilateral': use_bilateral,
                'Landmarks': use_landmarks,
                'Similaridade': similarity if isinstance(similarity, (int, float)) else None
            })
        except Exception as e:
            # Em caso de erro, imprime a combinação problemática
            print(f"Erro na combinação: gray={use_gray}, bilateral={use_bilateral}, landmarks={use_landmarks}")
            print(f"Erro: {str(e)}")
    
    # Converte os resultados em um DataFrame do pandas
    df = pd.DataFrame(results)
    return df

# Uso do código: caminhos das imagens e execução da análise
img1_path = 'Img/lowgirl.jpg'  # Caminho da primeira imagem
img2_path = 'Img/girl.jpg'     # Caminho da segunda imagem

# Executa a análise e imprime os resultados
results_df = run_analysis(img1_path, img2_path)
print(results_df.to_string(index=False))