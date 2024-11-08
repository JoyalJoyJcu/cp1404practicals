from project import Project
import datetime
from operator import attrgetter

FILENAME = 'projects.txt'  # for convenience (not code)


def main():
    """ Runs the project management menu, allowing users to load, save, display, filter,
    add, and update projects until they choose to quit. Prompts for saving before exit. """
    projects = []
    display_menu()
    choice = get_valid_choice()
    while choice != "Q":
        if choice == "L":
            # filename = valid_name("filename to load: ") # what it should have
            projects = load_projects(FILENAME)  # for test purposes, would be above code for code
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
        choice = get_valid_choice()
    user_input = input(f"Would you like to save to {FILENAME}?")  # would use filename from load
    if user_input == 'yes':
        save_projects(projects)
    print("Thank you for using custom-built project management software.")


def display_menu():
    """Display the menu options."""
    menu = ("(L)oad projects \n(S)ave projects \n(D)isplay projects "
            "\n(F)ilter projects by date \n(A)dd new project \n(U)pdate project \n(Q)uit")
    print(menu)


def get_valid_choice():
    """ Prompts for a valid menu choice"""
    user_choice = input(">>> ").upper()
    while user_choice != 'L,S,D,F,A,U,Q':
        print("Invalid choice. Please try again.")
        user_choice = input(">>> ").upper()
    return user_choice


def load_projects(filename):
    """Loads project data from a file, skipping the header, and adds each project to a list."""
    projects = []
    in_file = open(filename, 'r')
    in_file.readline()  # remove the header
    for line in in_file:
        parts = line.strip().split('\t')  # split by tabs in the code
        date = datetime.datetime.strptime(parts[1], "%d/%m/%Y")  # formate it right
        project = Project(parts[0], date, int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)
    in_file.close()
    print(f"{filename} loaded")

    return projects


def save_projects(projects):
    """Saves project data to a specified file, including a header row."""
    filename = input("Filename to save to: ")
    with open(filename, 'w') as out_file:
        out_file.write("Name\tStart Date\tPriority\tEstimate\tCompletion Percentage\n")  # adding header
        for project in projects:
            out_file = out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}"
                                      f"\t{project.estimate}\t{project.completion_percentage}\n")
        print(f"Projects saved to {filename}")


def display_projects(projects):
    """Displays incomplete and completed projects separately, sorted within each group."""
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
    """Filters and displays projects starting after a specified date, sorted by start date."""
    date = get_valid_date("Show projects that start after date (dd/mm/yy):")
    print(f"That day is/was {date.strftime('%A')}")
    print(date.strftime("%d/%m/%Y"))  # formats the code
    filtered_projects = [project for project in projects if project.start_date > date]
    filtered_projects.sort(key=attrgetter("start_date"))  # sort by date
    for project in filtered_projects:
        print(project)


def add_project(projects):
    """Adds a new project to the list by prompting for details like name,
    start date, priority, cost estimate, and completion percentage."""
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
    """Allows the user to update the completion percentage and
    priority of an existing project."""
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
    """Prompts the user to enter a non-empty name.
    Repeats until a valid name is provided."""
    name = input("Name: ")
    while name == '':
        print("Can't be empty!")
        name = input("Name: ")
    return name


def valid_project_choice(projects):
    """Prompts the user to select a valid project by index,
    ensuring the input is within the valid range."""
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
