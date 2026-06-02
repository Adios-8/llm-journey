"""环境检查脚本"""
import sys
import platform

def main():
      # 打印基本信息
      print(f"Python 版本: {sys.version}")
      print(f"操作系统: {platform.system()} {platform.release()}")
      print(f"架构: {platform.architecture()[0]}")

      # 检查依赖包
      pkgs = ["requests", "httpx", "pydantic", "numpy", "pandas", "jupyter"]
      for pkg in pkgs:
          try:
              __import__(pkg)
              print(f"✅ {pkg} 已安装")
          except ImportError:
              print(f"❌ {pkg} 未安装")

if __name__ == "__main__":
      main()