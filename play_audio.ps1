# Play a single file
Add-Type -AssemblyName presentationCore
$mediaPlayer = New-Object system.windows.media.mediaplayer
$musicPath = "C:\work\Projects\LangChain\AI-Doctor-VoiceBot\data\doctor_voice\"
$mediaPlayer.open($musicPath + 'final.mp3')

# Wait for the media to be loaded and its duration to be available
# This can be done by checking the NaturalDuration property or by using a short sleep
while (-not $mediaPlayer.NaturalDuration.HasTimeSpan) {
    Start-Sleep -Milliseconds 100
}

# Get the duration of the media file
$duration = $mediaPlayer.NaturalDuration.TimeSpan.TotalSeconds

# Play the media
$mediaPlayer.Play()

# Wait for the duration of the media file
# Add a small buffer to ensure playback completes fully
Start-Sleep -Seconds ($duration + 1) # Add 1 second buffer

# Stop and close the player
$mediaPlayer.Stop()
$mediaPlayer.Close()