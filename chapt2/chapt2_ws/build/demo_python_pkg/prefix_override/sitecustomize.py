import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/fishros/文档/GitHub/Learning-ROS2-with-Fishbot/chapt2/chapt2_ws/install/demo_python_pkg'
