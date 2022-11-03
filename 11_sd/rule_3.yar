rule rule_cmd_3
{	meta:
		description = "assemblyIdentity"
	strings:
	    $a0 = "Microsoft.Windows.FileSystem.CMD"
		$b0 = { 4d 5a 90 00 03 00 00 00 04 00 00 00 ff ff 00 00}
		$c0 = {43 00 6d 00 64 00}
	condition:
		$a0 and $b0 and $c0
}