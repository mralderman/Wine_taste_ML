import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error

def main():
    df = pd.read_csv('winequality-white.csv',sep=';')
    #print(df.head)
    X = df.drop('quality', axis=1)
    y=df['quality']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, shuffle = True)


    

if __name__ == '__main__':
    main()