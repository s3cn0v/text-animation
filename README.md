# Animation Text

Animación de texto estilo "hacker typing" con efectos de colores en la terminal. El texto se revela letra por letra simulando una decodificación tipo *Matrix* o *cyberpunk*.

![preview](https://img.shields.io/badge/status-active-brightgreen)
![python](https://img.shields.io/badge/python-3.6+-blue)

---

## Demo

```bash
python3 animation-text.py "Hello World!"
````

## Características

* Animación de caracteres ASCII
* Texto animado en color verde brillante
* Cursor oculto durante la animación
* Compatible con Windows, macOS y Linux
* Código limpio, organizado en funciones

## Requisitos

* Python 3.6 o superior
* `colorama` para los colores en terminal

Instálalo con:

```bash
pip install -r requirements.txt
```

## Uso

```bash
python3 animation-text.py "Texto que quieres animar"
```

También puedes hacer el archivo ejecutable agregando:

```bash
chmod +x animation-text.py
./animation-text.py "Hola mundo"
```

## Estructura del proyecto

```
animation-text/
│
├── animation-text.py     # Script principal
├── requirements.txt      # Dependencias de Python
└── README.md             # Este archivo
```

## Ejemplo de salida

```text
H̲e̲l̲l̲o̲ ̲W̲o̲r̲l̲d̲!
```

> *Cada carácter va "barajando" hasta coincidir, con color y animación.*

## Licencia

MIT License © 2025 — \[secnov]
