# このリポジトリについて
ソースコードの変更に基づいて全自動でドキュメントを生成することを目的としたリポジトリ

# 使い方
必要なものは以下の二点のみ。
* Workflow file
```.github\workflows\sphinx_workflow.yml```
* 自動ビルドに必要な設定など
```.\sphinx_setupkit```

今回はGithub Action上で動作確認できるようにソースコードを用意。

## 0. sphinxの設定を確認する
```.\sphinx_setupkit\sphinx_settings.json```の設定を確認する。
必要に応じて```.\templates```内のjinjaファイルの設定を行う。
詳細は公式のtemplatesを参照。
※正直仕様は知り尽くせていないので良く読み込んでおきたいところ
* https://www.sphinx-doc.org/ja/master/man/sphinx-apidoc.html
* https://sphinx-jinja2.readthedocs.io/en/latest/

## 1. ソースコードをPushだけ
ユーザーは自身のプログラムを同封したもとでリモートにPushするのみ。GithubAction上で```sphinx_setupkit\sphinx_settings.json```の設定に基づき```sphinx_apidoc```コマンドによりファイル構成が作成され、直後にビルドが走り、その後ドキュメントのアップロードまでが自動で処理される

## 2. アップロードリンク：
ドキュメントは以下URLで確認できる
https://wassawa1.github.io/SPHINX_GITHUB_ACTIONS/


