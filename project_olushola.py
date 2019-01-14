# Program to compute pupils results
#Olushola Sunday
#Code Lagos 5.0
#06/12/2018
print('WELCOME TO SAINT MARIS INTERNATIONAL SCHOOL RESULT COLLATION SHEET')
grand_total = 0
name = input('What is your name: ')
print('Welcome',name.upper(),'are you ready for the result compilation')
response = input('enter yes or No?: ')
if (response.lower() == 'yes'):
    #Requesting the test values from the user 
    subjects_test_score = dict(Maths = input("enter mathematics test score: "),Eng = input("enter english test score: "),Bscience = input("enter basic science test score: "),Heducation = input("enter health education test score: "),Agric = input("enter agricultural science test score: "),Heconomics = input("enter home economics test score: "),Yoruba = input("enter yoruba language test score: "),Sstudies = input("enter social studies test score: "),Crk = input("enter christian religious knowledge test score: "),Cca = input("enter creative & cultural arts test score: "),)
    print(name.upper(), 'TEST SCORES')
    for x,y in subjects_test_score.items(): 
        print(x,y)
    print('Test scores successfully entered would you like to continue: Enter Yes/No')
    response = input('enter yes or No?: ')
    if (response.lower() == 'yes'):
    #Requesting Exam scores from the User
        subjects_examination_score = dict(Maths = input("enter mathematics examination score: "),Eng = input("enter english examination score: "),Bscience = input("enter basic science examination score: "),Heducation = input("enter health education examination score: "),Agric = input("enter agricultural science examination score: "),Heconomics = input("enter home economics examination score: "),Yoruba = input("enter yoruba language examination score: "),Sstudies = input("enter social studies examination score: "),Crk = input("enter christian religious knowledge examination score: "),Cca = input("enter creative & cultural arts examination score: "),)
        print(name.upper(), 'EXAMINATION SCORES')
        for x,y in subjects_examination_score.items():
            print(x,y)
    else: print('your response is wrong')
    # Computing the Total for each subjecst
    maths1 =int(subjects_test_score['Maths'])
    maths2 = int(subjects_examination_score['Maths'])
    eng1 =int(subjects_test_score['Eng'])
    eng2 = int(subjects_examination_score['Eng'])
    bscience1 =int(subjects_test_score['Bscience'])
    bscience2 = int(subjects_examination_score['Bscience'])
    heducation1 =int(subjects_test_score['Heducation'])
    heducation2 = int(subjects_examination_score['Heducation'])
    agric1 =int(subjects_test_score['Agric'])
    agric2 = int(subjects_examination_score['Agric'])
    heconomics1 =int(subjects_test_score['Heconomics'])
    heconomics2 = int(subjects_examination_score['Heconomics'])
    yoruba1 =int(subjects_test_score['Yoruba'])
    yoruba2 = int(subjects_examination_score['Yoruba'])
    sstudies1 =int(subjects_test_score['Sstudies'])
    sstudies2 = int(subjects_examination_score['Sstudies'])
    crk1 =int(subjects_test_score['Crk'])
    crk2 = int(subjects_examination_score['Crk'])
    cca1 =int(subjects_test_score['Cca'])
    cca2 = int(subjects_examination_score['Cca'])
    subjects_total_score = dict(Maths = (maths1 + maths2), Eng = (eng1 + eng2), Bscience = (bscience1 +bscience2), Heducation = (heducation1 + heducation2), Agric = (agric1 + agric2), Heconomics = (heconomics1 + heconomics2), Yoruba = (yoruba1 + yoruba2), Sstudies = (sstudies1 + sstudies2), Crk = (crk1 + crk2), Cca = (cca1 + cca2))
    print('The TOTAL SCORE for each subject offered is ')
    for x,y in subjects_total_score.items():
        grand_total += y 
        print(x,y)
    average_score = float(grand_total/10)
    percentage_score = float((grand_total/1000)*100)
    print(name.upper(),'HERE IS YOUR RESULT')
    print('{:10}'.format('GRANDTOTAL:'),grand_total, ' AVERAGE SCORE:',average_score, ' PERCENTAGE SCORE:', percentage_score)
    
else:
    print('Get back when you are ready')
