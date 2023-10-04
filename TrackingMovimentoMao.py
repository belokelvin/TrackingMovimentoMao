
#importação 
import numpy as np
import cv2
from collections import deque
import mediapipe as mp
from utils.utils import get_idx_to_coordinates, rescale_frame

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

#módulos específicos da MediaPipe
def main():
    hands = mp_hands.Hands(
        min_detection_confidence=0.7, min_tracking_confidence=0.7)
    
    #objeto Hands é criado com configurações específicas, incluindo limites de confiança para detecção e rastreamento de mãos.
    hand_landmark_drawing_spec = mp_drawing.DrawingSpec(thickness=5, circle_radius=5)
    #objetos DrawingSpec especificam como as landmarks das mãos e as conexões entre elas devem ser desenhadas no vídeo.
    hand_connection_drawing_spec = mp_drawing.DrawingSpec(thickness=10, circle_radius=10)
    
    #captura de vídeo da webcam (câmera número 0)
    cap = cv2.VideoCapture(2)
    pts = deque(maxlen=64)
    
    while cap.isOpened():
        idx_to_coordinates = {} #armazenar as coordenadas das landmarks das mãos.
        ret, image = cap.read() # imagem é capturada a partir da webcam.
        
        #A imagem é invertida horizontalmente e convertida para o espaço de cores RGB
        image = cv2.flip(image, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results_hand = hands.process(image) #A imagem é passada para o objeto hands
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        #Verifica se pelo menos uma mão foi detectada na imagem.
        if results_hand.multi_hand_landmarks:
            # as landmarks das mãos são desenhadas na imagem usando as configurações especificadas nos objetos
            # hand_landmark_drawing_spec e hand_connection_drawing_spec. 
            # As conexões entre as landmarks também são desenhadas.
            for hand_landmarks in results_hand.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=hand_landmarks,
                    connections=mp_hands.HAND_CONNECTIONS,
                    landmark_drawing_spec=hand_landmark_drawing_spec,
                    connection_drawing_spec=hand_connection_drawing_spec)
                #get_idx_to_coordinates é uma função que recebe a imagem e os resultados da detecção das mãos e 
                # retorna um dicionário que mapeia índices de landmarks para suas coordenadas.
                idx_to_coordinates = get_idx_to_coordinates(image, results_hand)
                
        #Verifica se o índice 8 (dedo indicador) está presente no dicionário de coordenadas.
        if 8 in idx_to_coordinates:
            pts.appendleft(idx_to_coordinates[8])  # Index Finger
        else:
            pts.clear()
        #loop percorre os pontos armazenados na fila pts e desenha linhas para acompanhar o movimento do dedo indicador. 
        for i in range(1, len(pts)):
            if pts[i - 1] is None or pts[i] is None:
                continue
            thick = int(np.sqrt(len(pts) / float(i + 1)) * 4.5)
            cv2.line(image, pts[i - 1], pts[i], (0, 255, 0), thick)
        
        #A imagem é redimensionada e exibida em uma janela chamada "Res".
        cv2.imshow("Res", rescale_frame(image, percent=30))
        
        #Altere o valor abaixo para controlar a quantidade de frames por exibição
        if cv2.waitKey(60) & 0xFF == 40:  # Por exemplo, 30 milissegundos por frame
            break
    hands.close()
    cap.release()
if __name__ == '__main__':
    main()






