

"""
Módulo: open.py
Objetivo: abrir um módulo no OS, podendo ser áudio, áudio/vídeo, documentos, etc...
Observação:
    - precisa-se mudar para a rota onde está o arquivo, sem passar o [ nome do arquivo.formato ]
    - após ter mudado para a rota desejada, usa-se o método [ open(nome do arquivo.formato) ]
"""

from os import chdir
from webbrowser import open

# Os dados podem ser todos abertos de uma vez, ou um por vez
chdir('/media/lucas/OS/Users/Lucas/Downloads/main/type_sound/')
open('unknown.mp3')                                      # acessando áudio
chdir('/media/lucas/OS/Users/Lucas/Downloads/main/type_media')
open('refrigerator_gone_edited.mp4')                     # acessando vídeo
chdir('/media/lucas/OS/Users/Lucas/Downloads/main/studies')
open('curso_python_basico_ao_avancado_certificado.pdf')  # acessando documento
