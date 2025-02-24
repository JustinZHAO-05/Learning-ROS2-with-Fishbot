from demo_python_pkg.person_node import PersonNode
import rclpy

class WriterNode(PersonNode):
    def __init__(self, node_name:str, name: str, age: int, book: str) -> None:
        super().__init__(node_name, name, age)
        self.book = book
        self.get_logger().info(f'The book is {self.book}')


def main():
    rclpy.init()
    node = WriterNode('writr_node','Justin',18, 'How to build a robot')
    node.eat('fried ros2')
    rclpy.spin(node)
    rclpy.shutdown()

    
    

