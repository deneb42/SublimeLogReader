
# SublimeLogReader

Log colorator for SublimeText allowing easy reviewing of Android and iOS logs

## Installation
1. Download the repo as a zip
2. Inside SublimeText, go to Preferences/Browse Package...
3. Go up a level, then in Installed Package
4. Copy/paste the zip here
5. Rename it "LogReader.sublime-package"
6. And voila !

## Content
 - A theme dedicated for Log reading. (Also compatible with Monokaï, 
   and very likely also compatible with your prefered theme)
 - Coloration for iOS ans Android logs depending on the log level
 - Inclusive and exclusive filtering

## Usage
### Coloration
The plugin will automaticaly color .alog (for Android) and .ilog (iOS) files.
Else, you can trigger the coloration by setting the syntax to either alog or ilog. 

To do that you have multiple solution :
 - On the lower right corner, select LogReader/Android Logs / iOS Logs
 - "ctrl+shift+P" then "set syntax Android Logs" / "iOS Logs"
   A quick way to do this is to type "ctrl+shift+P" "alog" Enter

### Filtering
You can filter the logs to either : 
 - Remove the lines containing the text in your selection (multiple selection supported)
 - Keep only the lines containing the text in your selection (multiple selection supported)

To do that :
 - "ctrl+shift+x" to exclude lines containing your selection(s)
 - "ctrl+shift+c" to conserve lines containing your selection(s)
