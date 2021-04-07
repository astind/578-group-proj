
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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
    print_hi('PyCharm')
    main()
    df = pd.read_csv("adult.csv", delimiter=', ' , header=None, names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship',
                                           'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country','income'])
    #print(df.head())
    #print(df.columns)

    #Dimensionality of DataFrame
    n_records = df.shape[0]
    print("Total number of records: {}".format(n_records))
    print(df[df['income'] == "<=50K"])
    n_greater_50k = df[df['income'] == ">50K"].shape[0]
    print("Total number of records >50k: {}".format(n_greater_50k))

    for col_name in df.columns:
        if (df[col_name].dtype == 'object'):
            df[col_name] = df[col_name].astype('category')
            df[col_name] = df[col_name].cat.codes


    #Pearson correlation , we can compare numerical columns
    print("Pearson Correlation:")
    print(df.corr(method='pearson'))

    print("Kendall Correlation: ")
    print(df.corr(method='kendall'))

    # plot variables against eachother
    df.plot.scatter(x='age', y='income')
    plt.show(block=True)

    #colormap to show correlation
    corr = df.corr()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
    fig.colorbar(cax)
    ticks = np.arange(0, len(df.columns), 1)
    ax.set_xticks(ticks)
    plt.xticks(rotation=90)
    ax.set_yticks(ticks)
    ax.set_xticklabels(df.columns)
    ax.set_yticklabels(df.columns)
    plt.show()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
