Write-Output "QueryName,Result,ElapsedTime" > results-ps.csv

Get-ChildItem -Path "queries" -File | ForEach-Object {
	Write-Output ("Processing file" + $_.Name)
	$out = (& .\cvc5/bin/cvc5.exe $_.FullName --tlimit 60000 --stats 2>&1) | Out-String

	$res = ($out | Select-String -Pattern "(unsat)|(sat)|(timeout)").Matches[0].Value.Trim()

	$time = [int] ($out | Select-String -Pattern "[0-9]+ms").Matches[0].Value.Trim().Substring(0, ($out | Select-String -Pattern "[0-9]+ms").Matches[0].Value.Trim().Length - 2)

	Write-Output (@($_.Name, $res.ToUpper(), $time) -join ",") >> results-ps.csv
}
