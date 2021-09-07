# blender-alpha-updater

A python script for Linux that uses wget and tar to download and extract the current Blender Alpha daily build.


## How?

Pop the update_blender_latest.py file in a folder and run `python update_blender_latest.py` from a terminal. Once it's finished running, you will have two new folders. One is the actual Blender build, and the other is just a symbolic folder named "blender-latest" pointing to it. You can then create a shortcut to the blender binary inside the symbolic folder. You can edit the symbolic folder name and the keyword used to select the build in the start of the script.


## Who?

This is NOT for Blender users who are working on big collaborative productions, as the latest alpha build might have regressions, break, destroy all your files and/or worst. This is for the risk-taking, live-life-on-the-edge-of-your-seat, carefree kind of Blender users, who just always want to check the latest toys, and are fully aware that they're doing so at their own risks.


## When?

The script will only download the latest build when it has a different name from the ones in the current folder, so you don't end up downloading and extracting a version you already have installed. **Note** that whilst the symbolic folder gets updated, the previous build doesn't get deleted automatically. This is just in case of a show-stopping regression, and it does mean you might want to go and delete a few of the older builds every now and then.


## Why?

Every few days or week, I would go to the blender.org experimental build page, download the latest alpha daily archive, extract it then rename the folder to "blender-latest", so that I didn't need to change my custom shortcut to the Blender binary file.

After a few years of doing that, it hit me that this kind of repetitive tasks is exactly why we have computers in the first place. So I wrote this script which does all those steps automatically. The only difference is that instead of renaming the folder, it creates/overwrites a symbolic link to it. 
