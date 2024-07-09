import csv

def read_data(file_name):
    professions = set()
    min_age = float('inf')
    max_age = float('-inf')

    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            profession = row['job']
            age = int(row['age'])

            # Build set of unique professions
            professions.add(profession.lower())  # case insensitive check

            # Calculate min and max age
            if age < min_age:
                min_age = age
            if age > max_age:
                max_age = age

    return professions, {'min_age': min_age, 'max_age': max_age}

def main():
    file_name = 'bank-data.csv'
    professions, age_limits = read_data(file_name)

    print("Unique professions in the dataset:", professions)
    print("Age limits for eligibility: Min:", age_limits['min_age'], " Max:", age_limits['max_age'])

    while True:
        profession = input("Enter a profession (type 'END' to exit): ").strip().lower()

        if profession == 'end':
            print("Ending program.")
            break

        if profession in professions:
            print(f"Client with profession '{profession}' is eligible for the campaign.")
        else:
            print(f"Client with profession '{profession}' is not eligible for the campaign.")

if __name__ == "__main__":
    main()
