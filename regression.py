
import matplotlib.pyplot as plt
import quandl
import math
import numpy as np
import datetime
import pandas as pd
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
from matplotlib import style
style.use("ggplot")

df = quandl.get("WIKI/GOOGL")
df = df[['Adj. Close']]

forecast_col = "Adj. Close"
df.fillna(value=-99999, inplace=True)
forecast_out = int(math.ceil(0.01 * len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)

X = np.array(df.drop(["label"], 1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]
df.dropna(inplace=True)

y = np.array(df['label'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(
    X, y, test_size=0.2)

clf = LinearRegression(n_jobs=1)
# clf = svm.SVR()
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
y_pre_predict = clf.predict(X)
y_post_predict = clf.predict(X_lately)

df["forecast"] = np.nan
first_date = df.iloc[-1].name
last_unix = first_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

i = 0
date_pre_predict = []
while(i < len(X)):
    date = df.iloc[i].name.timestamp()
    date = datetime.datetime.fromtimestamp(date)

    date_pre_predict.append(date)
    i = i + 1

pre_predict_df = pd.DataFrame(
    {'Date': date_pre_predict, 'forecast': y_pre_predict})

pre_predict_df = pre_predict_df.set_index("Date")

for i in y_post_predict:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns) - 1)] + [i]


print(pre_predict_df)
print(df)
df['Adj. Close'].plot()
pre_predict_df["forecast"].plot(label="pre_forecast")
df['forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
