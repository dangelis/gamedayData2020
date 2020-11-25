import csv

with open ("Gameday Responses 11.24.20 11am.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
       
       first_name = row['First Name']
       last_name = row['Last Name']
       dob = row['Date of Birth']
       gender = row['Gender']
       grade = row['Current Grade Level']
       #league = row['?'] TODO
       team = row['Team Name']
       guardian_name = row['Parent/Guardian first name'] + " " + row['Parent/Guardian last name']
       guardian_email = row['Email']
       guardian_phone = row['Mobile Phone'] # or emergency phone?
       eval_score = row['Evaluation Score']
       years_experience = row['How many years has this child athlete participated in GAMEDAY or another basketball/cheer program prior to this?']
       height_ft = row['Height'] # TODO, parse out ft
       height_in = row['Height'] # TODO, parse out inches
       # TODO: requests will need some logic
       nights_not_avail = row['Request #1: Is there a night of the week this child athlete is not available to practice?']
       requested_coach = row['Request #3: If possible, is there a specific coach you would like this child athlete to play for?']
       requested_friend = row['Request #2: If possible, is there a specific friend or sibling you would like this child athlete to play with?']
       sib_list = row['If yes, please list the name(s) of the sibling(s).']
       sib_1 = row['Gender']
       sib_2 = row['Gender']
       sib_3 = row['Gender']
       special_request_priority = row['*Please indicate which of the following requests is the highest priority for you:']
       request_other = row['If other, what special request would you like to make?']

       print("""******************
       first_name = {}
       last_name = {}
       dob = {}
       gender = {}
       grade = {}
       team = {}
       guardian_name = {}
       guardian_email = {}
       guardian_phone = {}
       eval_score = {}
       years_experience = {}
       height_ft = {}
       height_in = {}
       nights_not_avail = {}
       requested_coach = {}
       requested_friend = {}
       sib_list = {}
       sib_1 = {}
       sib_2 = {}
       sib_3 = {}
       special_request_priority = {}
       request_other = {}"""
        .format(first_name,
        last_name,
        dob,
        gender,
        grade,
        team,
        guardian_name,
        guardian_email,
        guardian_phone,
        eval_score,
        years_experience,
        height_ft,
        height_in,
        nights_not_avail,
        requested_coach,
        requested_friend,
        sib_list,
        sib_1,
        sib_2,
        sib_3,
        special_request_priority,
        request_other))
