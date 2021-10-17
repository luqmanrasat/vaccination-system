from classes.Patient import Patient
from classes.VaccinationRecord import VaccinationRecord

patientsFile = 'datas/patients.txt'
vaccinationFile = 'datas/vaccination.txt'

##############
# SAVE & LOAD
##############

# Load all patients
# returns Patient[]
def loadPatients():
    file = open(patientsFile, "r")
    patientList = []
    for line in file:
        patientData = line.split()

        id = int(patientData[0])
        vacCentre = patientData[1]
        contactNumber = int(patientData[2])
        age = int(patientData[3])
        vacSelected = patientData[4]

        newPatient = Patient(id, vacCentre, contactNumber, age, vacSelected)
        patientList.append(newPatient)

    file.close()
    return patientList


# Save patient
# patient -> Patient
def savePatient(patient):
    file = open(patientsFile, "a")

    id = patient.id
    vacCentre = patient.vacCentre
    contactNumber = patient.contactNumber
    age = patient.age
    vacSelected = patient.vacSelected

    data = "{} {} {} {} {}\n".format(id, vacCentre, contactNumber, age, vacSelected)
    file.write(data)
    file.close()


# Load all vaccination records
# returns VaccinationRecord[]
def loadVaccinationRecords():
    file = open(vaccinationFile, "r")
    vaccinationRecordList = []
    for line in file:
        vaccinationRecordData = line.split()

        patientId = int(vaccinationRecordData[0])
        dose1 = vaccinationRecordData[1]
        dose2 = vaccinationRecordData[2]

        newVaccinationRecord = VaccinationRecord(patientId, dose1, dose2)
        vaccinationRecordList.append(newVaccinationRecord)

    file.close()
    return vaccinationRecordList


# Save vaccination record
# vaccinationRecord -> VaccinationRecord
def saveVaccinationRecord(vaccinationRecord):
    file = open(vaccinationFile, "r")
    fileData = file.readlines()
    file.close()

    patientId = vaccinationRecord.patientId
    dose1 = vaccinationRecord.dose1
    dose2 = vaccinationRecord.dose2
    data = "{} {} {}\n".format(patientId, dose1, dose2)
    
    # if new patient
    if patientId >= len(fileData):
        file = open(vaccinationFile, "a")
        file.write(data)
    # if patient exist
    else:
        fileData[patientId] = data
        file = open(vaccinationFile, "w")
        for line in fileData:
            file.write(line)

    file.close()

##########
# GETTERS
##########

# get patient by id
# patientId -> int
# patientList -> Patient[]
# returns Patient
def getPatientById(patientId, patientList):
    for patient in patientList:
        if patient.id == patientId:
            return patient


# get vaccine by vac code
# vacCode -> string
# vaccineList -> Vaccine[]
# returns Vaccine
def getVaccineByVacCode(vacCode, vaccineList):
    for vaccine in vaccineList:
        if vaccine.vacCode ==  vacCode:
            return vaccine


# get vaccination record by patient id
# patientId -> int
# vaccinationRecordList -> VaccinationRecord[]
# returns VaccinationRecord
def getVaccinationRecordById(patientId, vaccinationRecordList):
    for vaccinationRecord in vaccinationRecordList:
        if vaccinationRecord.patientId == patientId:
            return vaccinationRecord


##############
# VALIDATIONS
##############

# Check is input integer
# input => any
# returns boolean
def isInputInt(input):
    try:
        int(input)
        return True

    except ValueError:
        print('Input is not an integer')
        return False


# Check is input in range
# input => int
# min => int
# max => int
# returns boolean
def isInputInRange(input, min, max):
    if input >= min and input <= max:
        return True
    print('Input is out of range')
    return False