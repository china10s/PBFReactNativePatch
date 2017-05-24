# PBFReactNativePatch
A simple pactch script for reactnative project to build jsbundle and make diff file against every older versions.

## patch floder ##

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
