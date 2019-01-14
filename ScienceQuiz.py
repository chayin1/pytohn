# Title: CodeLagos Progress - My Science App
# Author: Samuel Akintola
# Organization: Code Lagos 4.0
# Date: Monday, 10th December 2018

# Designing A Science Quiz To Test A User's Knowledge On Physics;
# It Also Displays A List Of 50 Physics Formulae And 15 Physics Constants;
# It Also Displays The Elements Of The Periodic Table And Their Properties.
# The Purpose Of The App Is To Further Learning Among Science Students.
print("\t\t\t\t\t\t\t\t SAM's SCIENCE QUIZ                     ")

print('(a) Physics Formulae \t\t\t\t\t\t\t (b) Chemical Elements and their Properties')

User = input('Please Enter Your Name______ \n ')
user = input('Please enter the letter you wish to display its functions as shown above_____ ')

if user == 'a' :
    print('You have selected option (a)\n Here is a list of some common Physics Formulae\n '              
          '\t\t\t\t\t\t\t Physics Formulae\n'
           '1  Weight = mass*gravity\n2  Area = length*breadth\n3  Volume = area*height\n4  Speed = distance/time\n5  Velocity = displacement/timetaken \n6  Linear accleration = velocity/time\n7  Force = mass*acceleration\n8  Density = mass/volume\n9  Work = force*distance\n10 Pressure = force/area\n'                                                
           '11 Impulse = force*time\n12 Momentum = mass*velocity\n13 Energy = force*distance\n14 Kinetic energy = 0.5*mass*velocity*velocity\n15 Potential energy = mass*gravityconstant*height\n16 Power = work/time\n17 Electric power = current*current*resistance\n18 Superficial expansivity = 2*linear expansivity\n19 Cubic expansivity = 3*linear expansivity\n20 Electric charge = capacitance*potentialdifference\n'  
           '21 Electric charge = current*time\n22 Resistance = (resistivity*lenght)/area\n23 Refractive index = sin of incidence/sin of refraction\n24 Wavespeed = wavelength*frequency \n25 Frequency = 1nverse of time\n26 Magnification = image height/object height\n27 Number of images = (360/angle of inclination) - 1\n28 Angle of deviation = 2*angle of glance\n29 Focal lenght = radius of curveture*0.5\n30 Refractive index = real depth/apparent depth\n'
           '31 Power of lens = inverse of focal lenght\n32 Intensity of sound = power of source/area\n33 Velocity(air) = (2*distance)/time\n34 Gravitational force = (gravitational constant*mass1*mass2)/(radius*radius)\n35 Escape Velocity = sqrt(2*gravityconstant*radius)\n36 Mass liberated = electochemical equivalent*current*time\n37 Magnetic flux density = magnetic flux/area\n38 Half life = 0.692/radioactive decay constant\n39 Quantity of heat = mass*latent heat\n40 Power factor = real power/apparent power\n'
           '41 Magnetic flux = Magnetic flux density*induced current*length*sin of angle\n42 Surface tension = force/length\n43 Viscosity = force\(area*velocity)\n44 Stress = force/area\n45 Strain = extension/original length\n46 Young modulus = stress/strain\n47 Time of period = Timetaken/number of oscillation\n48 Moment = 2*radius*force\n49 Mechanical advantage = load/effort\n50 Efficiency = (Mechanical advantage/velocity ratio)*100\n')





    print('\t\t\t\t\t\t\t Physics Constants\n'
          "1  Avagadro's number = 6.0221367 × 10^23 mol^-1\n2  Speed of light = 3.0*10^8 m/s\n3  Electron charge = 1.60217733 × 10^-19 C\n4  Faraday's constant = 9.6485309 × 10^4 C mol^-1\n5  g, acceleration of free fall = 9.80665 ms^-2\n6  G,gravitational constant = 6.672 × 10^-11 N m^2 kg^-2\n7  h,Planck's constant = 6.6260755 × 10^-34 Js\n8  k,Boltzmann's constant = 1.380658 × 10^-23 J K^-1\n"
          "9  me,electron rest mass = 9.1093897 × 10^-31 kg\n10 mn, neutron rest mass = 1.6749286 × 10^-27 kg\n11 mp, protron rest mass = 1.6726231 × 10^-27 kg\n12 NL,Loschmidt's number = 2.686763 × 10^25 m^-3\n13 R, ideal gas constant = 8.314510 JK^-1 mol^-1\n14 atm,standard atmosphere = 1.01325 × 10^5 Pa\n15 s,Stefan-Boltzmann constant = 5.67051 × 10^-8 W m^-2 K^-4\n")


    user = input('Do You Wish To Go To Quiz Please Type In Either Yes or No___ ')
    if user == 'Yes':
        print("SAM's Science Quiz\n ")
        Score = 0
        Question_1 = input(
            '(1) Calculate the Weight of an object if the mass is 4kg?\n '
            'Note: acceleration of free fall is a constant\n '
            '(a) 4 \n (b) 12 \n (c) 40 \n (d) 30 \n  ')


        if Question_1.lower() == "c":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')
        Question_2 = input(" (2) Calculate the area of a shape whose length and breadth are 10cm?\n (a)100cm\n (b) 99cm\n (c) 17cm\n (d) 12cm\n ")
        if Question_2.lower() == "a":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_3 = input(
            " (3) The Volume of a certain solid is 2000m^3, calculate its area if its height is 20m?\n (a) 100m^2\n (b) 10m^2\n (c) 10m\n (d) 100m\n ")
        if Question_3.lower() == "a":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_4 = input(
            "(4) A car moved in a displacement of 500m while only using 50secs, calculate its velocity?\n (a) 500m/s^2\n (b) 10m/s^2\n (c) 100m/s^2\n (d) 50m/s^2\n ")
        if Question_4.lower() == "b":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_5 = input(
            " (5) The mass of an object is 500kg while its acceleration is 10m/s^2, calculate its force\n (a) 10*5^2N\n (b) 10*5^3N\n (c) 5*10^3N\n (d) 5*10^2N\n  ")
        if Question_5.lower() == "c":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_6 = input(
            " (6) The velocity of a certain car is 500m/s and its acceleration is 5m/s^2, calculate the timetaken\n (a) 1000secs\n (b) 10secs\n (c) 0secs\n (d) 100secs\n  ")
        if Question_6.lower() == "d":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_7 = input(
            " (7) Calculate the density of a substance whose mass is 250kg and velocity is 1000m^3\n (a) 0.25kgm^-3\n (b) 1.25kgm^-3\n (c) 2.25kgm^-3\n (d) 4.25kgm^-3\n   ")
        if Question_7.lower() == "a":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_8 = input(
            " (8) A certain machine performed Work at 2*10^3Kgm^2s^-2, if the force used is 200kgms^-2 calculate the distance used\n (a) 20m\n (b)10m\n (c) 1m\n (d) 2m\n   ")
        if Question_8.lower() == "b":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_9 = input(
            " (9) Calculate the pressure if the force and area are 4*10^6kgms^6 and 4*10^6m^2 respectively\n (a) 4.0*10^4kgm^2s^-2\n (b) 3.0*10^4kgm^2s^-2\n (c) 1.0*10^4kgm^2s^-2\n (d) 2.0*10^4kgm^2s^-2\n  ")
        if Question_9.lower() == "c":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_10 = input(
            " (10) The angle of incidence of a prism is 60 while its angle of refraction  is 30 calculate its refractive index\n (a) 0.4\n (b) 0.3\n (c) 0.1\n (d) 0.5\n   ")
        if Question_10.lower() == "d":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_11 = input(
            "(11) When a current of 0.5amp passes through an electic circuit for 2secs what amount of mass is liberated?\n (a) 1kg\n (b) 2kg\n (c) 3kg\n (d) 4kg\n   ")
        if Question_11.lower() == "a":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_12 = input(
            " (12)  Calculate the linear expansivity of a rod whose superficial expansivity is 40K^-1\n (a) 50K^-1\n (b) 20K^-1\n (c) 10K^-1\n (d) 90K^-1\n ")
        if Question_12.lower() == "b":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_13 = input(
            " (13) Calculate the linear expansivity of a rod whose cubic expansivity is 90K^-1\n (a) 3000K^-1\n (b) 300K^-1\n (c) 30K^-1\n (d) 3K^-1\n ")
        if Question_13.lower() == "c":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_14 = input(
            " (14) If the workdone by an electric appliance is 800J and the timetaken is 100secs, calculate its power\n (a) 7 watts \n (b) 1 watts\n (c) 3 watts\n (d) 8 watts\n  ")
        if Question_14.lower() == "d":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_15 = input(
            " (15) Calculate the Potential Energy of a machine if its mass and height are 1000kg and 500m respectively"
            "Note: acceleration of free fall is a constant\n "
            "(a) 1.0*10^6N\n (b) 25*10^6N\n (c) 5*10^6N\n (d) 100*10^6N\n  ")
        if Question_15.lower() == "c":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_16 = input(
            " (16) Calculate the Kinetic Energy of a machine if its mass and velocity are 25000kg and 500m/s respectively\n (a) 125*10^5\n (b) 3125*10^5N\n (c) 125*10^6N\n (d) 3125*10^6N\n  ")
        if Question_16.lower() == "d":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_17 = input(
            " (17) Calculate the force of an object if its mass is 200000kg\n "
            "Note: acceleration of free fall is a constant\n "
            "(a) 10*10^6N\n (b) 2*10^6N\n (c) 1*10^6N\n (d) 12*10^6N\n  ")
        if Question_17.lower() == "b":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_18 = input(
            " (18) Calculate the coefficient of static friction if its angle is 45\n (a) 1\n (b) 10\n (c) 30\n (d) 40\n")
        if Question_18.lower() == "a":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_19 = input(
            " (19) Calculate the momentum of a body if the mass is 50kg and its velocity is 10m/s\n (a) 25Nm\n (b) 50Nm\n (c) 500Nm\n (d) 25000Nm\n ")
        if Question_19.lower() == "c":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_20 = input(" (20) Calculate the impulse of a body if its force and time are 5*10^6kgms^-2 and 5*10^3secs respectively?\n (a) 10*10^9Nm\n (b) 15*10^9Nm\n (c) 25*10^9Nm\n (d) 5*10^9Nm\n ")
        if Question_20.lower() == "c":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_21 = input(" (21) Calculate the mass defect if energy released is 9*10^20J\n "
                            "Note: Speed of light is a constant\n "
                            "(a) 10*10^9J\n (b) 15*10^9J\n (c) 1.0*10^4J\n (d) 5*10^9J\n ")
        if Question_21.lower() == "c":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_22 = input(" (22) Calculate the threshold wavelength if the threshold frequency is 4.8*10^14Hz\n "
                            "Note: Speed of light is a constant\n "
                            "(a) 6.25*10^-7m\n (b) 15.25*10^-7m\n (c) 2.25*10^-7m\n (d) 5.25*10^-7m\n ")
        if Question_22.lower() == "a":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_23 = input(" (23) In a reaction the final and initial mass are 5.01*10^-27kg and 5.02*10^-27 respectively. Calculate the energy released in the process\n "
                            "Use Speed of light\n "
                            "(a) 9*10^-13J\n (b) 1*10^-13J\n (c) 2*10^-13J\n (d) 5*10^-13J\n ")
        if Question_23.lower() == "a":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_24 = input(" (24) Calculate the acclerating potential if the frequency of an emitted X-ray is 1.6*10^12Hz\n "
                            "Use Planck's constant and Electron charge\n "
                            "(a) 0.663v\n (b) 66.3v\n (c) 6.63v\n (d) 663.0v\n ")
        if Question_24.lower() == "b":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_25 = input(" (25) Calculate the Force between two bodies if the mass of the first and second body are 10^-30 and 2*10^-27 respectively the distance between them is 5*10^-11\n "
                            "Use the gravitational constant\n "
                            "(a) 53.6*10^-47N\n (b) 0.536*10^-47N\n (c) 5.36*10^-47N\n (d) 536*10^-47N\n ")
        if Question_25.lower() == "b":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_26 = input(" (26) Calculate the Force between two bodies if the mass of the first and second body are 2*10^20 and 10^25 respectively the distance between them is 10^15\n "
                            "Use the gravitational constant\n "
                            "(a) 433.4KN\n (b) 533.4KN\n (c) 233.4KN\n (d) 133.4KN\n ")
        if Question_26.lower() == "d":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_27 = input(" (27) Calculate the mass of silver deposited when a current of 2.6amp is passed through a solution of silver salt for 70minutes\n "
                            "Use Faraday's constant\n "
                            "(a) 32.12g\n (b) 52.12g\n (c) 22.12g\n (d) 12.12g\n ")
        if Question_27.lower() == "d":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_28 = input(" (28) How many atoms are there in 6g of carbon if carbon as a mass of 12g\n "
                            "Use Avagadro's number\n "
                            "(a) 4.01*10^23\n (b) 1.01*10^23\n (c) 2.01*10^23\n (d) 3.01*10^23\n ")
        if Question_28.lower() == "d":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_29 = input(" (29) How many atoms are there in 12g of carbon if carbon as a mass of 12g\n "
                            "Use Avagadro's number\n "
                            "(a) 101.66*10^-24\n (b) 151.66*10^-24\n (c) 21.66*10^-24\n (d) 1.66*10^-24\n ")
        if Question_29.lower() == "d":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')

        Question_30 = input(" (30) Calculate the acclerating potential if the frequency of an emitted X-ray is 1.5*10^12Hz\n"
                            "Use Planck Constant and Electron charge"
                            " \n (a) 10.19V\n (b) 1.19V\n (c) 2.19V\n (d) 6.19V\n ")
        if Question_30.lower() == "d":
            print('Right')
            Score = Score + 1
        else:
            print('Wrong\n')


        print(user, ',Your Score is___ ', Score)
        if (Score <= 5):
            print('You performed extremely low')
        elif (Score <= 15):
            print('You performed Poorly')
        elif (Score <= 20):
            print('You are a Good Science Student')
        elif (Score <= 25):
            print('You are a Good Science Student')
        else:
            print('You are a Professor of Science')
        print(
              ' Answers to the Quiz\n (1) c\n (2) a\n (3) a\n (4) b\n (5) c\n (6) d\n (7) a\n (8) b\n (9) c\n (10) d\n (11) a\n (12) b\n (13) c\n (14) d\n (15) c\n (16) d\n (17) b\n (18) a\n (19) c\n (20) c\n (21) c\n (22) a\n (23) a\n (24) b\n (25) b\n (26) d\n (27) d\n (28) d\n (29) d\n (30) d\n ')

        print("\t\t\t\t\t\t\tThis is SAM's Science Quiz App")
        print(" Please note: approximate values of constant to at least 2 decmial places so as to get exact answers.\n "
              " When using the Science Calculator to exponent use ** for example 10**2=100")

    elif user == 'No':
        print("\t\t\t\t\t\t\tThanks For Using SAM's Science Quiz App")
    else:
        print("Invalid Type In",User,"Please Choose Either Yes or No and make sure your Initials are in CAPITAL LETTERS.")

