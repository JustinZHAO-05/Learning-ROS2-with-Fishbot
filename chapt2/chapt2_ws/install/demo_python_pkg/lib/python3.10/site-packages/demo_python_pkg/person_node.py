import rclpy
from rclpy.node import Node

class PersonNode(Node):
    def __init__(self,node_name:str, name:str, age:int) -> None:
        super().__init__(node_name)
        self.age = age
        self.name = name

    def eat(self, food_name:str):
        self.get_logger().info(f'My name is {self.name}.      I\'m {self.age} years old.         I\'m eating {food_name}.')

def main():
    rclpy.init()
    node=PersonNode('person_node','Justin',20)
    node.eat('ros2')
    rclpy.spin(node)
    rclpy.shutdown()


