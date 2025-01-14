#!/usr/bin/python

##################
# init_TIRF.py
#
# Copyright David Baddeley, 2009
# d.baddeley@auckland.ac.nz
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################

from PYME.Acquire.Hardware.AndorIXon import AndorIXon
from PYME.Acquire.Hardware.AndorIXon import AndorControlFrame



from PYME.Acquire.Hardware import fakeShutters
import time
import os
import sys

def GetComputerName():
    if sys.platform == 'win32':
        return os.environ['COMPUTERNAME']
    else:
        return os.uname()[1]

#scope.cameras = {}
#scope.camControls = {}
from PYME.IO import MetaDataHandler

# Let the software know about the noise characteristics of the camera
# these can be found in the documentation that comes with the camera
# and will be propagated into the image metadata
# an entry must be present under your cameras serial number for the software to start
#
# The parameters are:
# noiseProperties[<serial number>]
#
# ReadNoise: Read noise in electrons
# ElectronsPerCount: as name implies - A/D the conversion factor
# NGainStages: Number of EM gain stages (afaik, the same for all IXons, allows a more accurate calulation of muliplication excess noise, but not currently used)
# ADOffset: The black level, or DC conversion offest. Typically recalculated on a per-series basis from initial dark frames as this number is not truely constant.
# DefaultEMGain: EM Gain register setting (not actual gain) to be used for acquistion. Typically a value which reduces the read noise to ~ 1 e- equivalent (I choose a value which makes the true EM gain ~35).
# SaturationThreshold: Pixel value at which to automatically turn off the EM gain / close the camera shutter to try and prevent damage to the CCD. 

AndorIXon.noiseProperties[7863]={
        'ReadNoise' : 152.69,
        'ElectronsPerCount' : 9.18,
        'NGainStages' : 536,
        'ADOffset' : 203,
        'DefaultEMGain' : 90,
        'SaturationThreshold' : (2**14 -1)
        }

InitBG('EMCCD Cameras', """
scope.cameras['A - Left'] = AndorIXon.iXonCamera(0)
scope.cam = scope.cameras['A - Left']
""")

#InitBG('EMCCD Camera 2', """
#scope.cameras['B'] = AndorIXon.iXonCamera(0)
#""")

InitGUI("""
scope.camControls['A - Left'] = AndorControlFrame.AndorPanel(MainFrame, scope.cameras['A - Left'], scope)
camPanels.append((scope.camControls['A - Left'], 'EMCCD A Properties'))

""")

#InitGUI("""
#from PYME.Acquire import sampleInformation
#sampPan = sampleInformation.slidePanel(MainFrame)
#camPanels.append((sampPan, 'Current Slide'))
#""")

#setup for the channels to aquire - b/w camera, no shutters
class chaninfo:
    names = ['bw']
    cols = [1] #1 = b/w, 2 = R, 4 = G1, 8 = G2, 16 = B
    hw = [fakeShutters.CH1] #unimportant - as we have no shutters
    itimes = [100]

scope.chaninfo = chaninfo
scope.shutters = fakeShutters


#PIFoc
#InitBG('PIFoc', """
#from PYME.Acquire.Hardware.Piezos import piezo_e816
#scope.piFoc = piezo_e816.piezo_e816('COM1', 400, 0, True)
#scope.piezos.append((scope.piFoc, 1, 'PIFoc'))
#""")

#InitBG('Stage Stepper Motors', """
#from PYME.Acquire.Hardware.Mercury import mercuryStepper
#scope.stage = mercuryStepper.mercuryStepper(comPort=5, axes=['A', 'B'], steppers=['M-229.25S', 'M-229.25S'])
#scope.stage.SetSoftLimits(0, [1.06, 20.7])
#scope.stage.SetSoftLimits(1, [.8, 17.6])
#scope.piezos.append((scope.stage, 0, 'Stage X'))
#scope.piezos.append((scope.stage, 1, 'Stage Y'))
#scope.joystick = scope.stage.joystick
#scope.joystick.Enable(True)
#scope.CleanupFunctions.append(scope.stage.Cleanup)
#""")

#InitGUI("""
#from PYME.Acquire import sarcSpacing
#ssp = sarcSpacing.SarcomereChecker(MainFrame, menuBar1, scope)
#""")



#InitGUI("""
#from PYME.Acquire import positionTracker
#pt = positionTracker.PositionTracker(scope, time1)
#pv = positionTracker.TrackerPanel(MainFrame, pt)
#MainFrame.AddPage(page=pv, select=False, caption='Track')
#time1.WantNotification.append(pv.draw)
#""")

#splitter
#InitGUI("""
#from PYME.Acquire.Hardware import splitter
#splt = splitter.Splitter(MainFrame, mControls, scope, scope.cam, flipChan = 0, dichroic = 'NotYet' , transLocOnCamera = 'Top', flip=False)
#""")

#we don't have a splitter - make sure that the analysis knows this
#scope.mdh['Splitter.Flip'] = False

#Z stage
#InitGUI("""
#from PYME.Acquire.Hardware import NikonTi
#scope.zStage = NikonTi.zDrive()
#import Pyro.core
#scope.zStage = Pyro.core.getProxyForURI('PYRONAME://%s.ZDrive'  % GetComputerName())
#scope.piezos.append((scope.zStage, 1, 'Z Stepper'))
#""")# % GetComputerName())

