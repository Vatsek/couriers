def filter(dataFrame):
    dataFrame = dataFrame.drop_duplicates(['Номер ЗК'])
    dataFrame = dataFrame.loc[dataFrame['ФИО курьера'].isin(['Брагин Антон Владимирович', 'Малышев Станислав Борисович', 'Круглов Сергей Анатольевич'])]
    dataFrame = dataFrame.groupby(['Дата выполнения ЗК','ФИО курьера']).size()
    return dataFrame