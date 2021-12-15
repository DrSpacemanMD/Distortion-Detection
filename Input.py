import Analysis
import Compute_Distortion
import sys

#Set up and run the Distortion Distance Calculation
ComputeDistortionGeoCorrection = Compute_Distortion.DistortionCalculation("TestData" , "3D Sag T1 BRAVO Geom Core") 
NoDitsortionAnalysis = Analysis.AnalysisResults("No_Distortion",ComputeDistortionGeoCorrection)


ComputeDistortionGeoCorrection.GetFudicalSpheres()
#ComputeDistortionGeoCorrection.AdjustPoint([121,263,85],[156,263,85])
#NoDitsortionAnalysis.CheckPoints()

ComputeDistortionGeoCorrection.GetDistances()

#Pass the distortion calc to the analysis class for well analysis...

NoDitsortionAnalysis.DistortionAnalysis()
NoDitsortionAnalysis.PrintToScreen()
#NoDitsortionAnalysis.OutputToFile("Output.txt")
#NoDitsortionAnalysis.Show3dModel("Interplate Max Distortion X")

#NoDitsortionAnalysis.OutputPeriodicData("DistortionData.csv")
#NoDitsortionAnalysis.OutputPeriodicData("DistortionData.csv")
#NoDitsortionAnalysis.OutputPeriodicData("DistortionData.csv")
NoDitsortionAnalysis.PlotCSV("DistortionData.csv")

'''
print (" ")
ComputeDistortionGeoCorrection = Compute_Distortion.DistortionCalculation("TestDistoredData" , "3D Sag T1 BRAVO BW=15 Shim off")
ComputeDistortionGeoCorrection.GetFudicalSpheres()

#Pass the distortion calc to the analysis class for well analysis...
NoDitsortionAnalysis = Analysis.AnalysisResults("Distortion",ComputeDistortionGeoCorrection)
NoDitsortionAnalysis.DistortionAnalysis()
NoDitsortionAnalysis.PrintToScreen()



print (" ")
ComputeDistortionGeoCorrection = Compute_Distortion.DistortionCalculation("TestDataNoCor" , "3D Sag T1 BRAVO")
ComputeDistortionGeoCorrection.GetFudicalSpheres()

#Pass the distortion calc to the analysis class for well analysis...
NoDitsortionAnalysis = Analysis.AnalysisResults("No_Correction",ComputeDistortionGeoCorrection)
NoDitsortionAnalysis.DistortionAnalysis()
NoDitsortionAnalysis.PrintToScreen()
'''