#Nikon Ti motorised controls
#InitGUI("""
#from PYME.Acquire.Hardware import NikonTi, NikonTiGUI
#scope.dichroic = NikonTi.FilterChanger()
#scope.lightpath = NikonTi.LightPath()
#
#TiPanel = NikonTiGUI.TiPanel(MainFrame, scope.dichroic, scope.lightpath)
#toolPanels.append((TiPanel, 'Nikon Ti'))
#time1.WantNotification.append(TiPanel.SetSelections)
#
#MetaDataHandler.provideStartMetadata.append(scope.dichroic.ProvideMetadata)
#MetaDataHandler.provideStartMetadata.append(scope.lightpath.ProvideMetadata)
#""")# % GetComputerName())

#InitGUI("""
#from PYME.Acquire.Hardware import focusKeys
#fk = focusKeys.FocusKeys(MainFrame, menuBar1, scope.piezos[0], scope=scope)
#time1.WantNotification.append(fk.refresh)
#""")

#from PYME.Acquire.Hardware import frZStage
#frz = frZStage.frZStepper(MainFrame, scope.zStage)
#frz.Show()

##3-axis piezo
#InitBG('Thorlabs Piezo', """
#from PYME.Acquire.Hardware import thorlabsPiezo
#
##check to see what we've got attached
#piezoSerialNums = thorlabsPiezo.EnumeratePiezos()
#if len(piezoSerialNums) == 3: #expect to see 3 piezos
#    scope.pzx = thorlabsPiezo.TLPiezo(91814461, 'X Axis')
#    scope.pzy = thorlabsPiezo.TLPiezo(91814462, 'Y Axis')
#    scope.pzz = thorlabsPiezo.TLPiezo(91814463, 'Z Axis')
#
#    scope.piezos.append((scope.pzx, 1, 'X Piezo'))
#    scope.piezos.append((scope.pzy, 1, 'Y Piezo'))
#    scope.piezos.append((scope.pzz, 1, 'Z Piezo'))
#
#    #centre the piezos
#    scope.pzx.MoveTo(0,50)
#    scope.pzy.MoveTo(0,50)
#    scope.pzz.MoveTo(0,40)
#else:
#    raise HWNotPresent
#
#""")
    
#from PYME.Acquire.Hardware.FilterWheel import WFilter, FiltFrame
#filtList = [WFilter(1, 'EMPTY', 'EMPTY', 0),
#    WFilter(2, 'ND.5' , 'UVND 0.5', 0.5),
#    WFilter(3, 'ND1'  , 'UVND 1'  , 1),
#    WFilter(4, 'ND2', 'UVND 2', 2),
#    WFilter(5, 'ND3'  , 'UVND 3'  , 3),
#    WFilter(6, 'ND4'  , 'UVND 4'  , 4)]
#
#InitGUI("""
#try:
#    scope.filterWheel = FiltFrame(MainFrame, filtList, 'COM4')
#    scope.filterWheel.SetFilterPos("ND4")
#    toolPanels.append((scope.filterWheel, 'Filter Wheel'))
#except:
#    print 'Error starting filter wheel ...'
#""")


#DigiData
#from PYME.Acquire.Hardware import phoxxLaser
#scope.l642 = phoxxLaser.PhoxxLaser('642')
#scope.StatusCallbacks.append(scope.l642.GetStatusText)
#scope.lasers = [scope.l642]
# scope.lasers = []
#InitBG('DigiData', """
#from PYME.Acquire.Hardware.DigiData import DigiDataClient
#dd = DigiDataClient.getDDClient()
#
#
#from PYME.Acquire.Hardware import lasers
#scope.l490 = lasers.DigiDataSwitchedLaser('490',dd,4)
#scope.l405 = lasers.DigiDataSwitchedLaserInvPol('405',dd,0)
##scope.l543 = lasers.DigiDataSwitchedAnalogLaser('543',dd,0)
##scope.l671 = lasers.DigiDataSwitchedAnalogLaser('671',dd,1)
#
#pport = lasers.PPort()
#scope.l671 = lasers.ParallelSwitchedLaser('671',pport,0)
#scope.l532 = lasers.ParallelSwitchedLaser('532',pport,1)
#
#scope.lasers = [scope.l405,scope.l532,scope.l671, scope.l490]
#""")

#InitGUI("""
#if 'lasers'in dir(scope):
#    from PYME.Acquire.Hardware import LaserControlFrame
#    lcf = LaserControlFrame.LaserControlLight(MainFrame,scope.lasers)
#    time1.WantNotification.append(lcf.refresh)
#    toolPanels.append((lcf, 'Laser Control'))
#""")
#
#from PYME.Acquire.Hardware import PM100USB
#
#scope.powerMeter = PM100USB.PowerMeter()
#scope.powerMeter.SetWavelength(671)
#scope.StatusCallbacks.append(scope.powerMeter.GetStatusText)

##Focus tracking
#from PYME.Acquire.Hardware import FocCorrR
#InitBG('Focus Corrector', """
#scope.fc = FocCorrR.FocusCorrector(scope.zStage, tolerance=0.20000000000000001, estSlopeDyn=False, recDrift=False, axis='Y', guideLaser=l488)
#scope.StatusCallbacks.append(fc.GetStatus)
#""")
#InitGUI("""
#if 'fc' in dir(scope):
#    scope.fc.addMenuItems(MainFrame, MainMenu)
#    scope.fc.Start(2000)
#""")




#must be here!!!
joinBGInit() #wait for anyhting which was being done in a separate thread

#scope.SetCamera('A')

time.sleep(.5)
scope.initDone = True
