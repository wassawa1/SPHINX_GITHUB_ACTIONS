# Read data from jsonfile
$json = (Get-Content "sphinx_settings.json" | ConvertFrom-Json)

# Check if the ./docs directory exists and delete it if it does
if (Test-Path "./docs") {
    Remove-Item "./docs" -Recurse -Force
}

# execute sphinx-apidoc using template files (customize ./docs/conf.py)
sphinx-apidoc -F -o "./docs" -A $json.author -H $json.project -V $json.version -t ./templates $json.source_dir 
