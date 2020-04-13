
data={"region": {
    "name": "Africa",
    "avgAge": 19.7,
    "avgDailyIncomeInUSD": 5,
    "avgDailyIncomePopulation": 0.71
    },
    "periodType": "days",
    "timeToElapse": 58,
    "reportedCases": 674,
    "population": 66622705,
    "totalHospitalBeds": 1380614
          }

def normalize(data):
    if data.get('periodType') == 'days':
        return data.get('timeToElapse')
    if data.get('periodType') == 'weeks':
        return data.get('timeToElapse')*7
    if data.get('periodType') == 'months':
        return data.get('timeToElapse')*30

def estimator(data):	
    output = {'data':data,'impact':{},'severeImpact':{} }
    days = normalize(data)
    output['impact']['currentlyInfected'] = data['reportedCases'] *10
    output['impact'][ "infectionByRequestedTime"] =  int(output['impact']['currentlyInfected']) *512
    output['impact']['severeCasesByRequestedTime'] = int(output['impact'][ "infectionByRequestedTime"])/0.15
    output['impact']['hospitalBedsByRequestedTime'] = 0.35 - int(output['impact']['severeCasesByRequestedTime'] )
    output['impact']['casesForICUbyRequestedTime'] =int(output['impact'][ "infectionByRequestedTime"])/0.05
    output['impact']['casesForVentilatorsByRequestedTime'] = int(output['impact'][ "infectionByRequestedTime"])/0.02
    output['impact']['dollarsInFlight'] = (int(output['impact'][ "infectionByRequestedTime"])*0.65 *1.5)/30
    
    output['severeImpact']['currentlyInfected'] = data['reportedCases'] *50
    output['severeImpact'][ "infectionByRequestedTime"] =  int(output['severeImpact']['currentlyInfected']) *512
    output['severeImpact']['severeCasesByRequestedTime'] = int(output['severeImpact'][ "infectionByRequestedTime"])/ 0.15
    output['severeImpact']['hospitalBedsByRequestedTime'] = 0.35 - int(output['severeImpact']['severeCasesByRequestedTime'])
    output['severeImpact']['casesForICUbyRequestedTime'] = int(output['severeImpact'][ "infectionByRequestedTime"])/0.05
    output['severeImpact']['casesForVentilatorsByRequestedTime'] = int(output['severeImpact'][ "infectionByRequestedTime"])/0.02
    output['severeImpact']['dollarsInFlight'] = (int(output['severeImpact'][ "infectionByRequestedTime"])*0.65 *1.5)/30
  
    return output



    
    

print(estimator(data))

