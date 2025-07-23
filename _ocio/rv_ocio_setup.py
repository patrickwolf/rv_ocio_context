import os
from rv import commands
import PyOpenColorIO as OCIO

# --- Configuration ---
DEFAULT_INPUT_SPACE = "ACES - ACEScg"
SCENE_LINEAR_SPACE = "ACES - ACEScg"
print ("INFO: RV OCIO Setup",__file__)

def ocio_config_from_media(media, attributes):

    #
    #  This can be either from an environment, or based on whatever
    #  setup you choose to set.
    #
    config = OCIO.Config()
    return config.CreateFromEnv()

def ocio_node_from_media(config, node, default, media=None, attributes={}):

    #
    #  Based on the incoming node assemble the corresponding pipeline
    #

    result = [{"nodeType" : d, "context" : {}, "properties" : {}} for d in default]
    context = {"CDL_FILE_PATH" : "",}

    if media:
        base_path = os.path.splitext(media)[0]
        if '.' in os.path.basename(base_path):
            base_path = base_path.rsplit('.', 1)[0]
        
        cdl_path = base_path + ".cdl"
        
        if os.path.exists(cdl_path):
            context["CDL_FILE_PATH"] = cdl_path
            print(f"INFO: [Yeti OCIO] Found CDL for {media}: {cdl_path}")

    nodeType = commands.nodeType(node)
    if (nodeType == "RVLinearizePipelineGroup"):
        result = [
            {"nodeType": "OCIOFile",
             "context" : context,
             "properties" : {
                 "ocio.function"            : "color",
                 "ocio.inColorSpace"        : DEFAULT_INPUT_SPACE,
                 "ocio_color.outColorSpace" : SCENE_LINEAR_SPACE}},
            {"nodeType" : "RVLensWarp", "context" : {}, "properties" : {}}]

    elif (nodeType == "RVLookPipelineGroup"):
        # Let the view handle applying looks instead of hardcoding them here
        result = [
            {"nodeType"   : "OCIOLook",
             "context"    : context,
             "properties" : {
                 "ocio.function"     : "look",
                 "ocio.inColorSpace" : DEFAULT_INPUT_SPACE,
                 # "ocio_look.look"    : "show_look"  # Commented out - let views handle this
                 }}
            ]

    elif (nodeType == "RVDisplayPipelineGroup"):
        display = config.getDefaultDisplay()
        result = [
            {
                "nodeType": "OCIODisplay",
                 "context": context,
                 "properties": {
                     "ocio.function"        : "display",
                     "ocio.inColorSpace"    : SCENE_LINEAR_SPACE,
                     "ocio_display.view"    : config.getDefaultView(display),
                     "ocio_display.display" : display }}]


    print ("INFO: RV OCIO Setup", result)
    return result
