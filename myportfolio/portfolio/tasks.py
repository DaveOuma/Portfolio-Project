from celery import shared_task
from datetime import datetime
from time import sleep
import logging

@shared_task(bind=True)
def execute_calculator(self):
    """
    Asynchronous task to execute a basic calculator.
    """
    try:
        result = "4 + 4 = 8\n5 - 3 = 2\n"  # Example output from a basic calculator
        return result
    except Exception as e:
        return f"An error occurred: {e}"

def print_current_time():
    """
    Function to print and return the current time.
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current time: {current_time}")
    return current_time

logger = logging.getLogger(__name__)
@shared_task(bind=True)
def long_running_task(self, param1):
    logger.info(f'Starting task with param1: {param1}')
    sleep(10)  # Simulating a long-running task
    result = f'Task completed with {param1}'
    logger.info(f'Task result: {result}')
    return result