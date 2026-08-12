import Jetson.GPIO as GPIO
import rclpy
from rclpy.node import Node

from std_srvs.srv import SetBool

SPRAYER_PIN = 9

class Sprayer(Node):
    def __init__(self):
        super().__init__('sprayer_node')

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SPRAYER_PIN, GPIO.OUT, initial=GPIO.LOW)

        self.spray_serv = self.create_service(SetBool, 'spray', self.spray)

        self.get_logger().info('Sprayer node started...')

    def spray(self, request: SetBool.Request, response: SetBool.Response):
        try:
            if request.data:
                GPIO.output(SPRAYER_PIN, GPIO.HIGH)
                response.success = True
                response.message = "Sprayer on."
            else:
                GPIO.output(SPRAYER_PIN, GPIO.LOW)
                response.success = True
                response.message = "Sprayer off."
        except Exception as e:
            response.success = False
            response.message = f"Failed to set GPIO: {str(e)}"
            self.get_logger().error(response.message)

        self.get_logger().info(f"State: {response.message}")
            
        return response

    def destroy_node(self):
        GPIO.output(SPRAYER_PIN, GPIO.LOW)
        GPIO.cleanup()
        self.get_logger().info('GPIO cleaned up and node destroyed.')
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = Sprayer()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
