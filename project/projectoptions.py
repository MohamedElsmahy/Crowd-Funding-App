from projectoperations import createProject, viewProject, editProject, deleteProject, searchProject

def projectOptions(email):
    choice = input("please write c for create a project , v for view all projects , e for edit your project ,"
                   " d for delete your project , s  for search for a project using date  : ")
    # choice = choice.strip()
    # if choice.isalpha():
    if choice == "c":
        createProject(email)
    elif choice == "v":
        viewProject(email)
    elif choice == "e":
        editProject(email)
    elif choice == "d":
        deleteProject(email)
    elif choice == "s":
        searchProject(email)
