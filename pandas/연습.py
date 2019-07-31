import pandas as pd
import numpy as np
np.random.seed(33)
df_score1 = pd.DataFrame(np.random.randint(50, 100, size =(5, 3)))
print(df_score1)

df_score1.index = ['하영','선우','용후','세영','희택']
df_score1.columns = ['국어','수학','영어']
print(df_score1)

df_score2 = df_score1.reset_index()
print(df_score2)
