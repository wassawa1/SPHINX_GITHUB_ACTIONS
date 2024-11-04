# JSON設定ファイルを読み込んで変換
$json = (Get-Content "sphinx_settings.json" | ConvertFrom-Json)

# sphinx-apidoc コマンドを実行
sphinx-apidoc -F -o "./docs" -A $json.author -H $json.project $json.source_dir 
