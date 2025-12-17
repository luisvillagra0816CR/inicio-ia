# Como imprimir la fecha actual en formato bonito

```python
import datetime

fecha_actual = datetime.now()

print( fecha_actual.strftime("%d/%m/%Y %H:%M:%S") )

```