# Play a single file
Add-Type -AssemblyName presentationCore
$mediaPlayer = New-Object system.windows.media.mediaplayer
$musicPath = "C:\work\Projects\LangChain\AI-Doctor-VoiceBot\data\doctor_voice"
$mediaPlayer.open($musicPath + '\test1.wav')


Start-Sleep -Seconds 1
$mediaPlayer.Play()
Start-Sleep -Seconds 10  