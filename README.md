# JupyterNotebook環境構築

## アジェンダ

* Macへの環境インストール


## 手順

1. brewインストール
1. pyenvインストール 
```
brew install pyenv
brew install pyenv-virtualenv
vi ~/.bashrc # 
source ~/.bashrc
```
1. Pythonインストール
```
pyenv install 3.7.0
pyenv global 3.7.0
pyenv rehash
```
1. Anacondaセットアップ
```
pyenv install anaconda3-5.2.0
pyenv global anaconda3-5.2.0
conda create --name py3.7.0 python=3.7.0
pyenv local anaconda3-5.2.0/envs/py3.7.0
pyenv global system
source $PYENV_ROOT/versions/anaconda3-5.2.0
```
1. Jupyter Notebookインストール
```
pip install jupyter
pip install "ipython[notebook]"
pip install pandas #  numpy
pip install matplotlib # matplotlib.
pip freeze > requirements.txt # pip install -r requirements.txt でインストールできるように。

```
1. pipのアップグレード（警告が表示される場合）
```
pip install --upgrade pip
```
1. 学習用のリポジトリを作成(Github作業)
```
Githubのページを開く->リポジトリ作成 ->
```
1. 学習用のリポジトリを作成(PC作業)
```
git clone git@github.com:Eigo-Mt-Fuji/aiml-training.git
cd aiml-training/
```
1. Jupyter Notebook起動
```
jupyer-notebook  # http://localhost:8888/がブラウザにて起動されることを確認
```


