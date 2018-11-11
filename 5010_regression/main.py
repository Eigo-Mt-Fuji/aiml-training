import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import model_selection
# 必要なモジュールを追記してください。
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
import time 
def plot_data(concrete_data):
        
    predict_target_column = 'Concrete compressive strength(MPa, megapascals) '
    concrete_data.plot.scatter(x='Cement (component 1)(kg in a m^3 mixture)', y=predict_target_column, c='Green')
    concrete_data.plot.scatter(x='Blast Furnace Slag (component 2)(kg in a m^3 mixture)', y=predict_target_column, c='Green')
    concrete_data.plot.scatter(x='Fly Ash (component 3)(kg in a m^3 mixture)', y=predict_target_column, c='Green')
    concrete_data.plot.scatter(x='Water  (component 4)(kg in a m^3 mixture)', y=predict_target_column, c='Green')
    concrete_data.plot.scatter(x='Superplasticizer (component 5)(kg in a m^3 mixture)', y=predict_target_column, c='Green')
    concrete_data.plot.scatter(x='Coarse Aggregate  (component 6)(kg in a m^3 mixture)', y=predict_target_column, c='Green')
    concrete_data.plot.scatter(x='Fine Aggregate (component 7)(kg in a m^3 mixture)', y=predict_target_column, c='Green')
    concrete_data.plot.scatter(x='Age (day)', y=predict_target_column, c='Green')

def save_predict_data(model_name, test_data, answer_correct, answer_predict):
    data = test_data.copy()
    data['Strength(MPa) '] = answer_correct
    data['Strength(MPa)  - Predict'] = pd.Series(answer_predict, index=answer_correct.index)
    
    predict_data_path = 'Concrete_Data_%s.xlsx' % (model_name)
    writer = pd.ExcelWriter(predict_data_path)
    data.to_excel(writer,'Sheet1')
    writer.save()
    return predict_data_path
def make_analyze_response(model_name, concrete_test_X, concrete_test_y, result, score):
    predict_data_path = save_predict_data(model_name, concrete_test_X, concrete_test_y, result)
    print("[%s] score: %s, predict: %s" % (model_name, score, predict_data_path))
    
    return {
        "model": model_name,
        "score":  score,
        "predict_data_path": predict_data_path
    }
def analyze_Lasso(concrete_train_X, concrete_test_X, concrete_train_y, concrete_test_y):
    model = Lasso()
    model.fit(concrete_train_X, concrete_train_y)
    predict = model.predict(concrete_test_X)
    score = model.score(concrete_test_X, concrete_test_y)
    return make_analyze_response("Lasso", concrete_test_X, concrete_test_y, predict, score)
def analyze_Ridge(concrete_train_X, concrete_test_X, concrete_train_y, concrete_test_y):
    model = Ridge()
    model.fit(concrete_train_X, concrete_train_y)
    predict = model.predict(concrete_test_X)
    score = model.score(concrete_test_X, concrete_test_y)
    return make_analyze_response("Ridge", concrete_test_X, concrete_test_y, predict, score)
def analyze_LinearRegression(concrete_train_X, concrete_test_X, concrete_train_y, concrete_test_y):
    model = LinearRegression(normalize=True)
    model.fit(concrete_train_X, concrete_train_y)
    
    predict = model.predict(concrete_test_X)
    score = model.score(concrete_test_X, concrete_test_y)
    return make_analyze_response("LinearRegression", concrete_test_X, concrete_test_y, predict, score)
def analyze_ElasticNet(l1_ratio, concrete_train_X, concrete_test_X, concrete_train_y, concrete_test_y):
    model = ElasticNet(l1_ratio=l1_ratio)
    model.fit(concrete_train_X, concrete_train_y)
    
    predict = model.predict(concrete_test_X)
    score = model.score(concrete_test_X, concrete_test_y)
    return make_analyze_response("ElasticNet L1_RATIO_%s" % (l1_ratio), concrete_test_X, concrete_test_y, predict, score)
def cross_validate_LinearRegression(X, y):
    test_model = LinearRegression(normalize=True)
    scores = model_selection.cross_val_score(test_model, X, y, cv=10)
    print (scores)
    print ("平均スコア :", scores.mean())
def cross_validate_Lasso(X, y):
    test_model = Lasso()
    scores = model_selection.cross_val_score(test_model, X, y, cv=100)
    print (scores)
    print ("平均スコア :", scores.mean())
# データの読み込み
concrete_data = pd.read_excel("https://archive.ics.uci.edu/ml/machine-learning-databases/concrete/compressive/Concrete_Data.xls")
# データ可視化
# plot_data(concrete_data)
X = concrete_data.drop(['Concrete compressive strength(MPa, megapascals) ', ], axis=1)
y = concrete_data['Concrete compressive strength(MPa, megapascals) ']
concrete_train_X, concrete_test_X, concrete_train_y, concrete_test_y = train_test_split(
    X,
    y,
    random_state=int(time.time()))
# 交差検証
cross_validate_LinearRegression(X, y)
cross_validate_Lasso(X, y)
# 以下にコードを記述してください。
results = []
## 解析 - 線形重回帰
results.append(analyze_LinearRegression(concrete_train_X, concrete_test_X, concrete_train_y, concrete_test_y))
results.append(analyze_Lasso(concrete_train_X, concrete_test_X, concrete_train_y, concrete_test_y))
results.append(analyze_Ridge(concrete_train_X, concrete_test_X, concrete_train_y, concrete_test_y))
# Lidge + Lasso ratio
results.append(analyze_ElasticNet(0.1, concrete_train_X, concrete_test_X, concrete_train_y, concrete_test_y))
results.append(analyze_ElasticNet(0.3, concrete_train_X, concrete_test_X, concrete_train_y, concrete_test_y))
results.append(analyze_ElasticNet(0.5, concrete_train_X, concrete_test_X, concrete_train_y, concrete_test_y))
results.append(analyze_ElasticNet(0.7, concrete_train_X, concrete_test_X, concrete_train_y, concrete_test_y))
results.append(analyze_ElasticNet(0.9, concrete_train_X, concrete_test_X, concrete_train_y, concrete_test_y))
# 一番いい結果を出力
df = pd.DataFrame.from_records(results, columns=["score", "model", "predict_data_path"])
best = df.loc[ df['score'].idxmax()]
print ("一番いい結果: %s" % (best))

