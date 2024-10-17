import os
import numpy as np
from PIL import Image

def particionar_imagem(caminho_imagem, pasta_destino, tamanho_x, tamanho_y):
    # Carrega a imagem
    imagem = Image.open(caminho_imagem)
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
            
            # Salva a partição
            caminho_particao = os.path.join(pasta_destino, f'particao_{contador}.png')
            particao.save(caminho_particao)
            contador += 1
