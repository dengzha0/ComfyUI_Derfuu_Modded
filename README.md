# Description

This is a fork from Derfuu_ComfyUI_ModdedNodes. You can find the original repo from [LINK](https://github.com/Derfuu/Derfuu_ComfyUI_ModdedNodes) .

I've made a few modifications to accommodate my own usage habits.

# Modifications
- Math Nodes
  - multiply: the input type changed to int\*float from float\*float, the output type changed to int from float.
  - divide: the input type changed to int/float from float/float, the output type changed to int from float.
  - sum: the input type changed to int+int from float+float, the output type changed to int from float.
  - sub: the input type changed to int-int from float-float, the output type changed to int from float.
- Pow Node: I completely changed this node to another whole different function since I will never use this node.
- KeepRatio Node: New node from PowNode, this node will output a new group of width and height. This node is similar to Latent_Scale_to_side or Image_scale_to_side, the difference is the input and output of this node is width/height instead of image/latent.
