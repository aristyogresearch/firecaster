import logging
import pandas as pd
import numpy as np
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.model_selection import cross_validate
from collections import Counter
import cPickle


class DataAnalyzer():
    """
        DataAnalyzer class to perform analysis on a given dataset

    """

    def __init__(self, data_fname=None):
        """
        Initialize the class with path to data file
        """
        self.data_fname = data_fname

    def load_data(self, data_fname):
        """
        load the data using Pandas

        :param data_fname: path to data file
        :type data_fname: :py:class:`str`

        :return: DataFrame with separated columns
        """
        df = pd.read_csv(data_fname, index_col=False, sep='\t')
        self.data_fname = data_fname

        return df

    def load_samples(self, df, features, target):
        """
        load X and Y

        :param df: dataframe
        :type df: :py:class:`pandas.DataFrame`

        :param features: a list of features
        :type  features: :py:class:`list`

        :param target: a list of one target name
        :type  target: :py:class:`list`

        :return: X, y
        """

        X = df[features]
        y = df[target]

        logging.info("Features: %s" % features)
        logging.info("Target: %s" % target)

        logging.info("Feature space holds %d observations and %d features" % X.shape)
        logging.info("Unique target labels: %s" % np.unique(y))

        return X, y

    def encode_labels(self, df):
        """
        encode the labels

        :param df: dataframe
        :type df: :py:class:`pandas.DataFrame`

        :return: DataFrame with separated columns
        """
        df = df.apply(LabelEncoder().fit_transform)
        return df

    def train_test_split(self, X, y, test_size=0.3):
        """
        Generate Train/Test Datasets

        :param X: a matrix x that hold features' values
        :type  X: `np.array`

        :param y: a matrix x that hold target' values
        :type  y: `np.array`

        :param test_size: a percentage to take the test
        :type  test_size: :py:class:`int`

        return X_train, X_test, y_train, y_test
        """
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

        logging.info("X_train.shape = %r", X_train.shape)
        logging.info("X_test.shape = %r", X_test.shape)
        logging.info("y_train.shape = %r", y_train.shape)
        logging.info("y_test.shape = %r", y_test.shape)

        return X_train, X_test, y_train, y_test

    def label_target(self, df, target):
        """
        label target based on some criterias 
        
        :param df: dataframe
        :type df: :py:class:`pandas.DataFrame`
        
        :param target: the name of the target
        :type  target: :py:class:`str`

        :return: DataFrame with separated columns
        """
        # df[target] = df[target].apply(lambda x: 0 if x == 0 else 1 if (x>0 and x < 10) else 2 )
        df[target] = df[target].apply(lambda x: 0 if x == 0 else 1)
        logging.info("Labels : %s" % dict(Counter(df[target].values)))

        return df

    def feature_importance(self, X, y, features):
        """
        engineer features using sklearn.feature_selection

        :param X: a matrix x that hold features' values
        :type  X: `np.array`

        :param y: a matrix x that hold target' values
        :type  y: `np.array`
        
        :param features: a list of features
        :type  features: :py:class:`list`

        """
        # feature extraction
        model = ExtraTreesClassifier()
        model.fit(X, y)
        print "Features importances: \n", sorted(zip(map(lambda x: round(x, 4), model.feature_importances_), features),
                                                 reverse=True)

    def evaluate_model(self, X, y, classifier, cv, **kwargs):
        """
        evaluate models using Cross-Validation
        
        :param X : The data to fit/train the model
        :type  X: `np.array` 

        :param y : The data to be predict so the model can learn  
        :type  y: `np.array`

        :param classifier: classifier model to classify data
        :type  classifier: sklearn.model

        :param cv: 
        :type  cv: :py:class:`int`

        :param kwargs:

        :return:
            clf: classifier
            accuracy_scores: a vector that contains the accuracy scores

        """
        clr = OneVsRestClassifier(classifier(**kwargs))

        scoring = ['accuracy', 'roc_auc', 'f1_weighted', 'precision_weighted', 'recall_weighted']

        scores = cross_validate(clr, X, y, scoring=scoring, cv=cv, return_train_score=True)

        roc_auc_scores = scores['test_roc_auc']
        accuracy_scores = scores['test_accuracy']
        f1_scores = scores['test_f1_weighted']
        precision_scores = scores['test_precision_weighted']
        recall_scores = scores['test_recall_weighted']

        logging.info("Accuracy = %r", np.mean(accuracy_scores))
        logging.info("F1 = %r", np.mean(f1_scores))
        logging.info("Precision = %r", np.mean(precision_scores))
        logging.info("Recall = %r", np.mean(recall_scores))
        logging.info("ROC AUC= %r", np.mean(roc_auc_scores))

        return clr

    def dump_model(self, clr, output):
        """
        dump the model

        :param clr: classifier model to classify data
        :type  clr: sklearn.model

        :param output: a path to export the file
        :type  output: :py:class:`str`
        """
        with open(output, 'wb') as f:
            cPickle.dump(clr, f)
