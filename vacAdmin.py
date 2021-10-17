from utils import getPatientById, getVaccineByVacCode, getVaccinationRecordById, isInputInt, saveVaccinationRecord


def vacAdmin(patientList, vaccineList, vaccinationRecordList):
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
        
        # prompt user for dose number
        isValid = False
        while not isValid:
            doseNumber = input('Please enter dose number [D1 or D2]: ')
            # validation
            doseNumber = doseNumber.upper()
            if doseNumber != 'D1' and doseNumber != 'D2':
                print('Input must be either D1 or D2.')
                continue
            isValid = True
        

        # get vaccine & vaccination record
        vacCode = patient.vacSelected
        vaccine = getVaccineByVacCode(vacCode, vaccineList)
        vaccinationRecord = getVaccinationRecordById(patientId, vaccinationRecordList)
        
        dosRequired = vaccine.dosRequired
        dose1 = vaccinationRecord.dose1
        
        # Update vaccination record
        # D1 cases
        if doseNumber == 'D1':
            if dose1 == 'COMPLETED':
                print('{} is completed.'.format(doseNumber))
                isComplete = True
                break
            else:
                if dosRequired > 1:
                    interval = vaccine.interval
                    print('Please come again in {} weeks.'.format(interval))
                
                vaccinationRecord.dose1 = 'COMPLETED'

        # D2 cases
        if doseNumber == 'D2':
            dose2 = vaccinationRecord.dose2

            if dose2 == 'COMPLETED':
                print('{} is completed.'.format(doseNumber))
                isComplete = True
                break
            else:
                if dosRequired < 2:
                    print('2nd dose is not required for {}.'.format(vacCode))
                    isComplete = True
                    break
                if dose1 == 'INCOMPLETE':
                    print('Please take the 1st dose.')
                    isComplete = True
                    break

                vaccinationRecord.dose2 = 'COMPLETED'
        
        # Save vaccination record
        saveVaccinationRecord(vaccinationRecord)

        print('{} for {} has been administered.'.format(doseNumber, vacCode))
        isComplete = True
        return [patientId, vaccinationRecord]