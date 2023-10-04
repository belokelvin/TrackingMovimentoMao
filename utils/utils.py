# Importando as bibliotecas necessárias
from mediapipe.python.solutions.drawing_utils import _normalized_to_pixel_coordinates
import cv2

# Esta função mapeia os índices das landmarks da mão para as coordenadas em pixels na imagem.
# Ela recebe uma imagem, resultados das landmarks da mão detectadas e dois limiares (thresholds)
# para determinar se uma landmark é visível e presente. Se uma landmark não atender aos critérios,
# ela não será incluída no resultado.
def get_idx_to_coordinates(image, results, VISIBILITY_THRESHOLD=0.5, PRESENCE_THRESHOLD=0.5):
    # Um dicionário para armazenar os índices das landmarks e suas coordenadas correspondentes.
    idx_to_coordinates = {}
    
    # Obtendo as dimensões da imagem de entrada.
    image_rows, image_cols, _ = image.shape
    
    try:
        # Iterando sobre todas as landmarks detectadas na primeira mão (multi_hand_landmarks[0]).
        for idx, landmark in enumerate(results.multi_hand_landmarks[0].landmark):
            # Verificando se a landmark possui o atributo de visibilidade e se a visibilidade
            # é maior que o limite especificado, ou se a landmark possui o atributo de presença
            # e a presença é maior que o limite especificado.
            if ((landmark.HasField('visibility') and
                 landmark.visibility < VISIBILITY_THRESHOLD) or
                    (landmark.HasField('presence') and
                     landmark.presence < PRESENCE_THRESHOLD)):
                # Se a landmark não atender aos critérios, continue para a próxima iteração.
                continue
            
            # Convertendo as coordenadas normalizadas para coordenadas em pixels usando a função
            # _normalized_to_pixel_coordinates.
            landmark_px = _normalized_to_pixel_coordinates(landmark.x, landmark.y,
                                                           image_cols, image_rows)
            
            # Verificando se as coordenadas foram obtidas com sucesso.
            if landmark_px:
                # Armazenando o índice da landmark e suas coordenadas no dicionário.
                idx_to_coordinates[idx] = landmark_px
    except:
        pass
    
    # Retornando o dicionário com os índices das landmarks e suas coordenadas em pixels.
    return idx_to_coordinates

# Esta função redimensiona um quadro de imagem para uma porcentagem específica do tamanho original.
def rescale_frame(frame, percent=75):
    # Calculando as novas dimensões com base na porcentagem especificada.
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)
    
    # Redimensionando o quadro usando a função cv2.resize.
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
