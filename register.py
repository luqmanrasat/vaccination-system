from classes.Patient import Patient
from classes.VaccinationRecord import VaccinationRecord
from utils import isInputInRange, isInputInt, savePatient, saveVaccinationRecord


# print available vaccine centres
# vcList -> string[]
def printVaccineCentres(vcList):
    print("{:<3} | {:<3}".format('No.', 'Vaccine Centre'))
    for index, centre in enumerate(vcList):
        print("{:<3} | {:<3}".format(index, centre))


# check for eligible vaccines using patient's age
# age -> int
# vaccinesList -> Vaccine[]
# returns Vaccine[]
def checkEligibleVaccines(age, vaccinesList):
    eligibleVaccineList = []
    for vaccine in vaccinesList:
        if vaccine.isEligible(age):
            eligibleVaccineList.append(vaccine)
    return eligibleVaccineList


# print eligible vaccines info
# eligibleVaccineList -> Vaccine[]
def printEligibleVaccines(eligibleVaccineList):
    vaccineInfoList = []
    for vaccine in eligibleVaccineList:
        vaccineInfo = [vaccine.vacCode, vaccine.dosRequired, vaccine.interval]
        vaccineInfoList.append(vaccineInfo)

    print("{:<3} | {:<12} | {:<15} | {:<15}".format('No.', 'Vaccine Code', 'Dosage Required', 'Interval(weeks)'))
    for index, info in enumerate(vaccineInfoList):
        vacCode = info[0]
        dosRequired = info[1]
        interval = info[2]
        print("{:<3} | {:<12} | {:<15} | {:<15}".format(index, vacCode, dosRequired, interval))



def register(vcList, vaccineList, patientId):
    isComplete = False
    isEligible = True
    
    while (not isComplete and isEligible):
        # prompt user for vc
        isValid = False
        printVaccineCentres(vcList)
        while not isValid:
            vacCentre = input('Select vaccination centre no.: ')
            # validation
            isValid = isInputInt(vacCentre)
            if not isValid:
                continue
            vacCentre = int(vacCentre)
            isValid = isInputInRange(vacCentre, 0, len(vcList)-1)
            if not isValid:
                continue

        # prompt user for contact number
        contactNumber = input('Enter your contact number: ')
        
        # prompt user for age
        isValid = False
        while not isValid:
            age = input('Enter your age: ')
            # validation
            isValid = isInputInt(age)
            if not isValid:
                continue
            age = int(age)

        # check is age is less than 12
        if age < 12:
            print('Children under 12 is not eligible for vaccination.')
            isEligible = False
            break
        
        # prompt user for vaccine selection
        isValid = False
        eligibleVaccineList = checkEligibleVaccines(age, vaccineList)
        printEligibleVaccines(eligibleVaccineList)
        while not isValid:
            vacSelected = input('Select vaccine no.: ')
            # validation
            isValid = isInputInt(vacSelected)
            if not isValid:
                continue
            vacSelected = int(vacSelected)
            isValid = isInputInRange(vacSelected, 0, len(eligibleVaccineList)-1)
            if not isValid:
                continue

        # Create & save Patient
        vc = vcList[vacCentre]
        vacSelected = eligibleVaccineList[vacSelected]
        vacCode = vacSelected.vacCode
        newPatient = Patient(patientId, vc, contactNumber, age, vacCode)
        savePatient(newPatient)

        # Create & save VaccinationRecord
        dosRequired = vacSelected.dosRequired
        if dosRequired == 2:
            newVaccinationRecord = VaccinationRecord(patientId, 'INCOMPLETE', 'INCOMPLETE')
        else:
            newVaccinationRecord = VaccinationRecord(patientId, 'INCOMPLETE')
        saveVaccinationRecord(newVaccinationRecord)
        
        print('Patient id {} created.'.format(newPatient.id))
        isComplete = True
        return [newPatient, newVaccinationRecord]