# Proyecto PRII 3 — Sprint 1

## Grupo 05: dibujo del 0

Este repositorio contiene mi parte del Sprint 1 del proyecto de Robots
Inteligentes. La aplicación utiliza ROS 2 y turtlesim para mover una tortuga
de forma autónoma y dibujar el número 0, que forma parte del identificador
G05.

## Entorno utilizado

- Ubuntu: Ubuntu 24.04.5 LTS
- ROS 2 Jazzy Jalisco.
- Python 3.
- Shell utilizada: zsh.

> El enunciado original de la práctica menciona ROS 2 Humble. Esta versión
> se ha desarrollado y probado con ROS 2 Jazzy.

## Descargar el repositorio

```zsh
cd ~/Documents
git clone [https://github.com/IvanEscuriola/sprint1_g05_prii3_ws.git] (https://github.com/IvanEscuriola/sprint1_g05_prii3_ws.git) proy3
cd proy3
```

## Dependencias

Cargar el entorno de ROS 2 Jazzy:

```zsh
source /opt/ros/jazzy/setup.zsh
```

Si turtlesim no está instalado:

```zsh
sudo apt update
sudo apt install ros-jazzy-turtlesim
```

## Estructura principal

```text
proy3/
├── README.md
├── .gitignore
└── src/
    └── g05_prii3_turtlesim/
        ├── package.xml
        ├── setup.py
        ├── resource/
        ├── launch/
        │   └── dibujar_cero.launch.py
        └── g05_prii3_turtlesim/
            ├── __init__.py
            └── dibujar_0.py
```

## Compilación

Desde la raíz del workspace:

```zsh
cd ~/Documents/proy3
source /opt/ros/jazzy/setup.zsh
colcon build --symlink-install
source install/setup.zsh
```

## Ejecución

Ejecutar el simulador y el nodo mediante el archivo launch:

```zsh
source /opt/ros/jazzy/setup.zsh
source ~/Documents/proy3/install/setup.zsh

ros2 launch g05_prii3_turtlesim dibujar_cero.launch.py
```

El nodo mueve la tortuga de forma autónoma para dibujar el número 0.

## Servicios

Los servicios se ejecutan desde otra terminal.

### Pausar el dibujo

```zsh
source /opt/ros/jazzy/setup.zsh
source ~/Documents/proy3/install/setup.zsh

ros2 service call /pausar_reanudar_cero std_srvs/srv/SetBool "{data: true}"
```

### Reanudar el dibujo

```zsh
ros2 service call /pausar_reanudar_cero std_srvs/srv/SetBool "{data: false}"
```

### Reiniciar el dibujo

```zsh
ros2 service call /reiniciar_cero std_srvs/srv/Empty "{}"
```

## Comprobar el nodo y los servicios

```zsh
ros2 node list
ros2 topic list
ros2 service list
```

Para comprobar la información del nodo:

```zsh
ros2 node info /dibujar_0
```

## Git

La rama principal del repositorio es `main`.

```zsh
git status
git log --oneline
git branch
```

## Autor

Ivan — Grupo 05
