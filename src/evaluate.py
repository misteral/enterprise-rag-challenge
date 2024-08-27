import json
import matplotlib.pyplot as plt
import os

def calculate_correct_answers(source_file: str, result_file: str) -> float:
    """
    Calculate the percentage of correct answers by comparing the result file with the source of truth file.

    Args:
        source_file (str): Path to the source of truth JSON file.
        result_file (str): Path to the result JSON file.

    Returns:
        float: The percentage of correct answers.
    """
    with open(source_file, 'r') as f:
        source_data = json.load(f)

    with open(result_file, 'r') as f:
        result_data = json.load(f)

    correct_count = 0

    for source, result in zip(source_data, result_data):
        if source['answer'] == result['answer']:
            correct_count += 1

    total_questions = len(source_data)
    return (correct_count / total_questions) * 100 if total_questions > 0 else 0.0

def evaluate_all_results(source_file: str, result_files: list[str]):
    """
    Evaluate all result files and create a visual chart of the correct answer percentages.

    Args:
        source_file (str): Path to the source of truth JSON file.
        result_files (list[str]): List of paths to the result JSON files.
    """
    results = {}
    for result_file in result_files:
        percentage = calculate_correct_answers(source_file, result_file)
        system_name = os.path.splitext(os.path.basename(result_file))[0]
        results[system_name] = percentage

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(results.keys(), results.values(), color='skyblue')
    plt.xlabel('System Names')
    plt.ylabel('Percentage of Correct Answers')
    plt.title('Evaluation of Correct Answers Across Different Systems')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def main():
    source_file = 'results/source_of_thruth.json'
    result_files = [
        'results/open_ai_a1.json',
        'results/open_ai_a2.json',
        # Add other result files here
    ]
    evaluate_all_results(source_file, result_files)

if __name__ == "__main__":
    main()
