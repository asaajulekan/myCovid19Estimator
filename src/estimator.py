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
    output={'data': data, "impact": {}, "severeImpact": {}}
    days=normalize(data)
    output['impact']['currentlyInfected']=data['reportedCases'] * 10
    output['severeImpact']['currentlyInfected']=data['reportedCases'] * 50

    # infection by requested time
    output['impact']['infectionsByRequestedTime']=int(
    output['impact']['currentlyInfected'] * (2 ** int(days / 3)))
    output['severeImpact']['infectionsByRequestedTime']=int(
    output['severeImpact']['currentlyInfected'] * (2 ** int(days / 3)))

    # Severe cases by requested time
    output['impact']['severeCasesByRequestedTime']=int( 
        0.15 * output['impact']['infectionsByRequestedTime'])
    output['severeImpact']['severeCasesByRequestedTime']=int(
    0.15 * output['severeImpact']['infectionsByRequestedTime'])

    # Hospital beds by requested time
    output['impact']['hospitalBedsByRequestedTime']=int((0.35 * data['totalHospitalBeds'])
    - output['impact']['severeCasesByRequestedTime'])
    output['severeImpact']['hospitalBedsByRequestedTime']=int((0.35 * data['totalHospitalBeds'])
    - output['severeImpact']['severeCasesByRequestedTime'])

    # Cases for ICU by requested time
    output['impact']['casesForICUByRequestedTime']=int(
    0.05 * output['impact']['infectionsByRequestedTime'])
    output['severeImpact']['casesForICUByRequestedTime']=int(
    0.05 * output['severeImpact']['infectionsByRequestedTime'])

    # Cases for ventilators by requested time
    output['impact']['casesForVentilatorsByRequestedTime']=int(
    0.02 * output['impact']['infectionsByRequestedTime'])
    output['severeImpact']['casesForVentilatorsByRequestedTime']=int(
    0.02 * output['severeImpact']['infectionsByRequestedTime'])

    # Dollars in flight 
    output['impact']['dollarsInFlight']=int((output['impact']['infectionsByRequestedTime']
    * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) / days)
    output['severeImpact']['dollarsInFlight']=int((output['severeImpact']['infectionsByRequestedTime']
    * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) / days)

    return output
