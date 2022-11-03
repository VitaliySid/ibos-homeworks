rule rule_cmd_2
{	meta:
		description = "assemblyIdentity"
	strings:
		$c0 = {43 00 6d 00 64 00}
	condition:
		$c0
}