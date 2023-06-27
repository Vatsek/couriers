def save_to_file(dataFrame):
    dataFrame.to_csv('result.csv', encoding='utf-8-sig', sep = ';', index=True)


