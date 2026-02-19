from PIL import Image
import numpy as np
import os

def adaptar_imagem_para_kmeans(
    caminho_entrada,
    caminho_saida="Mapeamento 3D caverna_RGB.png",
    tamanho_maximo=1024
):
    # Abre imagem
    img = Image.open(caminho_entrada)

    # Converte qualquer formato para RGB (remove alpha e grayscale)
    img = img.convert("RGB")

    # Reduz tamanho se for muito grande
    largura, altura = img.size
    maior_lado = max(largura, altura)

    if maior_lado > tamanho_maximo:
        escala = tamanho_maximo / maior_lado
        nova_largura = int(largura * escala)
        nova_altura = int(altura * escala)
        img = img.resize((nova_largura, nova_altura), Image.LANCZOS)

    # Garante formato uint8
    img_np = np.array(img).astype(np.uint8)

    # Salva imagem
    img_final = Image.fromarray(img_np)
    img_final.save(caminho_saida, format="JPEG", quality=95)

    print("Imagem adaptada com sucesso!")
    print("Novo tamanho:", img_np.shape)
    print("Salva em:", os.path.abspath(caminho_saida))

    return caminho_saida


adaptar_imagem_para_kmeans("Mapeamento 3D caverna.png")
