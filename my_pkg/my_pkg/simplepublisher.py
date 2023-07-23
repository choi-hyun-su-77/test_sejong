from typing import Iterator
import rclpy
from rclpy.node import Node
from rclpy.publisher import Publisher
from std_msgs.msg import String

def test():
    print('test')

class Sim_pub(Node):
    def __init__(self):
        super().__init__('simple_mpub')
        self.pub = self.create_publisher(String, 'message',10)
        self.create_timer(1,self.publishers)

    def publishers(self):
        msg = String()
        msg.data = 'hellow'
        self.pub.publish(msg)


def main():
    rclpy.init()
    node = Sim_pub()
    #node.create_timer(1,test)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('keyboard interrept!!')
    finally:
        node.destroy_node
        rclpy.shutdown()

if __name__ == '__main__':
    main()
