# Check if vaccination is complete
# vaccinationRecord -> VaccinationRecord
# returns boolean
def isVaccinationComplete(vaccinationRecord):
    if vaccinationRecord.dose2 != '-':
        if vaccinationRecord.dose2 == 'COMPLETED':
            return True
    else:
        if vaccinationRecord.dose1 == 'COMPLETED':
            return True

    return False


def statsInfo(patientList, vaccinationRecordList, vcList):
    vc1Waiting = 0
    vc1Completed = 0
    vc2Waiting = 0
    vc2Completed = 0

    # Calculate waiting & completed for each VC
    for patient in patientList:
        patientId = patient.id
        vacCentre = patient.vacCentre
        vaccinationRecord = vaccinationRecordList[patientId]
        
        if vacCentre == vcList[0]:
            if isVaccinationComplete(vaccinationRecord):
                vc1Completed += 1
            else:
                vc1Waiting += 1
                

        if vacCentre == vcList[1]:
            if isVaccinationComplete(vaccinationRecord):
                vc2Completed += 1
            else:
                vc2Waiting += 1
    
    # print results
    print("{:<30} | {:<3}".format(vcList[0], vcList[1]))
    print("{:<18} | {:<9} | {:<18} | {:<9}".format('Waiting for Dose 2', 'Completed', 'Waiting for Dose 2', 'Completed'))
    print("{:<18} | {:<9} | {:<18} | {:<9}".format(vc1Waiting, vc1Completed, vc2Waiting, vc2Completed))