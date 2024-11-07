from project import Project
import datetime
from operator import attrgetter


def main():
    filename = 'projects.txt'
    projects = []
    display_menu()
    choice = get_choice()
    while choice != "Q":
        if choice == "L":
            projects = load_projects()
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_project(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        display_menu()
        choice = get_choice()
    user_input = input(f"Would you like to save to {filename}?")
    if user_input == 'yes':
        save_projects(projects)
    print("Thank you for using custom-built project management software.")


def display_menu():
    """Display the menu options."""
    menu = ("(L)oad projects \n(S)ave projects \n(D)isplay projects "
            "\n(F)ilter projects by date \n(A)dd new project \n(U)pdate project \n(Q)uit")
    print(menu)


def get_choice():
    """user's choice."""
    return input(">>> ").upper()


def load_projects():
    projects = []
    # filename = input("filename to load: ") # actual code
    filename = 'projects.txt'  # for test purposes
    in_file = open(filename, 'r')
    in_file.readline()  # remove the header
    for line in in_file:
        parts = line.strip().split('\t')  # split by tabs in the code
        date = datetime.datetime.strptime(parts[1], "%d/%m/%Y")
        project = Project(parts[0], date, int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)
    in_file.close()
    print(f"{filename} loaded")

    return projects


def save_projects(projects):
    filename = input("Filename to save to: ")
    with open(filename, 'w') as out_file:
        out_file.write("Name\tStart Date\tPriority\tEstimate\tCompletion Percentage\n")  # adding header
        for project in projects:
            out_file = out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}"
                                      f"\t{project.estimate}\t{project.completion_percentage}\n")
        print(f"Projects saved to {filename}")


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]

    incomplete_projects_sorted = sorted(incomplete_projects)
    completed_projects_sorted = sorted(completed_projects)

    print("Incomplete projects:")
    for project in incomplete_projects_sorted:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects_sorted:
        print(f"  {project}")

    return projects


def filter_project(projects):
    date = get_valid_date("Show projects that start after date (dd/mm/yy):")
    print(f"That day is/was {date.strftime('%A')}")
    print(date.strftime("%d/%m/%Y"))
    filtered_projects = [project for project in projects if project.start_date > date]
    filtered_projects.sort(key=attrgetter("start_date"))
    for project in filtered_projects:
        print(project)


def add_project(projects):
    print("Let's add a new project")
    name = valid_name()
    date = get_valid_date("Start date (dd/mm/yy): ")
    priority = get_valid_number("Priority: ")
    cost = get_valid_number("Cost estimate: $")
    percentage = get_valid_number("Percent complete: ")
    new_project = Project(name, date, priority, cost, percentage)
    projects.append(new_project)
    print(f"Added new project: {new_project}")


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_choice = valid_project_choice(projects)
    project = projects[project_choice]
    print(f"{project}")

    new_percentage = get_valid_number("New Percentage:")
    if new_percentage != '':
        project.completion_percentage = new_percentage
    new_priority = get_valid_number("New Priority:")
    if new_priority != '':
        project.priority = new_priority


def valid_name():
    name = input("Name: ")
    while name == '':
        print("Can't be empty!")
        name = input("Name: ")
    return name


def valid_project_choice(projects):
    project_choice = int(input("Project choice:"))
    while 0 > project_choice > len(projects) - 1:  # Check if number is out of valid range
        print("Invalid place number.")
        project_choice = int(input("Project choice:"))  # Get a valid number from the user
    return project_choice


def get_valid_number(prompt):
    """valid score between 0 and 100."""
    number = int(input(prompt))
    while number < 0 or number > 100:
        print("Invalid number")
        number = int(input(prompt))
    return number


def get_valid_date(prompt):
    """Prompt for a valid date in dd/mm/yy format."""
    date_input = input(prompt)
    valid = False
    while not valid:
        try:
            date = datetime.datetime.strptime(date_input, "%d/%m/%y")
            valid = True  # If the date is valid, stop the loop
        except ValueError:
            print("Invalid date format. Please use dd/mm/yy.")
            date_input = input(prompt)  # Ask the user to input the date again
    return date


main()
