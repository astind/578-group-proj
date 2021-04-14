
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn import preprocessing


# steps needed to build a data model
# 1. Load Data
# 2.Analyze for income groups
# 3. Clean and prepare data
# 4. normalization through scaling
# 5. transform categorical features
# 6. find correlation of features and rid of irrelevant
# 7. Performance Evaluation through test data
# 8. Prediction algorithms: scikit-learn: decision trees
# 9 optimize the model and measure accuracy and F-score

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def main():
    print_hi("")


if __name__ == '__main__':
    main()
    df = pd.read_csv("adult.csv", delimiter=', ' , header=None, names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship',
                                           'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country','income'])


    #Dimensionality of DataFrame
    n_records = df.shape[0]
    print("Total number of records: {}".format(n_records))
    n_greater_50k = df[df['income'] == ">50K"].shape[0]
    print("Total number of records >50k: {}".format(n_greater_50k))

    #Explore the data
    print(df.describe())
    print(df.groupby('capital-loss').size())

    #remove spaces in column names
    df.columns = df.columns.str.replace(' ','')
    df = df.drop('education-num',axis=1)
    df = df.drop('fnlwgt',axis=1)
    #drop occupation where unknown
    df = df[df.occupation != '?']
    df = df.drop_duplicates(keep='first')

    #Find any Null Values
    print(df.isnull().sum(axis=0))

    #Prints unique counts
    #print(df['occupation'].value_counts())
    #print(df['capital-loss'].value_counts())
    #print(df['income'].value_counts())

    #convert categorical data into numerical values
    for col_name in df.columns:
        if (df[col_name].dtype == 'object'):
            df[col_name] = df[col_name].astype('category')
            df[col_name] = df[col_name].cat.codes

    #Normalize the data
    #values now between 0 and 1
    d = preprocessing.normalize(df,axis=0)
    scaled_df = pd.DataFrame(d,columns=df.columns)

    data_normalized = preprocessing.normalize(df, norm='l1')

    #Pearson correlation , we can compare numerical columns
    print("Pearson Correlation:")
    print(data_normalized.corr(method='pearson'))

    print("Kendall Correlation: ")
    print(scaled_df.corr(method='kendall'))

    #data_normalized = preprocessing.normalize(df, norm='l1')
    #print ("\nL1 normalized data = ", data_normalized)
    # plot variables against eachother
    #df.plot.scatter(x='age', y='income')
    #plt.show(block=True)

    #df.plot.scatter(x='education-num', y='income')
    #plt.show(block=True)

    #df.plot.scatter(x='sex', y='income')
    #plt.show(block=True)

    scaled_df.plot.scatter(x='capital-gain', y='income')
    plt.show(block=True)

    scaled_df.plot.scatter(x='capital-loss', y='income')
    plt.show(block=True)

    df.hist(column='capital-gain', by='income')
    plt.suptitle("Capital Gain Histogram")
    plt.title(">50k")
    plt.show()

    df.hist(column='capital-loss', by='income')
    plt.suptitle("Capital Loss Histogram")
    plt.title(">50k")
    plt.show()

    #df.plot.scatter(x='hours-per-week', y='income')
    #plt.show(block=True)

    #df.plot.scatter(x='occupation', y='income')
    #plt.show(block=True)

    #df.plot.scatter(x='race', y='income')
    #plt.show(block=True)

    #df.plot.scatter(x='education', y='income')
   # plt.show(block=True)

    #colormap to show correlation
    corr = scaled_df.corr()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
    fig.colorbar(cax)
    ticks = np.arange(0, len(scaled_df.columns), 1)
    ax.set_xticks(ticks)
    plt.xticks(rotation=90)
    ax.set_yticks(ticks)
    ax.set_xticklabels(scaled_df.columns)
    ax.set_yticklabels(scaled_df.columns)
    plt.show()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
