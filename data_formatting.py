def data_formatting(data):
    if not data['MonthlyIncome']:
        data['MonthlyIncome'] = 0
    if data['DebtRatio'] > 5:  
        data['DebtAbsolute'] = data['DebtRatio']
    else:
        data['DebtAbsolute'] = data['DebtRatio'] * data['MonthlyIncome']
    data['MonthlyBalance'] = data['MonthlyIncome'] - data['DebtAbsolute']
    data['BalancePerPerson'] = data['MonthlyBalance']/(data['NumberOfDependents']+1)
    return data