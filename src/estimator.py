data = {"region": {
    "name": "Africa",
    'avgAge': 19.7,
    'avgDailyIncomeInUSD': 5,
    'avgDailyIncomePopulation': 0.71
    },
    'periodType': "days",
    'timeToElapse': 58,
    'reportedCases': 674,
    'population': 66622705,
    'totalHospitalBeds': 1380614
}
# Normalization of days
def normalize(data):

  if data.get('periodType') == 'days':
    return data.get('timeToElapse')
  if data.get('periodType') == 'weeks':
    return data.get('timeToElapse') * 7
  if data.get('periodType') == 'months':
    return data.get('timeToElapse') * 30
# The estimator
def estimator(data):
    result={'data': data, "impact": {}, "severeImpact": {}}
    days=normalize(data)
    result['impact']['currentlyInfected']=data['reportedCases'] * 10
    result['severeImpact']['currentlyInfected']=data['reportedCases'] * 50

    # infection by requested time
    result['impact']['infectionsByRequestedTime']=int(
    result['impact']['currentlyInfected'] * (2 ** int(days / 3)))
    result['severeImpact']['infectionsByRequestedTime']=int(
    result['severeImpact']['currentlyInfected'] * (2 ** int(days / 3)))

    # Severe cases by requested time
    result['severeImpact']['severeCasesByRequestedTime']=int( \
        0.15 * result['severeImpact']['infectionsByRequestedTime'])
    result['severeImpact']['severeCasesByRequestedTime']=int(
    0.15 * result['severeImpact']['infectionsByRequestedTime'])

    # Hospital beds by requested time
    result['severeImpact']['hospitalBedsByRequestedTime']=int((0.35 * data['totalHospitalBeds'])
    - result['severeImpact']['severeCasesByRequestedTime'])
    result['severeImpact']['hospitalBedsByRequestedTime']=int((0.35 * data['totalHospitalBeds'])
    - result['severeImpact']['severeCasesByRequestedTime'])

    # Cases for ICU by requested time
    result['severeImpact']['casesForICUByRequestedTime']=int(
    0.05 * result['severeImpact']['infectionsByRequestedTime'])
    result['severeImpact']['casesForICUByRequestedTime']=int(
    0.05 * result['severeImpact']['infectionsByRequestedTime'])

    # Cases for ventilators by requested time
    result['severeImpact']['casesForVentilatorsByRequestedTime']=int(
    0.02 * result['severeImpact']['infectionsByRequestedTime'])
    result['severeImpact']['casesForVentilatorsByRequestedTime']=int(
    0.02 * result['severeImpact']['infectionsByRequestedTime'])

    # Dollars in flight
    result['severeImpact']['dollarsInFlight']=int((result['severeImpact']['infectionsByRequestedTime']
    * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) / days)
    result['severeImpact']['dollarsInFlight']=int((result['severeImpact']['infectionsByRequestedTime']
    * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) / days)


    return result