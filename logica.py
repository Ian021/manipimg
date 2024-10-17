import os
import numpy as np
from PIL import Image

def particionar_imagem(caminho_imagem, pasta_destino, tamanho_x, tamanho_y):
    # Carrega a imagem com suporte a transparência (RGBA)
    imagem = Image.open(caminho_imagem).convert('RGBA')
    largura, altura = imagem.size
    
    # Converte para numpy array
    matriz_imagem = np.array(imagem)

    # Calcula o número de partições
    num_particoes_x = largura // tamanho_x
    num_particoes_y = altura // tamanho_y

    contador = 0
    for i in range(num_particoes_y):
        for j in range(num_particoes_x):
            # Define a área da partição
            area = (
                j * tamanho_x, 
                i * tamanho_y, 
                (j + 1) * tamanho_x, 
                (i + 1) * tamanho_y
            )
            particao = imagem.crop(area)
            
            # Converte a partição para NumPy array (com suporte a 4 canais: RGBA)
            matriz_particao = np.array(particao)

            # Verifica o canal alfa (canal 3) para detectar pixels opacos
            # Se todos os pixels tiverem o valor alfa 0, não salva a partição
            canal_alfa = matriz_particao[:, :, 3]  # Canal alfa da imagem (4º canal)

            if np.any(canal_alfa > 0):  # Se algum pixel for opaco (alfa > 0), salva
                caminho_particao = os.path.join(pasta_destino, f'particao_{contador}.png')
                particao.save(caminho_particao)
                contador += 1
