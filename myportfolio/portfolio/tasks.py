from celery import shared_task
import subprocess
from django.utils import timezone

@shared_task
def execute_calculator():
    #Executing the c calculator program
    try:
        result = subprocess.run(['c_programs/calculator.exe'], capture_output=True, text=True, timeout=30)
        output = result.stdout
        return output
    except subprocess.TimeoutExpired:
        return "Execution timed out. Please try again later."
    except Exception as e:
        return f"An error ocurred: {e}"

def print_current_time():
    current_time = timezone.now()
    print(f"current time: {current_time}")