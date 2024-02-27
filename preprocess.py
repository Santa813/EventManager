import pandas as pd

data= pd.read_csv(r"C:\Users\Swift3\Documents\EventManager\Data\Ideathon-Registration.csv")

def preprocess_df(df, value_name, addcols):
    names = ['Leader', 'Participant - 1', 'Participant - 2', 'Participant - 3']
    # remove useless columns
    df.drop(['Floor', 'Phone Number', 'Signature'], axis=1, inplace=True)

    # melt the dataframe to have names in one columns
    df = pd.melt(df,
                 id_vars='Team Names',
                 value_vars=names,
                 var_name='Post',
                 value_name=value_name)
    
    df.dropna(axis=0, inplace=True)

    df.insert(3,addcols[0],'')
    df.insert(3,addcols[1],'')
    df.insert(3,addcols[2],'')
    df.insert(3,addcols[3],'')

    # df.apply(lambda x: x.astype(str).str.lower())

    for columns in df.columns:
        df[columns] = df[columns].str.lower()
        df[columns] = df[columns].str.strip()

    df.sort_values(by= ['Team Names', 'Post'],ascending= True, inplace = True)
    return df

data=preprocess_df(data,'Participants',['Snacks','Lunch','Breakfast','Goodies'])

data.to_csv(r"C:\Users\Swift3\Documents\EventManager\Data\Data.csv", index=False)