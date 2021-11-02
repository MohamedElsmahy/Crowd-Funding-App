import datetime

def createProject(email):
    while True:
        projectID = input("please enter your project ID :")
        if projectID.isdigit():
            break

    while True:
        title = input("please enter your project name :")
        if title.isalpha():
            break

    while True:
        details = input("please enter your project details :")
        if details.isalpha():
            break

    while True:
        total_target = input("please enter your total target of money :")
        if total_target.isdigit():
            break

    while True:
        project_start_time = input("please enter start date of project in (dd-mm-yyyy) :")
        try:
            date_format = "%d-%m-%Y"
            datetime.datetime.strptime(project_start_time, date_format)
        except ValueError:
            print("This is the incorrect date format")
        else:
            d1 = datetime.datetime.strptime(project_start_time, date_format)
            d2 = datetime.datetime.now()
            if d1 > d2:
                break
            else:
                print("Date can't be the same current date")

    while True:
        project_end_time = input("please enter end date of project in (dd-mm-yyyy) :")
        try:
            date_format = "%d-%m-%Y"
            datetime.datetime.strptime(project_end_time, date_format)
        except ValueError:
            print("This is the incorrect date format")
        else:
            d1 = datetime.datetime.strptime(project_end_time, date_format)
            d2 = datetime.datetime.strptime(project_start_time, date_format)
            if d1 > d2:
                break
            else:
                print("Date can't be the same current date")


    projectlist = ",".join([projectID, title, details, total_target, project_start_time,project_end_time,email])
    projectlist = projectlist + "\n"

    try:
        projectfile = open("projects.txt")
    except:
        print("file not found")
    else:
        data = projectfile.readlines()
        projects = []
        for item in data:
            projects.append(item.strip("\n"))
        for project in projects:
            projectdetails = project.split(",")
            if projectdetails[0] == projectID:
                print("## project already exist pick another project ID ##")
                projectfile.close()
                createProject()
        else:
            projectfile.close()
            try:
                wfile = open("projects.txt", "a")
            except:
                print("file not found")
            else:
                wfile.write(projectlist)
                wfile.close()
                print("## project created successfully ##")


def viewProject(email):
    try:
        projectfile = open("projects.txt")
    except:
        print("file not found")
    else:
        data = projectfile.readlines()
        projects = []
        for item in data:
            projects.append(item.strip("\n"))
        for project in projects:
            projectdetails = project.split(",")
            if projectdetails[6] == email:
                print(f"## {projects} ##")
                projectfile.close()
                break
        else:
            print("## you dosent create project untill now go and create one ! ##")
            createProject(email)


def editProject(email):
    deleteProject(email)
    createProject(email)


def deleteProject(email):
    try:
        projectfile = open("projects.txt")
    except:
        print("file not found")
    else:
        data = projectfile.readlines()
        projects = []
        for item in data:
            projects.append(item.strip("\n"))
        projectid = input("enter ID of project you want to delete :")
        for project in projects:
            projectdetails = project.split(",")
            if projectdetails[0] == projectid and projectdetails[6] == email:
                projects.remove(project)
                print("## project deleted successfully ##")
                projectfile.close()
                wfile = open("projects.txt", "w")
                for line in projects:
                    wfile.write(line + "\n")
                wfile.close()
                break
        else:
            print("## you choose wrong ID or wrong loggoed in user##")
            deleteProject(email)


def searchProject(email):
    try:
        projectfile = open("projects.txt")
    except:
        print("file not found")
    else:
        data = projectfile.readlines()
        projects = []
        for item in data:
            projects.append(item.strip("\n"))
        project_start_date = input("enter start date of project you want to show :")
        project_end_date = input("enter end date of the same project you want to show :")
        for project in projects:
            projectdetails = project.split(",")
            if projectdetails[4] == project_start_date and projectdetails[5] == project_end_date:
                if projectdetails[6] == email:
                    print(f"## {project} ##")
                    projectfile.close()
                    break
            # break
        else:
            print("## you entered wrong date of project search again ! ##")
            searchProject(email)