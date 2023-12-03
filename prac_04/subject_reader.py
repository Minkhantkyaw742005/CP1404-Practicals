"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    display_subject_details(data)




def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data_list = []
    for line in input_file:
        line = line.strip().split(',')
        data_list.append(line)
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        # line = line.strip()  # Remove the \n
        # parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        # parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
    return data_list
    input_file.close()

def display_subject_details(data):
    for number in range(3):
        subject = data[number]
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[-1]} students")

main()