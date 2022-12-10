$project_root=Split-Path  $PSScriptRoot

Get-ChildItem $project_root -Include __pycache__ -Recurse | Remove-Item -Recurse