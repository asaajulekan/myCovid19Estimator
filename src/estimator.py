def estimator(data):
  return data
data={
    "region": {
    "name": "Africa",
    "avgAge": 19.7,
    "avgDailyIncomeInUSD": 5,
    "avgDailyIncomePopulation": 0.71
    },
    "periodType": "days",
    "timeToElapse": 58,
    "reportedCases": 674,
    "population": 66622705,
    "totalHospitalBeds": 1380614}
def normalize(data):
    if data.get('periodType') == 'days':
        return data.get('timeToElapse')
    if data.get('periodType') == 'weeks':
        return data.get('timeToElapse')*7

    if data.get('periodType') == 'months':
        return data.get('timeToElapse')*30
    result = {'data':data, 'impact':{}, 'severimpact':{}}
    result['impact']['currentlyInfected'] = data['reportedCases'] *10
    result['severeImpact']['currentlyInfected'] = data['reportedCases'] *50

    return result
print(estimator(data))
