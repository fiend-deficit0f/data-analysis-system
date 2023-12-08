# main_program.py

from data_processing import preprocess_data, analyze_data
from visualization import plot_data

def main():
    # Generate sample data
    raw_data = [1, 2, 3, 4, 5]

    # Preprocess data
    processed_data = preprocess_data(raw_data)

    # Analyze data
    result = analyze_data(processed_data)
    print(result)

    # Visualize data
    plot_data(processed_data)

if __name__ == "__main__":
    main()
