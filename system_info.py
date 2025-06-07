import sys
import platform
print("="*50)
print(f"操作系统: {platform.system()}")
print(f"架构信息: {platform.machine()}")
print(f"平台详情: {platform.platform()}")
print(f"Python 版本: {sys.version}")
print("="*50)
