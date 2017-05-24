# PBFReactNativePatch
A simple patch script for reactnative project to build jsbundle and make diff file against every older versions.

## Patch floder ##

    Automatically pack reactnative jsbundle and different package,directory structure：
             -Root
                -package.json
                -index.ios.js
                -index.android.js
                -[bundlePatch]
                   -[bundles]                       //source floder
                      -1_0_0
                         -ios
                            -assets
                            -ios.jsbundle
                         -android
                            -drawable-mdpi
                            -android.jsbundle
                      -1_0_1
                         -ios
                            -assets
                            -ios.jsbundle
                         -android
                            -drawable-mdpi
                            -android.jsbundle
                   -[patches]                       //differ patch
                      -1_0_0
                      -1_0_1
                         -ios
                            -1_0_0-1_0_1.zip
                         -android
                            -1_0_0-1_0_1.zip
                   -[patchtask]                     //job
                      -build
                      patch.py                      //main function
                      patchImageFile.py
                      patchJSBuild.py
                      patchJSFile.py
                      patchCompare.py
                      patchZip.py
                      diff_match_patch.py


## Usage (Android & iOS) ##

first you should install node_modules with **package.json** like zhis:
    
    cd [rootpath]
    npm install

after you finished this,u can use this script:

    python patch.py

## Logic of diff  ##
For every **jsbundle** in the project,i use [**google-diff-match-patch**](http://code.google.com/p/google-diff-match-patch/) (Copyright 2006 Google Inc.)to compute the diff of the old one and the new one.

For every **Image** file in the project,i only put the image which has been changed or first add to the project.

In the end,zip the diff floder for publish.
