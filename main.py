import os
from classes.Vaccine import Vaccine
from utils import isInputInRange, isInputInt, loadPatients, loadVaccinationRecords
from register import register
from vacAdmin import vacAdmin
from search import search
from statsInfo import statsInfo

# Constants
VC_LIST = ['VC1', 'VC2']
VACCINE_LIST = [
    Vaccine('AF', 2, 2, 12, '-'),
    Vaccine('BV', 2, 3, 18, '-'),
    Vaccine('CZ', 2, 3, 12, 45),
    Vaccine('DM', 2, 4, 12, '-'),
    Vaccine('EC', 1, '-', 18, '-'),
]

# print main menu

def printMenu():
    os.system('cls')
    print('MAIN MENU')
    print('0. New Patient Registration')
    print('1. Vaccine Administration')
    print('2. Search Patient Record and Vaccination Status')
    print('3. Statistical Information on Patients Vaccinated')
    print('4. Exit')

patientList = loadPatients()
vaccinationRecordList = loadVaccinationRecords()

# menu loop
isStart = True
while isStart:
    printMenu()
    isValid = False
    while not isValid:
        selectMenu = input('Please enter your selection number: ')
        # validation
        isValid = isInputInt(selectMenu)
        if not isValid:
            continue
        selectMenu = int(selectMenu)
        isValid = isInputInRange(selectMenu, 0, 4)
        if not isValid:
            continue
    
    os.system('cls')
    # REGISTRATION
    if selectMenu == 0:
        newPatientId = len(patientList)
        registerResult = register(VC_LIST, VACCINE_LIST, newPatientId)
        if registerResult is not None:
            patientList.append(registerResult[0])
            vaccinationRecordList.append(registerResult[1])
        input("Press Enter to continue...")
        continue

    # VACCINE ADMINISTRATION
    elif selectMenu == 1:
        vacAdminResult = vacAdmin(patientList, VACCINE_LIST, vaccinationRecordList)
        if vacAdminResult is not None:
            patientId = vacAdminResult[0]
            newVaccinationRecord = vacAdminResult[1]
            vaccinationRecordList[patientId] = newVaccinationRecord
        input("Press Enter to continue...")
        continue

    # SEARCH RECORD
    elif selectMenu == 2:
        search(patientList, VACCINE_LIST, vaccinationRecordList)
        input("Press Enter to continue...")
        continue

    # STATISTICS INFORMATION
    elif selectMenu == 3:
        statsInfo(patientList, vaccinationRecordList, VC_LIST)
        input("Press Enter to continue...")
        continue

    # EXIT
    else:
        print('Bye')
        isStart = False