import csv
from project import Project
import datetime

def main():
    file_path = 'projects.txt'
    projects = read_projects_from_file(file_path)

    while True:
        print("Menu:")
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        option = input(">>> ").lower()

        if option == 'l':
            # Load projects
            file_name = input("Enter filename to load projects from: ")
            projects = read_projects_from_file(file_name)

        elif option == 's':
            # Save projects
            file_name = input("Enter filename to save projects to: ")
            write_projects_to_file(file_name, projects)

        elif option == 'd':
            # Display projects
            display_projects(projects)

        elif option == 'f':
            # Filter projects by date
            filter_date = input("Show projects that start after date (dd/mm/yyyy): ")
            filtered_projects = filter_projects_by_date(projects, filter_date)
            display_projects(filtered_projects)

        elif option == 'a':
            # Add new project
            new_project = add_new_project()
            projects.append(new_project)

        elif option == 'u':
            # Update project
            project_choice = int(input("Project choice: "))
            update_project(projects, project_choice)

        elif option == 'q':
            print("Thank you for using custom-built project management software.")
            break

        else:
            print("Invalid option. Please try again.")

def read_projects_from_file(file_path):
    projects = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)
        for row in reader:
            projects.append(Project(*row))
    return projects


def write_projects_to_file(file_path, projects):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['Name', 'Start Date', 'Priority', 'Estimate', 'Completion'])
        for project in projects:
            writer.writerow([project.name, project.start_date.strftime('%d/%m/%Y'),
                             project.priority, project.estimate, project.completion])


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects, filter_date):
    filter_date = datetime.datetime.strptime(filter_date, "%d/%m/%Y").date()

    print(f"Filter Date: {filter_date}")

    filtered_projects = [project for project in projects if project.start_date > filter_date]

    print("Filtered Projects:")
    for project in filtered_projects:
        print(f"  {project.start_date}")

    return filtered_projects


def add_new_project():
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    estimate = input("Cost estimate: $")
    completion = input("Percent complete: ")

    return Project(name, start_date, priority, estimate, completion)


def update_project(projects, choice):
    if 0 <= choice < len(projects):
        project = projects[choice]

        print(project)
        new_percentage = int(input("New Percentage: "))
        project.completion = new_percentage

        new_priority = input("New Priority: ")
        if new_priority:
            project.priority = int(new_priority)

        print("Project updated successfully.")
    else:
        print("Invalid project choice. Please try again.")

if __name__ == "__main__":
    main()
