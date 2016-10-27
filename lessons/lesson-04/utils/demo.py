from plotly.offline import init_notebook_mode, iplot
import plotly.tools as tls
import cufflinks as cf
import numpy as np
import pandas as pd

init_notebook_mode()
cf.go_offline()

import warnings
warnings.filterwarnings('ignore')

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def lin_reg(X_train, y_train, X_test, y_test, graph=True, normalize=False):
    regr = LinearRegression(normalize=normalize)
    regr.fit(X_train, y_train)
    predictions = regr.predict(X_test)

    # Graphing with Plotly via Cufflinks
    if graph:
        df = pd.concat([X_test, y_test],axis=1,)
        df.columns = ['X','y']
        df.set_index('y').iplot(
            mode="markers",
            title="Estimation with LinearRegression",
            bestfit=True,
            colors=['#F7CD94'],
            bestfit_colors=['#F794AA'],
            error_type='data')
    
    mse = mean_squared_error(y_test, predictions)
    print('Mean Squared Error: {:.2}'.format(mse))
    print('Root Mean Squared Error: {:.2}'.format(np.sqrt(mse)))
    print('Variance Score: {:.2}'.format(regr.score(X_test, y_test)))
    print('Coefficients:', regr.coef_)
    
    return regr

def rules(clf, features, labels, node_index=0):
    """Structure of rules in a fit decision tree classifier

    Parameters
    ----------
    clf : DecisionTreeClassifier
        A tree that has already been fit.

    features, labels : lists of str
        The names of the features and labels, respectively.

    """
    node = {}
    if clf.tree_.children_left[node_index] == -1:  # indicates leaf
        count_labels = zip(clf.tree_.value[node_index, 0], labels)
        node['name'] = ', '.join(('{} of {}'.format(int(count), label)
                                  for count, label in count_labels))
    else:
        feature = features[clf.tree_.feature[node_index]]
        threshold = clf.tree_.threshold[node_index]
        node['name'] = '{} > {}'.format(feature, threshold)
        left_index = clf.tree_.children_left[node_index]
        right_index = clf.tree_.children_right[node_index]
        node['children'] = [rules(clf, features, labels, right_index),
                            rules(clf, features, labels, left_index)]
    return node

import json
from IPython.display import IFrame
    
def graph_tree(dt, features, labels):
    r = rules(dt, features, labels)
    with open('utils/structure.json', 'w') as f:
        f.write(json.dumps(r))
    return IFrame('utils/d3-tree.html', width='100%', height=350)