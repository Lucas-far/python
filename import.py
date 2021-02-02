

"""
Módulo: import.py
Objetivo: mostrar maneiras de fazer importação na linguagem Python
"""

import pyautogui                                    # importação global
import sys as y                                     # importação global apelidada
from math import *                                  # importação global com sintaxe de importação específica
from random import random                           # importação específica
from os import path as p                            # importação específica apelidada
from datetime import datetime, time, timezone       # importações específicas múltiplas
from collections import Counter as ct, deque as dq  # importações específicas múltiplas apelidadas
from typing import (List, Dict, Tuple)              # importações específicas múltiplas em tupla
from shutil import (copy as cy, move as mv)         # importações específicas múltiplas apelidadas em tupla
from _lembretes import pendentes                    # importação modular
from vazio.vazio import vazio                       # importação diretório modular
