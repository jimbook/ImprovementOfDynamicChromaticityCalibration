from MyTool.plotShow import *
from MyTool import wellData
from MyTool.dataPrehandle import *




d_raw = wellData().azigamma().iloc[160:930]#wellData().cflog(0).iloc[2650:3800]#
print("d_smoothly")
d_smoothly = gaussianFilter(d_raw)
print("d_dynamic")
d_dynamic = dynamicOperation(d_smoothly,histogramEqualization,100)
print("d_meanValue")
d_meanValue = dynamicOperation_MeanValue(d_smoothly,histogramEqualization,100)
print("d_gradualChange")
d_gradualChange = dynamicOperation_GradualChange(d_smoothly,histogramEqualization,100)
print("d_AHE-quick")
d_AHE = dynamicOperation_QuicklyAutoAdjust(d_smoothly,transform_HE,100)

# plt.subplot(1,5,1)
# showImage(interpolation(d_smoothly))
# addLabel("未做色度标定","角度方位，°","深度，m")
plt.subplot(1,3,1)
showImage(interpolation(d_dynamic))
addLabel("(a)动态色度标定","角度方位，°","深度，m")
# plt.subplot(1,4,2)
# showImage(interpolation(d_meanValue))
# addLabel("平均值法","角度方位，°","深度，m")
plt.subplot(1,3,2)
showImage(interpolation(d_gradualChange))
addLabel("(b)渐变过渡法","角度方位，°","深度，m")
plt.subplot(1,3,3)
showImage(interpolation(d_AHE))
addLabel("(c)限制步长法","角度方位，°","深度，m")
plt.show()