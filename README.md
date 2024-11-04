# このリポジトリの目的
ソースコードの変更に基づいて全自動でドキュメントを生成することを目指したリポジトリ


# 使い方
現状全自動にはなっていない。現状のフローを紹介。

## 1. ```./docs```を強制削除し、ディレクトリを再構成(手動)


```powershell
Remove-Item -Recurse -Force docs
.\generate_sphinx_docs.ps1
```


## 2. ```./docs/conf.py```の編集(手動)

**```conf.py```に対して以下の二か所の記述を追加する**
*  ```./docs```よりも一階層上のソースコードにもパスが通るよう、以下の記述を頭に追加

```python
# ==ここを追加=================================
import os
import sys
sys.path.insert(0, os.path.abspath('../'))
# ============================================
```

* extensionsに以下の二項目を追加
```python
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
]
```

* お好みで以下のスタイルに変更
```python
html_theme = 'sphinx_rtd_theme' # お好みでデザインを変えてもOK
```

<!-- TODO:ここも自動化を目指す。```./docs/conf.py```のtemplates利用方法の習得が課題。 -->

## 3. Pushする
Pushすれば勝手にビルドが走り、作成されたドキュメントがアップロードされるはず。

1. アップロードリンク：
https://wassawa1.github.io/SPHINX_GITHUB_ACTIONS/


