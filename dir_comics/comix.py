import pandas as pd

df = pd.read_csv('./data/export_comics.csv')

print(df['Tags'])

df['Bag'] = ''

df['Mylite'] = ''

df['Mylar'] = ''

df['Board'] = ''

df['Box'] = ''

print(df)

for i in range(0, len(df)):

    tags = df.iloc[i]['Tags']

    #print tags

    if isinstance(tags, (int, float)):

        print tags

    else:

        labels = tags.split(", ")

        for label in labels:

            if (label == 'Bag'):

                df['Bag'][i] = 'Bag'

print(df['Bag'])

#    print df.iloc[i]['c1'], df.iloc[i]['c2']


for row in df['Tags']:

    if isinstance(row, (int, float)):

        print(row)

    else:

        result = df[row]

        p = df.index.get_loc(result.index[0])

        print(p)

        tags = row.split(", ")

        for tag in tags:

            if (tag == 'Bag'):

                df['Bag'][1] = 'Bag'

                print(df)


#print(df.index)

#print(len(df.index))

#len_df = len(df.index)

#print(df['Tags'].notnull())

#print(df[df['Tags'].notnull()])



