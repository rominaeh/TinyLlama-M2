import platform
import psutil
import subprocess

def get_hardware_info():
    system = platform.system()
    machine = platform.machine()
    cpu_arch = platform.processor()
    cpu_cores_physical = psutil.cpu_count(logical=False)
    cpu_cores_logical = psutil.cpu_count()
    ram_gb = round(psutil.virtual_memory().total / (1024 ** 3))

    # Get actual Apple Silicon model (M1/M2) on macOS
    try:
        cpu_model = subprocess.check_output(
            ["sysctl", "-n", "machdep.cpu.brand_string"]
        ).decode().strip()
    except Exception:
        cpu_model = "Unknown"

    print("=== Hardware Info ===")
    print(f"System: {system}")
    print(f"Machine: {machine}")
    print(f"CPU Architecture: {cpu_arch}")
    print(f"CPU Model: {cpu_model}")
    print(f"CPU Cores: {cpu_cores_physical} physical, {cpu_cores_logical} logical")
    print(f"RAM: {ram_gb} GB")
    print("=====================")

if __name__ == "__main__":
    get_hardware_info()
