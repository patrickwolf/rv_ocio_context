Install: https://docs.astral.sh/uv/

Checkout contents to C:\test_ocio on Windows 

Then when running rv_ocio.bat you'll receive this error message

INFO: using OCIOFile node for sourceGroup000000_source RVLinearizePipelineGroup
INFO: RV OCIO Setup [{'nodeType': 'OCIOLook', 'context': {'CDL_FILE_PATH': 'HSO_0510_comp_BOT_v003.cdl'}, 'properties': {'ocio.function': 'look', 'ocio.inColorSpace': 'ACES - ACEScg', 'ocio_look.look': 'shot_specific_look'}}]
INFO: using OCIOLook node for sourceGroup000000_source RVLookPipelineGroup
ERROR: OCIOIPNode: The specified file reference '${CDL_FILE_PATH}' could not be located. The following attempts were made: 'C:\test_ocio\_ocio\luts\${CDL_FILE_PATH}' : 'C:\test_ocio\_media\${CDL_FILE_PATH}'.
