import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_srvs.srv import SetBool, Empty


class DibujarCero(Node):
    def __init__(self):
        super().__init__('dibujar_0')

        self.publicador = self.create_publisher(
            Twist, '/turtle1/cmd_vel', 10
        )

        self.create_service(
            SetBool,
            '/pausar_reanudar_cero',
            self.pausar_reanudar
        )

        self.create_service(
            Empty,
            '/reiniciar_cero',
            self.reiniciar
        )

        self.cliente_reset = self.create_client(Empty, '/reset')

        self.movimientos = [
            (1.0, 0.0, 20),
            (0.0, 1.57, 10),
            (1.0, 0.0, 35),
            (0.0, 1.57, 10),
            (1.0, 0.0, 20),
            (0.0, 1.57, 10),
            (1.0, 0.0, 35),
        ]

        self.paso = 0
        self.contador = 0
        self.pausado = False
        self.esperando_reset = None

        self.create_timer(0.1, self.actualizar)

    def parar(self):
        self.publicador.publish(Twist())

    def actualizar(self):
        if self.esperando_reset is not None:
            if self.esperando_reset.done():
                self.esperando_reset = None
                self.paso = 0
                self.contador = 0
                self.pausado = False
            else:
                self.parar()
            return

        if self.pausado or self.paso >= len(self.movimientos):
            self.parar()
            return

        lineal, angular, duracion = self.movimientos[self.paso]

        velocidad = Twist()
        velocidad.linear.x = lineal
        velocidad.angular.z = angular
        self.publicador.publish(velocidad)

        self.contador += 1

        if self.contador >= duracion:
            self.contador = 0
            self.paso += 1

    def pausar_reanudar(self, solicitud, respuesta):
        self.pausado = solicitud.data

        if self.pausado:
            self.parar()

        respuesta.success = True
        respuesta.message = (
            'Dibujo pausado' if self.pausado
            else 'Dibujo reanudado'
        )
        return respuesta

    def reiniciar(self, solicitud, respuesta):
        self.parar()

        if self.cliente_reset.service_is_ready():
            self.esperando_reset = self.cliente_reset.call_async(
                Empty.Request()
            )
        else:
            self.get_logger().error('El servicio /reset no está disponible')

        return respuesta


def main(args=None):
    rclpy.init(args=args)
    nodo = DibujarCero()

    try:
        rclpy.spin(nodo)
    except KeyboardInterrupt:
        pass
    finally:
        nodo.parar()
        nodo.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
