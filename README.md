# Simulación de crecimiento bacteriano en microgravedad

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Descripción

Este proyecto implementa un **autómata celular bidimensional** para simular el crecimiento de bacterias (ej. *Bacillus cereus* y *Escherichia coli*) bajo dos condiciones gravitacionales:

- **Gravedad normal** (1 g)
- **Microgravedad** (simulada)

El modelo está basado en el seminario *Microgravedad y Radiación Espacial: Su Impacto en la Biología Cuántica de las Bacterias* (Avendaño, 2025) y reproduce cualitativamente los efectos observados en experimentos de la ISS: mayor tasa de división, formación de biopelículas y tolerancia a la aglomeración celular en microgravedad.

## Base científica

- **Microgravedad** → aumenta la probabilidad de división (`P_div`), reduce la inhibición espacial (`N0`) y favorece la agregación (`P_cluster`).
- **Sustrato** → difusión browniana y consumo local por células en crecimiento.
- **Reglas celulares**:
  - `0` = vacío
  - `1` = célula en división
  - `2` = célula en crecimiento
- **Inhibición espacial**: una célula en división pasa a crecimiento si el número de vecinos supera el umbral `N0`.

## Estructura del proyecto
microgravity_bacteria_sim/
├── src/
│ ├── init.py
│ ├── model.py # Lógica del autómata
│ └── visualization.py # Visualización y guardado de frames
├── tests/ # Pruebas unitarias (pendientes)
├── data/ # Datos generados (opcional)
├── runs/ # Outputs de simulación
├── output_simulacion/ # Imágenes guardadas (si se activa)
├── requirements.txt
├── .gitignore
├── LICENSE
├── README.md
└── run.py # Script principal


## Instalación

### Requisitos

- Python 3.12 o superior, en caso de presentar conflictos de versiones intente usar la version 3.12 de python
- pip

### Pasos

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/savendanobo-ui/microgravity_bacteria_sim.git
   cd microgravity_bacteria_sim

2. Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows

3. Instalar dependencias
pip install -r requirements.txt

Uso
python run.py --steps 300 --size 150 --microgravity --save-interval 50

Puede alterar los diferentes argumentos, use python run.py --help para ver los argumentos disponibles

Argumentos disponibles
--microgravity	Activa parámetros de microgravedad	
--steps STEPS	Número de pasos de simulación	
--size SIZE	Tamaño del grid (SIZE x SIZE)	
--save SAVE	Guardar último frame como PNG	
--interval INTERVAL	Milisegundos entre pasos de animación	
--no-metrics	Oculta la gráfica de evolución	
--seed SEED	Semilla para reproducibilidad	
--save-interval N	Guardar imagen cada N pasos (0 = no guardar)	
--output-dir DIR	Carpeta destino para imágenes guardadas	

Limitaciones conocidas:
El sustrato se difunde aleatoriamente (sin gradientes de concenración ni quimiotaxis)
La visualización puede volverse lenta para grids de mas de 200x200

Si utilizas este codigo, por favor referencia este repositorio
https://github.com/savendanobo-ui/microgravity_bacteria_sim

Distribuido bajo licencia MIT. Consulta el archivo LICENSE para mas información.

Contacto
Samir Steven Avendaño Bolaños - savendanobo@unal.edu.co