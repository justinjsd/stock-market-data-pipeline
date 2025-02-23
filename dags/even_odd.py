from airflow.decorators import dag, task
from datetime import datetime
import random

# Define the DAG using the TaskFlow API
@dag(
    dag_id="random_number_checker_taskflow",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    description="A simple DAG to generate and check random numbers using TaskFlow API",
)
def random_number_checker():
    
    # Task 1: Generate a random number
    @task
    def generate_random_number():
        number = random.randint(1, 100)
        print(f"Generated random number: {number}")
        return number  # Return the value directly

    # Task 2: Check if the number is even or odd
    @task
    def check_even_odd(number: int):
        result = "even" if number % 2 == 0 else "odd"
        print(f"The number {number} is {result}.")

    # Define task dependencies
    check_even_odd(generate_random_number())

# Instantiate the DAG
random_number_checker()