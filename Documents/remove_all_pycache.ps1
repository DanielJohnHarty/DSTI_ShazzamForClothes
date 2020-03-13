$source = '..'
$names = @('__pycache__')

Get-ChildItem $source -Recurse -Force |
Where-Object { $_.PSIsContainer -and $names -contains $_.Name } |
Sort-Object FullName -Descending |
Remove-Item -Recurse -Force