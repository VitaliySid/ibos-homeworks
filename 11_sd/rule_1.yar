rule rule_cmd_1
{	meta:
		description = "assemblyIdentity"
	strings:
		$c0 = "Microsoft.Windows.FileSystem.CMD"
	condition:
		$c0
}