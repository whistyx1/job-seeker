Job Seeker - an app for finding job vacancies in various specialties


FEATURES:
    - You can search jobs by multi-filter search system. Write filters to the searchbar, it can be single world, separated by space or coma. The app will loop through all of them and add them to the list, duplicate vacancies will be automatically deleted.
    - Work.ua integration. This app parses work.ua for information. Parser for robota.ua doesn't work, but will keep working on this problem.
    - Choose region. You can choose a region from list or if there are not your region you can choose 'other'. In the job card the region will be shown.
    - Save jobs. You can save jobs to json file moreover, In the second all of your saved jobs will be displayed in the convenient format.
    -Delete jobs. AS far you can save jobs, you can delete them from both json file and qsqrollarea list.
    -PyQt5 UI. Clear interface with light colors.
    -Async parsing. It doesn't block your interface.
    -JSON data. Your data saves to json file which will be in the main app folder.

Tech Stack:
    -GUI: PyQt5
    -Web Parsing: BeautifulSoup4, requests, lxml.
    -Multithreading: QThread (PyQt).
    -Data: JSON.
    -Containerization: Docker

Launch:

    -Prerequisites:
        -python 3.8+
        -pip
    
    -Clone github repository:
        -git clone https://github.com/whistyx1/job-seeker.git

    -Install requirements:
        -cd job-seeker
        -pip install -r requirements.txt
    
    -Run app:
        -python main.py


Docker:

    -Build the image:
        -docker build -t job-seeker 


    -Run the container:
        -docker run -it --rm \
        -e DISPLAY=$DISPLAY \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        job-seeker

    -Docker compose:
        -docker-compose up

How to Use?:
    -Add filters. By typing keywords into searchbar and press 'Add a Filter' button.
    -Choose website to search(only work.ua is working yet).
    -Choose a region or Ukraine is set by default.
    -Press 'Search a Job' button.
    -You can save jobs by pressing 'Save' button on the job card in the left side of an app.
    -View saved vacancies in the section 'Saved Jobs List'.