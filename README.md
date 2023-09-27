# CaritasMTYAPI

API for an app developed for "Cáritas de Monterrey" as a school project.

### Instructions

### 1- Clonar el repo y entrar en el
```{bash}
$ git clone https://github.com/AdrianM0Hdz/CaritasMTYAPI.git
$ cd CaritasMTYAPI
```

### 2- Crear ambiente virtual (solo una vez por computadora)
```{bash}
python -m venv env
```

### 3- Activar ambiente virtual (cada vez que se desee correr el código)
#### Windows Command Prompt
```{bash}
.\env\Scripts\activate
```

#### MACOS and Linux
```{bash}
source env/bin/activate
```

#### Windows Powershell
```{bash}
.\env/Scripts/Activate.ps1
```

### 4- Instalar dependencias
(solo una vez inicialmente y despues solo si hay un cambio en el archivo requirements.txt)
```{bash}
pip install -r requirements.txt
```

Si estas usando Apple Silicon tienes que borrar e instalar pyodbc de esta manera:
```{bash}
pip uninstall pyodbc && pip install --no-binary :all: pyodbc
```

### 5- Correr el servidor
```{bash}
python app.py
```

### 6- Salir del ambiente virtual
```{bash}
deactivate
```
