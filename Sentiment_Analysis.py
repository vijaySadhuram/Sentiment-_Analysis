Import	pandas	as	Pd
Import	numpy	as	Np
df=pd.read_csv('deceptive-opinion.csv')
df['text']
df.info()
df['hotel'].unique()