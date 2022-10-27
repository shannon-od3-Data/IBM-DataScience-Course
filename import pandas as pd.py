
# os.path.join('Users', 'shann', 'Desktop', 'Vases', 'Files','data')
# fullPath = "\Users\shann\Desktop\Vases\Files\data\AllAthenianWImages.csv"
# files2Load = ['.csv','.csv']
# for filename in files2Load fp = p + fl
# pd.read_csv()

import pandas as pd
import os

test_df = pd.read_csv('C:\Users\shann\Desktop\Vases\Files\data\AllAthenianWImages.csv', nrows=100)
print("Dataframe shape:", test_df.shape)