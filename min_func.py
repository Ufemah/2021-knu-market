def train(i, j, k, data, number_of_predictions):
    model = ARIMA(data, order=(i, j, k))
    model_fit = model.fit()
    arima = []
    # make prediction
    for x in range(number_of_predictions):
        arima_prediction = model_fit.predict(len(data) + x, len(data) + x)
        arima.append(arima_prediction)
    return arima


def min_func(ideal, new_pred, i, j, k, min_count, min_summ_array,length):
    new_count = 0
    for c in range(length, length+len(ideal)):
        new_count += math.sqrt(((ideal[c] - new_pred[c])**2))
    if new_count - min_count > 0:
        pass
    elif new_count - min_count < 0:
        f = open("res.txt", 'a')
        f.write("configuration:{0}{1}{2} better than previous; new_count = {3} \n".format(i,j,k,new_count))
        f.close()
        min_summ_array = new_pred
        min_count = new_count
    elif new_count - min_count == 0:
        f = open("res.txt", 'a')
        f.write("configuration:{0}{1}{2} equal to the previous one \n".format(i,j,k))
        f.close()



if __name__ == '__main__':
    min_summ_array = []
    min_count = 100000000000000
    import pandas as pd
    import math
    from statsmodels.tsa.arima.model import ARIMA
    df = pd.read_csv('data/[1h]BTCUSDT.csv')
    train_set = df["Close"][0:math.floor(0.75*len(df["Close"]))]
    ideal = df["Close"][math.floor(0.75*len(df["Close"])):len(df["Close"])]
    for i in range(len(train_set)):
        for j in range(len(train_set)):
            for k in range(len(train_set)):
                arima_i = train(i, j, k, train_set, len(ideal))
                min_func(ideal, arima_i, i, j, k,min_count,min_summ_array,len(train_set))
    print(min_summ_array,min_count)
