import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/fishros/document/GitHub/Learning-ROS2-with-Fishbot/chapt3/topic_practice_ws/src/install/status_publisher'