elif user == 'b':
    print('You have selected option (b)\n '
          'Periodic Table is table of chemical elements: a table of the chemical elements arranged according to their atomic numbers.\n It was developed by Prof Dmitry Ivanovich Mendeleyev who is the founder of Periodic Law.\n'
          'Elements are chemically indivisible substance: any substance that cannot be broken down into a simpler one by a chemical reaction.\n'
          'All other substances are formed from combinations of elements. The periodic table provides a means of arranging all the known elements and even those yet to be discovered.\n'
          'Here is the Elements of the Periodic Table and their Properties in alphabetical order \n '
          '\t\t\t\t\t\t\t\t Elements of the Periodic Table\n'
          'Actinium\nAluminum\nAmericium\nAntimony\nArgon\nArsenic\nAstatine\nBarium\nBerkelium\nBeryllium\nBismuth\nBohrium\nBoron\nBromine\nCadmium\nCalcium\nCadmium\nCalcium\nCalifornium\nCarbon\nCerium\nCesium\nChlorine\nChromium\n'
          'Cobalt\nCopper\nCurium\nDarmstadtium\nDubnium\nDysprosium\nEinsteinium\nErbium\nEuropium\nFermium\nFluorine\nFrancium\nadolinium\nGallium\nGermanium\nGold\nHafnium\nHassium\nHelium\nHolmium\nHydrogen\nIndium\nIodine\nIridium\n'
          'Iodine\nIridium\nIron\nKrypton\nLanthanum\nLawrencium\nLead\nLithium\nLutetium\nMagnesium\nManganese\nMeitnerium\nMendelevium\nMercury\nMolybdenum\nNeodymium\nNeon\nNeptunium\nNickel\nNiobium\nNitrogen\nNobelium\nOsmium\nOxygen\n'  
          'Palladium\nPhosphorus\nPlatinum\nPlutonium\nPolonium\nPotassium\nPraseodymium\nPromethium\nProtacti|nium\nRadium\nRadon\nRhenium\nRhodium\nRubidium\nRuthenium\nRutherfordium\nSamarium\nScandium\nSeaborgium\nSelenium\n'                                                              
          'Silicon\nSilver\nSodium\nStrontium\nSulfur\nTantalum\nTechnetium\nTellurium\nTerbium\nThallium\nThorium\nThulium\nTin\nTitanium\nTungsten\nUnunbium\n'
          'Ununhexium\nUnunquadium\nRoentgenium\nUranium\nVanadium\nXenon\nYtterbium\nYttrium\nZinc\nZirconium\n')

    user = input('Please enter the name of the element you wish to display its properties as shown above_____\n ')


    print(
        'Please note elements with * in their Relative Molecular Mass are based on the carbon-12 isotope as the standard.\n '
        'These are the values of the most stable isotope.')




    if user == 'Actinium':
        print('Element: Actinium\n' 'Symbol: Ac\n' 'Atomic number: 89\n' 'Relative atomic mass: 227*\n ')

    elif user == 'Aluminium':
        print('Element: Aluminium\n' 'Symbol: Al\n' 'Atomic number: 13\n' 'Relative atomic mass: 26.9815\n ')

    elif user == 'Americium':
        print('Element: Americium\n' 'Symbol: Am\n' 'Atomic number: 95\n' 'Relative atomic mass: 243*\n ')

    elif user == 'Antimony':
        print('Element: Antimony\n' 'Symbol: Sb\n' 'Atomic number: 51\n' 'Relative atomic mass: 121.75\n ')

    elif user == 'Argon':
        print('Element: Argon\n' 'Symbol: Ar\n' 'Atomic number: 18\n' 'Relative atomic mass: 39.948\n ')

    elif user == 'Arsenic':
        print('Element: Arsenic\n' 'Symbol: As\n' 'Atomic number: 33\n' 'Relative atomic mass: 74.9216\n ')

    elif user == 'Astatine':
        print('Element: Astatine\n' 'Symbol: At\n' 'Atomic number: 85\n' 'Relative atomic mass: 210*\n ')

    elif user == 'Barium':
        print('Element: Barium\n ' 'Symbol: Ba\n' 'Atomic number: 56\n' 'Relative atomic mass: 137.34\n ')

    elif user == 'Berkelium':
        print('Element: Berkelium\n' 'Symbol: Bk\n' 'Atomic number: 97\n' 'Relative atomic mass: 249*\n ')

    elif user == 'Beryllium':
        print('Element: Beryllium\n' 'Symbol: Be\n' 'Atomic number: 4\n' 'Relative atomic mass: 9.0122\n ')

    elif user == 'Bismuth':
        print('Element: Bismuth\n' 'Symbol: Bi\n' 'Atomic number: 83\n' 'Relative atomic mass: 208.9086\n ')

    elif user == 'Boron':
        print('Element: Boron\n' 'Symbol: B\n' 'Atomic number: 5\n' 'Relative atomic mass: 10.81\n ')

    elif user == 'Bohrium':
        print('Element: Bohrium\n' 'Symbol: Bh\n' 'Atomic number: 107\n' 'Relative atomic mass: 262*\n ')

    elif user == 'Bromine':
        print('Element: Bromine\n' 'Symbol: Br\n' 'Atomic number: 35\n' 'Relative atomic mass: 79.904\n ')

    elif user == 'Cadmium':
        print('Element: Cadmium\n' 'Symbol: Cd\n' 'Atomic number: 48\n' 'Relative atomic mass: 112.40\n ')

    elif user == 'Caesium':
        print('Element: Caesium\n' 'Symbol: Cs\n' 'Atomic number: 55\n' 'Relative atomic mass: 132.9055\n ')

    elif user == 'Calcium':
        print('Element: Calcium\n' 'Symbol: Ca\n' 'Atomic number: 20\n' 'Relative atomic mass: 40.08\n ')

    elif user == 'Californium':
        print('Element: Californium\n' 'Symbol: Cf\n' 'Atomic number: 98\n' 'Relative atomic mass: 251*\n ')

    elif user == 'Carbon':
        print('Element: Carbon\n' 'Symbol: C\n' 'Atomic number: 6\n' 'Relative atomic mass: 12.011\n ')

    elif user == 'Cerium':
        print('Element: Cerium\n' 'Symbol: Ce\n' 'Atomic number: 58\n' 'Relative atomic mass: 140.12\n ')

    elif user == 'Chlorine':
        print('Element: Chlorine\n' 'Symbol: Cl\n' 'Atomic number: 17\n' 'Relative atomic mass: 35.453\n ')

    elif user == 'Chromium':
        print('Element: Chromium\n' 'Symbol: Cr\n' 'Atomic number: 24\n' 'Relative atomic mass: 51.996\n ')

    elif user == 'Cobalt':
        print('Element: Cobalt\n' 'Symbol: Co\n' 'Atomic number: 27\n' 'Relative atomic mass: 58.933\n ')

    elif user == 'Copper':
        print('Element: Copper\n' 'Symbol: Cu\n' 'Atomic number: 29\n' 'Relative atomic mass: 63.546\n ')

    elif user == 'Curium':
        print('Element: Curium\n' 'Symbol: Cm\n' 'Atomic number: 96\n' 'Relative atomic mass: 247\n ')

    elif user == 'Dysprosium':
        print('Element: Dysprosium\n' 'Symbol: Dy\n' 'Atomic number: 66\n' 'Relative atomic mass: 162.50\n ')

    elif user == 'Dubnium':
        print('Element: Dubnium\n' 'Symbol: Db\n' 'Atomic number: 105\n' 'Relative atomic mass: 262*\n ')

    elif user == 'Darmstadtium':
        print('Element: Darmstadtium\n' 'Symbol: Ds\n' 'Atomic number: 110\n' 'Relative atomic mass: 271*\n ')

    elif user == 'Einsteinium':
        print('Element: Einsteinium\n' 'Symbol: Es\n' 'Atomic number: 99\n' 'Relative atomic mass: 254*\n ')

    elif user == 'Erbium':
        print('Element: Erbium\n' 'Symbol: Er\n' 'Atomic number: 68\n' 'Relative atomic mass: 167.26\n ')

    elif user == 'Europium':
        print('Element: Europium\n' 'Symbol: Eu\n' 'Atomic number: 63\n' 'Relative atomic mass: 151.96\n ')

    elif user == 'Fermium':
        print('Element: Fermium\n' 'Symbol: Fm\n' 'Atomic number: 100\n' 'Relative atomic mass: 257*\n ')

    elif user == 'Fluorine':
        print('Element: Fluorine\n' 'Symbol: F\n' 'Atomic number: 9\n' 'Relative atomic mass:18.9984 \n ')

    elif user == 'Francium':
        print('Element: Francium\n' 'Symbol: Fr\n' 'Atomic number: 87\n' 'Relative atomic mass:223* \n ')

    elif user == 'Gadolinium':
        print('Element: Gadolinium\n' 'Symbol: Gd\n' 'Atomic number: 64\n' 'Relative atomic mass:157.25 \n ')

    elif user == 'Gallium':
        print('Element: Gallium\n' 'Symbol: Ga\n' 'Atomic number: 31\n' 'Relative atomic mass:69.72 \n ')

    elif user == 'Germanium':
        print('Element: Germanium\n' 'Symbol: Ge\n' 'Atomic number: 32\n' 'Relative atomic mass:72.95 \n ')

    elif user == 'Gold':
        print('Element: Gold\n' 'Symbol: Au\n' 'Atomic number: 79\n' 'Relative atomic mass:196.9665 \n ')

    elif user == 'Hafnium':
        print('Element: Hafnium\n' 'Symbol: Hf\n' 'Atomic number: 72\n' 'Relative atomic mass:178.49 \n ')

    elif user == 'Hassium':
        print('Element: Hassium\n' 'Symbol: Hs\n' 'Atomic number: 108\n' 'Relative atomic mass: 263* \n ')

    elif user == 'Hahnium':
        print('Element: Hahnium\n' 'Symbol: Ha\n' 'Atomic number: 105\n' 'Relative atomic mass:262* \n ')

    elif user == 'Helium':
        print('Element: Helium\n' 'Symbol: He\n' 'Atomic number: 2\n' 'Relative atomic mass:4.0026 \n ')

    elif user == 'Holmium':
        print('Element: Holmium\n' 'Symbol: Ho\n' 'Atomic number: 67\n' 'Relative atomic mass:164.9303 \n ')

    elif user == 'Hydrogen':
        print('Element: Hydrogen\n' 'Symbol: H\n' 'Atomic number: 1\n' 'Relative atomic mass:1.008 \n ')

    elif user == 'Indium':
        print('Element: Indium\n' 'Symbol: In\n' 'Atomic number: 49\n' 'Relative atomic mass:114.82 \n ')

    elif user == 'Iodine':
        print('Element: Iodine\n' 'Symbol: I\n' 'Atomic number: 53\n' 'Relative atomic mass:126.9045 \n ')

    elif user == 'Iridium':
        print('Element: Iridium\n' 'Symbol: Ir\n' 'Atomic number: 77\n' 'Relative atomic mass:192.22 \n ')

    elif user == 'Iron':
        print('Element: Iron\n' 'Symbol: Fe\n' 'Atomic number: 26\n' 'Relative atomic mass:55.84 \n ')

    elif user == 'Krypton':
        print('Element: Krypton\n' 'Symbol: Kr\n' 'Atomic number: 36\n' 'Relative atomic mass:83.80 \n ')

    elif user == 'Lanthanum':
        print('Element: Lanthanum\n' 'Symbol: La\n' 'Atomic number: 57\n' 'Relative atomic mass:138.9055 \n ')

    elif user == 'Lawrencium':
        print('Element: Lawrencium\n' 'Symbol: Lw/lr\n' 'Atomic number: 103\n' 'Relative atomic mass:260* \n ')

    elif user == 'Lanthanum':
        print('Element: Lanthanum\n' 'Symbol: La\n' 'Atomic number: 57\n' 'Relative atomic mass:138.9055 \n ')

    elif user == 'Lead':
        print('Element: Lead\n' 'Symbol: Pb\n' 'Atomic number: 82\n' 'Relative atomic mass:207.19 \n ')

    elif user == 'Lithium':
        print('Element: Lithium\n' 'Symbol: Li\n' 'Atomic number: 3\n' 'Relative atomic mass:6.939 \n ')

    elif user == 'Lutetium':
        print('Element: Lutetium\n' 'Symbol: Lu\n' 'Atomic number: 71\n' 'Relative atomic mass:174.97 \n ')

    elif user == 'Magnesium':
        print('Element: Magnesium\n' 'Symbol: Mg\n' 'Atomic number: 12\n' 'Relative atomic mass:24.312 \n ')

    elif user == 'Manganese':
        print('Element: Manganese\n' 'Symbol: Mn\n' 'Atomic number: 25\n' 'Relative atomic mass:54.9380 \n ')

    elif user == 'Meitnerium':
        print('Element: Meitnerium\n' 'Symbol: Mt\n' 'Atomic number: 109\n' 'Relative atomic mass:268* \n ')

    elif user == 'Mendelevium':
        print('Element: Mendelevium\n' 'Symbol: Md\n' 'Atomic number: 101\n' 'Relative atomic mass:258* \n ')

    elif user == 'Mercury':
        print('Element: Mercury\n' 'Symbol: Hg\n' 'Atomic number: 80\n' 'Relative atomic mass:200.59 \n ')

    elif user == 'Molybdenum':
        print('Element: Molybdenum\n' 'Symbol: Mo\n' 'Atomic number: 42\n' 'Relative atomic mass:95.94 \n ')

    elif user == 'Neodymium':
        print('Element: Neodymium\n' 'Symbol: Nd\n' 'Atomic number: 60\n' 'Relative atomic mass:144.24 \n ')

    elif user == 'Neon':
        print('Element: Neon\n' 'Symbol: Ne\n' 'Atomic number: 10\n' 'Relative atomic mass:20.183 \n ')

    elif user == 'Neptunium':
        print('Element: Neptunium\n' 'Symbol: Np\n' 'Atomic number: 93\n' 'Relative atomic mass:237* \n ')

    elif user == 'Nickel':
        print('Element: Nickel\n' 'Symbol: Ni\n' 'Atomic number: 28\n' 'Relative atomic mass:58.71 \n ')

    elif user == 'Niobium':
        print('Element: Niobium\n' 'Symbol: No\n' 'Atomic number:41\n' 'Relative atomic mass:92.9064 \n ')

    elif user == 'Nitrogen':
        print('Element: Nitrogen\n' 'Symbol: N\n' 'Atomic number: 7\n' 'Relative atomic mass:14.0067 \n ')

    elif user == 'Nobelium':
        print('Element: Nobelium\n' 'Symbol: No\n' 'Atomic number: 102\n' 'Relative atomic mass:259* \n ')

    elif user == 'Osmium':
        print('Element: Osmium\n' 'Symbol: Os\n' 'Atomic number: 76\n' 'Relative atomic mass:190.2 \n ')

    elif user == 'Oxygen':
        print('Element: Oxygen\n' 'Symbol: O\n' 'Atomic number: 8\n' 'Relative atomic mass:15.9994 \n ')

    elif user == 'Palladium':
        print('Element: Palladium\n' 'Symbol: Pd\n' 'Atomic number: 46\n' 'Relative atomic mass:106.4 \n ')

    elif user == 'Phosphorus':
        print('Element: Phosphorus\n' 'Symbol: P\n' 'Atomic number: 15\n' 'Relative atomic mass:30.9738 \n ')

    elif user == 'Platinum':
        print('Element: Platinum\n' 'Symbol: Pt\n' 'Atomic number: 78\n' 'Relative atomic mass:195.09 \n ')

    elif user == 'Plutonium':
        print('Element: Plutonium\n' 'Symbol: Pu\n' 'Atomic number: 94\n' 'Relative atomic mass:244* \n ')

    elif user == 'Polonium':
        print('Element: Polonium\n' 'Symbol: Po\n' 'Atomic number: 84\n' 'Relative atomic mass:210* \n ')

    elif user == 'Potassium':
        print('Element: Potassium\n' 'Symbol: K\n' 'Atomic number: 19\n' 'Relative atomic mass:39.102 \n ')

    elif user == 'Praseodymiun':
        print('Element: Praseodymiun\n' 'Symbol: Pr\n' 'Atomic number: 59\n' 'Relative atomic mass:140.9077 \n ')

    elif user == 'Promethium':
        print('Element: Promethium\n' 'Symbol: Pm\n' 'Atomic number: 61\n' 'Relative atomic mass:145* \n ')

    elif user == 'Protactinium':
        print('Element: Protactinium\n' 'Symbol: Pa\n' 'Atomic number: 91\n' 'Relative atomic mass:231.0359 \n ')

    elif user == 'Radium':
        print('Element: Radium\n' 'Symbol: Ra\n' 'Atomic number: 88\n' 'Relative atomic mass:226.0254\n ')

    elif user == 'Radon':
        print('Element: Radon\n' 'Symbol: Rn\n' 'Atomic number: 86\n' 'Relative atomic mass:222* \n ')

    elif user == 'Roentgenium':
        print('Element: Roentgenium\n' 'Symbol: Rg\n' 'Atomic number: 111\n' 'Relative atomic mass:272* \n ')

    elif user == 'Rhenium':
        print('Element: Rhenium\n' 'Symbol: Ra\n' 'Atomic number: 75\n' 'Relative atomic mass:186.2 \n ')

    elif user == 'Rhodium':
        print('Element: Rhodium\n' 'Symbol: Rh\n' 'Atomic number: 45\n' 'Relative atomic mass:102.9055 \n ')

    elif user == 'Rubidium':
        print('Element: Rubidium\n' 'Symbol: Rb\n' 'Atomic number: 37\n' 'Relative atomic mass:85.4678 \n ')

    elif user == 'Ruthenium':
        print('Element: Ruthenium\n' 'Symbol: Ru\n' 'Atomic number: 44\n' 'Relative atomic mass:101.07 \n ')

    elif user == 'Rutherfordium':
        print('Element: Rutherfordium\n' 'Symbol: Rf\n' 'Atomic number: 104\n' 'Relative atomic mass:261* \n ')

    elif user == 'Samarium':
        print('Element: Samarium\n' 'Symbol: Sm\n' 'Atomic number: 62\n' 'Relative atomic mass:150.4 \n ')

    elif user == 'Scandium':
        print('Element: Scandium\n' 'Symbol: Sc\n' 'Atomic number: 21\n' 'Relative atomic mass:44.9559 \n ')

    elif user == 'Seaborgium':
        print('Element: Seaborgium\n' 'Symbol: Sg\n' 'Atomic number: 106\n' 'Relative atomic mass:266* \n ')

    elif user == 'Selenium':
        print('Element: Selenium\n' 'Symbol: Se\n' 'Atomic number: 34\n' 'Relative atomic mass:78.96 \n ')

    elif user == 'Silicon':
        print('Element: Silicon\n' 'Symbol: Si\n' 'Atomic number: 14\n' 'Relative atomic mass:28.086 \n ')

    elif user == 'Silver':
        print('Element: Silver\n' 'Symbol: Ag\n' 'Atomic number: 47\n' 'Relative atomic mass:107.868 \n ')

    elif user == 'Sodium':
        print('Element: Sodium\n' 'Symbol: Na\n' 'Atomic number: 11\n' 'Relative atomic mass:22.9898 \n ')

    elif user == 'Strontium':
        print('Element: Strontium\n' 'Symbol: Sr\n' 'Atomic number: 38\n' 'Relative atomic mass:87.62 \n ')

    elif user == 'Sulphur':
        print('Element: Sulphur\n' 'Symbol: S\n' 'Atomic number: 16\n' 'Relative atomic mass:32.06 \n ')

    elif user == 'Tentalum':
        print('Element: Tentalum\n' 'Symbol: Ta\n' 'Atomic number: 73\n' 'Relative atomic mass:180.9497 \n ')

    elif user == 'Technetium':
        print('Element: Technetium\n' 'Symbol: Tc\n' 'Atomic number: 43\n' 'Relative atomic mass:99* \n ')

    elif user == 'Tellurium':
        print('Element: Tellurium\n' 'Symbol: Te\n' 'Atomic number: 52\n' 'Relative atomic mass:127.60 \n ')

    elif user == 'Terbium':
        print('Element: Terbium\n' 'Symbol: Tb\n' 'Atomic number: 65\n' 'Relative atomic mass:158.9254 \n ')

    elif user == 'Thallium':
        print('Element: Thallium\n' 'Symbol: Tl\n' 'Atomic number: 81\n' 'Relative atomic mass:204.37 \n ')

    elif user == 'Thorium':
        print('Element: Thorium\n' 'Symbol: Th\n' 'Atomic number: 90\n' 'Relative atomic mass:232.0381 \n ')

    elif user == 'Thulium':
        print('Element: Thulium\n' 'Symbol: Tm\n' 'Atomic number: 69\n' 'Relative atomic mass:168.9342 \n ')

    elif user == 'Tin':
        print('Element: Tin\n ' 'Symbol: Sn\n' 'Atomic number: 50\n' 'Relative atomic mass:118.69 \n ')

    elif user == 'Titanium':
        print('Element: Titanium\n' 'Symbol: Ti\n' 'Atomic number: 22\n' 'Relative atomic mass:47.90 \n ')

    elif user == 'Tungsten':
        print('Element: Tungsten\n' 'Symbol: W\n' 'Atomic number: 74\n' 'Relative atomic mass:183.85 \n ')

    elif user == 'Ununbium':
        print('Element: Ununbium\n' 'Symbol: Unb\n' 'Atomic number: 112\n' 'Relative atomic mass:277* \n ')

    elif user == 'Ununhexium':
        print('Element: Ununhexium\n' 'Symbol: Uuh\n' 'Atomic number: 116\n' 'Relative atomic mass:292* \n ')

    elif user == 'Ununquadium':
        print('Element: Ununquadium\n' 'Symbol: Uuq\n' 'Atomic number: 114\n' 'Relative atomic mass:285* \n ')

    elif user == 'Uranium':
        print('Element: Uranium\n' 'Symbol: U\n' 'Atomic number: 92\n' 'Relative atomic mass:238.092 \n ')

    elif user == 'Vanadium':
        print('Element: Vanadium\n' 'Symbol: V\n' 'Atomic number: 23\n' 'Relative atomic mass:50.9414 \n ')

    elif user == 'Xenon':
        print('Element: Xenon\n' 'Symbol: xe\n' 'Atomic number: 54\n' 'Relative atomic mass:131.30 \n ')

    elif user == 'Ytterbium':
        print('Element: Ytterbium\n' 'Symbol: Yb\n' 'Atomic number: 70\n' 'Relative atomic mass:173.04 \n ')

    elif user == 'Yttrium':
        print('Element: Yttrium\n' 'Symbol: Y\n' 'Atomic number: 39\n' 'Relative atomic mass:88.9059 \n ')

    elif user == 'Zinc':
        print('Element: Zinc\n' 'Symbol: Zn\n' 'Atomic number: 30\n' 'Relative atomic mass:65.37 \n ')

    elif user == 'Zirconium':
        print('Element: Zirconium\n' 'Symbol: Zr\n' 'Atomic number: 40\n' 'Relative atomic mass:91.22 \n ')


    else:
        print('Invalid Selection,',User,'Please choose from the above elements and make sure your Initials are in CAPITAL LETTERS.')
else:
    print('Invalid Option,' , User, 'Please choose between (a) or (b) ')





print('\t\t\t This App Is Created To Further And Ease Learning Among Science Students.\t\t\t\t\t\t\t\t\t\t\t\t\t\t')
print('\t\t\t\t\t\t\t Created by SAMUEL AKINTOLA.\t\t\t\t\t\t\t')



