# LinkedIn Premium Web Scrapping example

 The Lnk_scrapper is a class based system that extracts specific information from different companies' LinkedIn profiles
 and stores the information in a .csv file that works as a results database. It is based on selenium for the web scrapping
 process since some information is generated depending on interactions like mouse hoovering.

 The Lnk_scrapper aims to be scalable and modular through the usage of classes. 

 1. Executing the function
    - Open a terminal in the same place as main.py
    - arguments: give them separated by spaces
        * username: must have Linkedin Premium account
        * Password: Is required in the console so it is not stored in any file
        * companies list: separated by spaces.

        [locate on main.py dir] python main.py username@email.com Pa$$w0rd google microsoft amazon (etc)

    The system opens a Chrome browser and navigates autonomously over the required companies LinkedIn profiles.
    

2. Database
    Each excecution will generate as many new rows as companies consulted. Database contains the following fields
    - Index: rows numerical index
    - Timestamp: YYYY/mm/dd of the search
    - Company: company name
    - Q_period: Quarterly period reported by LinkedIn on the search date
    - Total_openings: Total job openings
    - Sales_openings: job openings for sales positions

    Database is stored as .csv file in [working_directory]/Database/data.csv

3. Modules

    3.1. utils.py
        Contains execution constants (paths, stardard Xpaths for the searchs, etc).  It makes customization faster and avoids
        manual parameter input on the .py modules.

    3.2. Database.py
        Manages the dataset connection and manipulation. Using database as an indivual file eases switching between databases structures.
        If there is not a database file in the file location, creates a new file

    3.3. LnkDriver.py
        Instantiates a browser and allows navigation through LinkedIn profiles using the company name

    3.4. LnkCrawler.py
        Implements web scrapping using selenium to extract the target information. Creates a pandas dataframe chunk each time the function is called

    3.5. main.py
        Base module that instantiates the classes and coordinates the interactions between them for the web scrapping.
