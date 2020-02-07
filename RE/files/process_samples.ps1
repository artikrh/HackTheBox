$process_dir = "C:\Users\luke\Documents\malware_process"
$files_to_analyze = "C:\Users\luke\Documents\ods"
$yara = "C:\Users\luke\Documents\yara64.exe"
$rule = "C:\Users\luke\Documents\ods.yara"

while($true) {
        # Get new samples
        move C:\Users\luke\Documents\malware_dropbox\* $process_dir

        # copy each ods to zip file
        Get-ChildItem $process_dir -Filter *.ods |
        Copy-Item -Destination {$_.fullname -replace ".ods", ".zip"}

        Get-ChildItem $process_dir -Filter *.zip | ForEach-Object {

                # unzip archive to get access to content
                $unzipdir = Join-Path $_.directory $_.Basename
                New-Item -Force -ItemType directory -Path $unzipdir | Out-Null
                Expand-Archive $_.fullname -Force -ErrorAction SilentlyContinue -DestinationPath $unzipdir

                # yara to look for known malware
                $yara_out = & $yara -r $rule $unzipdir
                $ods_name = $_.fullname -replace ".zip", ".ods"
                if ($yara_out.length -gt 0) {
                        Remove-Item $ods_name
                }
        }


        # if any ods files left, make sure they launch, and then archive:
        $files = ls $process_dir\*.ods
        if ( $files.length -gt 0) {
                # launch ods files
                Invoke-Item "C:\Users\luke\Documents\malware_process\*.ods"
                Start-Sleep -s 5

                # kill open office, sleep
                Stop-Process -Name soffice*
                Start-Sleep -s 5

                #& 'C:\Program Files (x86)\WinRAR\Rar.exe' a -ep $process_dir\temp.rar $process_dir\*.ods 2>&1 | Out-Null
                Compress-Archive -Path "$process_dir\*.ods" -DestinationPath "$process_dir\temp.zip"
                $hash = (Get-FileHash -Algorithm MD5 $process_dir\temp.zip).hash
                # Upstream processing may expect rars. Rename to .rar
                Move-Item -Force -Path $process_dir\temp.zip -Destination $files_to_analyze\$hash.rar
        }

        Remove-Item -Recurse -force -Path $process_dir\*
        Start-Sleep -s 5
}
