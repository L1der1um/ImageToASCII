#pip install ascii-magic
#pip3 install ascii-magic

#SCRIPT PARA PEGAR IMAGEM E GERAR UM ASCII (REPRESENTAÇÃO DA IMAGEM EM CARACTERES)

from ascii_magic import AsciiArt

def ascii(path):
    art=AsciiArt.from_image(path)
    art.to_terminal()

#DO AMBIENTE LOCAL PEGAR UMA IMAGEM CHAMADA CAP.PNG
ascii("cap.png")