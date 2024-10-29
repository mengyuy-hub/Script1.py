import os
import re

# Q1: Load the events.txt file and set the output path
output_folder = "d:\\output"
os.makedirs(output_folder, exist_ok=True)  # Create the folder if it does not exist

# Q2: Function to load events
# a) Determine if function needs input parameters (it does not here)
def load_events():
    # b) Create an empty list named events
    events = []
    try:
        # c) Read the file line by line and extract the required data
        with open("d:\\events.txt", "r", encoding="utf-8") as file:
            for line in file:
                # Use regular expression to split the line and filter events before the year 1000
                match = re.match(r"(\d{4})\s*:\s*(.+)", line)
                if match:
                    year = int(match.group(1))
                    if year >= 1000:  # Ignore events before the year 1000
                        description = match.group(2).strip()
                        # Create a tuple with year and description, add it to events list
                        events.append((str(year), description))
    except FileNotFoundError:
        pass  # Ignore error and return an empty event list if the file is not found
    # d) Return the list of tuples, where each item is a tuple for an event
    return events

# Q3: Function to annotate events
# a) Copy the additional_details dictionary into the script
additional_details = {
    "1066": "Normans defeat the English.",
    "1215": "King John of England agrees to it.",
    "1492": "Columbus reaches the New World.",
    "1588": "Major naval victory for England against Spain.",
    "1776": "USA declares independence from Britain.",
    "1789": "Storming of the Bastille in Paris.",
    "1804": "Napoleon establishes the First French Empire.",
    "1859": "Foundational text of evolutionary biology.",
    "1865": "Confederate General Lee surrenders to Union General Grant.",
    "1876": "First successful demonstration of the telephone.",
    "1914": "Caused by assassination of Archduke Franz Ferdinand.",
    "1920": "19th Amendment to the U.S. Constitution ratified.",
    "1939": "Caused by Germany's invasion of Poland.",
    "1963": "Delivered in Washington D.C.",
    "1969": "Neil Armstrong becomes the first human on the Moon.",
    "1989": "Marks end of the Cold War.",
    "2008": "Major banks and financial institutions collapse."
}

# b) Define the annotate_event() function to take an event as an argument
def annotate_event(event):
    year, description = event
    # c) Use the year of the event tuple as a dictionary key to find additional information
    if year in additional_details:
        # If additional detail is found, create a new file and write the description
        full_description = f"{description}\n{additional_details[year]}"
        # Define the output file path
        output_path = os.path.join(output_folder, f"{year}.txt")
        # Write the full description to the file
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(full_description)

# Q4: Call the load_events() function, which returns the events as a list of tuples
if __name__ == "__main__":
    events = load_events()

    # Q5: Iterate over the list of events and call annotate_event() for each event
    for event in events:
        annotate_event(event)
