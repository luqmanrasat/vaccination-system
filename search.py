from utils import getPatientById, getVaccinationRecordById, getVaccineByVacCode, isInputInt


def search(patientList, vaccineList, vaccinationRecordList):
    isComplete = False
    isPatientExist = True

    while (not isComplete and isPatientExist):
        # prompt user for patient id
        isValid = False
        while not isValid:
            patientId = input('Please enter patient id: ')
            # validation
            isValid = isInputInt(patientId)
            if not isValid:
                continue
            patientId = int(patientId)

        # get patient
        patient = getPatientById(patientId, patientList)
        if patient is None:
            print('No patient with matching id.')
            isPatientExist = False
            break
        
        vacCode = patient.vacSelected

        # get vaccine & vaccination record
        vaccine = getVaccineByVacCode(vacCode, vaccineList)
        vaccinationRecord = getVaccinationRecordById(patientId, vaccinationRecordList)

        dosRequired = vaccine.dosRequired
        dose1 = vaccinationRecord.dose1
        dose2 = vaccinationRecord.dose2

        # print results
        print("{:<30} | {:<16}{:<6}".format('', '', 'Status'))
        print("{:<12} | {:<15} | {:<13} | {:<12} | {:<12}".format('Vaccine Code', 'Dosage Required', 'Before Dose 1', 'After Dose 1', 'After Dose 2'))
        print("{:<12} | {:<15} | {:<13} | {:<12} | {:<12}".format(vacCode, dosRequired, 'NEW', dose1, dose2))

        isComplete = True