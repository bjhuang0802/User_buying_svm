"""

========================================
SVM for product-buying prediction
========================================

"""
print(__doc__)

import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm
from sklearn.metrics import roc_curve, auc
from sklearn.externals import joblib
import pickle
import timeit
import data
start = timeit.default_timer()


fp = open('time_log.txt','a+')
fp1= open('general_log.txt','a+')

x0=[]
y0=[]
f=[]
x0,y0,f=data.data(0.05)
print 'Data is loaded. Use %d features for each uniq clientId.' %(len(x0[0]))
print >>fp1,'Data is loaded. Use %d features for each uniq clientId.' %(len(x0[0]))
for i in range(0,len(f)):
    print '%d. %s' %(i,f[i])
    print >>fp1,'%d. %s' %(i,f[i])
print ''
X=np.array(x0)
y=np.array(y0)
n_sample = len(X)
np.random.seed(0)
order = np.random.permutation(n_sample)
X = X[order]
y = y[order].astype(np.float)
s=int(8)
div=int(n_sample/10*s)
X_train = X[:div]
y_train = y[:div]
X_test = X[div:]
y_test = y[div:]
print 'There are %d samples.' %(n_sample)
print 'Prepare train(%d percentage) and test(%d percentage) sample: %d, %d' %(s*10,(10-s)*10,len(X_train),len(X_test))
print >>fp1,'There are %d samples.' %(n_sample)
print >>fp1,'Prepare train(%d percentage) and test(%d percentage) sample: %d, %d' %(s*10,(10-s)*10,len(X_train),len(X_test))
# fit the model
#for fig_num, kernel in enumerate(('linear', 'rbf', 'poly')):
for fig_num, kernel in enumerate(('linear', 'rbf')):
    clf = svm.SVC(kernel=kernel, gamma=1,probability=True)
    probas_ = clf.fit(X_train, y_train).predict_proba(X_test)
    fpr, tpr, thresholds = roc_curve(y_test, probas_[:, 1],pos_label=2)
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, lw=1, label='ROC (area = %0.2f)' % ( roc_auc))

    name=kernel
    joblib.dump(clf, 'model/svm_'+name+'.pkl') 
    strain =clf.score(X_train, y_train)
    stest  =clf.score(X_test,  y_test)
    print 'Kernel:%s, Accuracy(Train,Test):%6.2f,%6.2f, AUC:%6.2f' %(kernel,strain, stest,roc_auc)
    print >>fp, 'Train set:%s,%6.2f' %(kernel, strain)
    print >>fp1,'Kernel:%s, Accuracy(Train,Test):%6.2f,%6.2f, AUC:%6.2f' %(kernel,strain, stest,roc_auc)
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example '+kernel)
    plt.legend(loc="lower right")
    plt.show()

stop = timeit.default_timer()
ds = stop -start
dm = ds/60.0
print ''
print '%d samples, time cost: %8.2f (mins)/ %8d (sec)' %(n_sample,dm,ds)
print >>fp,'%d,%8d,%8.2f' %(n_sample,ds,dm)
print >>fp1,'%d samples, time cost: %8.2f (mins)/ %8d (sec)' %(n_sample,dm,ds)
print >>fp1, '-----------------'
