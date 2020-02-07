rule metasploit
{
        strings:
                $getos = "select case getGUIType" nocase wide ascii
                        $getext = "select case GetOS" nocase wide ascii
                        $func1 = "Sub OnLoad" nocase wide ascii
                        $func2 = "Sub Exploit" nocase wide ascii
                        $func3 = "Function GetOS() as string" nocase wide ascii
                        $func4 = "Function GetExtName() as string" nocase wide ascii

                condition:
                    (all of ($get*) or 2 of ($func*))
}

rule powershell
{
        strings:
                        $psh1  = "powershell" nocase wide ascii
                        $psh2  = "new-object" nocase wide ascii
                        $psh3  = "net.webclient" nocase wide ascii
                        $psh4  = "downloadstring" nocase wide ascii
                        $psh5  = "downloadfile" nocase wide ascii
                        $psh6  = "iex" nocase wide ascii
                        $psh7  = "-e" nocase wide ascii
                        $psh8  = "iwr" nocase wide ascii
                        $psh9  = "-outfile" nocase wide ascii
                        $psh10 = "invoke-exp" nocase wide ascii

                condition:
                    2 of ($psh*)
}

rule cmd
{
        strings:
                    $cmd1 = "cmd /c" nocase wide ascii
                        $cmd2 = "cmd /k" nocase wide ascii
                condition:
            any of ($cmd*)
}
