
def analyze_log(file_path):
    counts = {
        "ERROR": 0,
        "WARNING": 0,
        "INFO": 0
    }

# We check every line in the log file and we update the right counter
    try:
        with open(file_path, "r") as file:
            for line in file:
                if "ERROR" in line:
                    counts["ERROR"] += 1
                elif "WARNING" in line:
                    counts["WARNING"] += 1
                elif "INFO" in line:
                    counts["INFO"] += 1

        return counts

    except FileNotFoundError:
        print("Log file not found.")
        return None

#main prints the number of Errors, Warnings and Info
def main():
    file_path = "sample.log"
    result = analyze_log(file_path)

    if result:
        print("Log Analysis Results:")
        for key, value in result.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()