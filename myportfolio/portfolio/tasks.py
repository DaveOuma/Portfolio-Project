from celery import shared_task
import subprocess
from datetime import datetime

@shared_task(bind=True)
def execute_calculator(self):
    #Executing the c calculator program
    try:
        result = subprocess.run(['c_programs/calculator.exe'], capture_output=True, text=True, timeout=10)
        output = result.stdout
        return output
    except subprocess.TimeoutExpired:
        return "Execution timed out. Please try again later."
    except Exception as e:
        return f"An error ocurred: {e}"

def print_current_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current time: {current_time}")
    return current_time