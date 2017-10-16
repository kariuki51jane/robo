#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import spi
import signal
import time
from motor import *
from recive import *
import compass
import socket
'''s1=socket.socket()
host1='192.168.43.167'
port=12345
s1.bind((host1, port))
s1.listen(5)'''

  
class MFRC522:
  

  NRSTPD = 22
  
  MAX_LEN = 16
  
  PCD_IDLE       = 0x00
  PCD_AUTHENT    = 0x0E
  PCD_RECEIVE    = 0x08
  PCD_TRANSMIT   = 0x04
  PCD_TRANSCEIVE = 0x0C
  PCD_RESETPHASE = 0x0F
  PCD_CALCCRC    = 0x03
  
  PICC_REQIDL    = 0x26
  PICC_REQALL    = 0x52
  PICC_ANTICOLL  = 0x93
  PICC_SElECTTAG = 0x93
  PICC_AUTHENT1A = 0x60
  PICC_AUTHENT1B = 0x61
  PICC_READ      = 0x30
  PICC_WRITE     = 0xA0
  PICC_DECREMENT = 0xC0
  PICC_INCREMENT = 0xC1
  PICC_RESTORE   = 0xC2
  PICC_TRANSFER  = 0xB0
  PICC_HALT      = 0x50
  
  MI_OK       = 0
  MI_NOTAGERR = 1
  MI_ERR      = 2
  
  Reserved00     = 0x00
  CommandReg     = 0x01
  CommIEnReg     = 0x02
  DivlEnReg      = 0x03
  CommIrqReg     = 0x04
  DivIrqReg      = 0x05
  ErrorReg       = 0x06
  Status1Reg     = 0x07
  Status2Reg     = 0x08
  FIFODataReg    = 0x09
  FIFOLevelReg   = 0x0A
  WaterLevelReg  = 0x0B
  ControlReg     = 0x0C
  BitFramingReg  = 0x0D
  CollReg        = 0x0E
  Reserved01     = 0x0F
  
  Reserved10     = 0x10
  ModeReg        = 0x11
  TxModeReg      = 0x12
  RxModeReg      = 0x13
  TxControlReg   = 0x14
  TxAutoReg      = 0x15
  TxSelReg       = 0x16
  RxSelReg       = 0x17
  RxThresholdReg = 0x18
  DemodReg       = 0x19
  Reserved11     = 0x1A
  Reserved12     = 0x1B
  MifareReg      = 0x1C
  Reserved13     = 0x1D
  Reserved14     = 0x1E
  SerialSpeedReg = 0x1F
  
  Reserved20        = 0x20  
  CRCResultRegM     = 0x21
  CRCResultRegL     = 0x22
  Reserved21        = 0x23
  ModWidthReg       = 0x24
  Reserved22        = 0x25
  RFCfgReg          = 0x26
  GsNReg            = 0x27
  CWGsPReg          = 0x28
  ModGsPReg         = 0x29
  TModeReg          = 0x2A
  TPrescalerReg     = 0x2B
  TReloadRegH       = 0x2C
  TReloadRegL       = 0x2D
  TCounterValueRegH = 0x2E
  TCounterValueRegL = 0x2F
  
  Reserved30      = 0x30
  TestSel1Reg     = 0x31
  TestSel2Reg     = 0x32
  TestPinEnReg    = 0x33
  TestPinValueReg = 0x34
  TestBusReg      = 0x35
  AutoTestReg     = 0x36
  VersionReg      = 0x37
  AnalogTestReg   = 0x38
  TestDAC1Reg     = 0x39
  TestDAC2Reg     = 0x3A
  TestADCReg      = 0x3B
  Reserved31      = 0x3C
  Reserved32      = 0x3D
  Reserved33      = 0x3E
  Reserved34      = 0x3F
    
  serNum = []
  
  def __init__(self, dev='/dev/spidev0.0', spd=1000000):
    spi.openSPI(device=dev,speed=spd)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(22, GPIO.OUT)
    GPIO.output(self.NRSTPD, 1)
    self.MFRC522_Init()
  
  def MFRC522_Reset(self):
    self.Write_MFRC522(self.CommandReg, self.PCD_RESETPHASE)
  
  def Write_MFRC522(self, addr, val):
    spi.transfer(((addr<<1)&0x7E,val))
  
  def Read_MFRC522(self, addr):
    val = spi.transfer((((addr<<1)&0x7E) | 0x80,0))
    return val[1]
  
  def SetBitMask(self, reg, mask):
    tmp = self.Read_MFRC522(reg)
    self.Write_MFRC522(reg, tmp | mask)
    
  def ClearBitMask(self, reg, mask):
    tmp = self.Read_MFRC522(reg);
    self.Write_MFRC522(reg, tmp & (~mask))
  
  def AntennaOn(self):
    temp = self.Read_MFRC522(self.TxControlReg)
    if(~(temp & 0x03)):
      self.SetBitMask(self.TxControlReg, 0x03)
  
  def AntennaOff(self):
    self.ClearBitMask(self.TxControlReg, 0x03)
 
  def MFRC522_ToCard(self,command,sendData):
    backData = []
    backLen = 0
    status = self.MI_ERR
    irqEn = 0x00
    waitIRq = 0x00
    lastBits = None
    n = 0
    i = 0
    
    if command == self.PCD_AUTHENT:
      irqEn = 0x12
      waitIRq = 0x10
    if command == self.PCD_TRANSCEIVE:
      irqEn = 0x77
      waitIRq = 0x30
    
    self.Write_MFRC522(self.CommIEnReg, irqEn|0x80)
    self.ClearBitMask(self.CommIrqReg, 0x80)
    self.SetBitMask(self.FIFOLevelReg, 0x80)
    
    self.Write_MFRC522(self.CommandReg, self.PCD_IDLE);  
    
    while(i<len(sendData)):
      self.Write_MFRC522(self.FIFODataReg, sendData[i])
      i = i+1
    
    self.Write_MFRC522(self.CommandReg, command)
      
    if command == self.PCD_TRANSCEIVE:
      self.SetBitMask(self.BitFramingReg, 0x80)
    
    i = 2000
    while True:
      n = self.Read_MFRC522(self.CommIrqReg)
      i = i - 1
      if ~((i!=0) and ~(n&0x01) and ~(n&waitIRq)):
        break
    
    self.ClearBitMask(self.BitFramingReg, 0x80)
  
    if i != 0:
      if (self.Read_MFRC522(self.ErrorReg) & 0x1B)==0x00:
        status = self.MI_OK

        if n & irqEn & 0x01:
          status = self.MI_NOTAGERR
      
        if command == self.PCD_TRANSCEIVE:
          n = self.Read_MFRC522(self.FIFOLevelReg)
          lastBits = self.Read_MFRC522(self.ControlReg) & 0x07
          if lastBits != 0:
            backLen = (n-1)*8 + lastBits
          else:
            backLen = n*8
          
          if n == 0:
            n = 1
          if n > self.MAX_LEN:
            n = self.MAX_LEN
    
          i = 0
          while i<n:
            backData.append(self.Read_MFRC522(self.FIFODataReg))
            i = i + 1;
      else:
        status = self.MI_ERR

    return (status,backData,backLen)

  def MFRC522_Request(self, reqMode):
    status = None
    backBits = None
    TagType = []
    
    self.Write_MFRC522(self.BitFramingReg, 0x07)
    
    TagType.append(reqMode);
    (status,backData,backBits) = self.MFRC522_ToCard(self.PCD_TRANSCEIVE, TagType)
  
    if ((status != self.MI_OK) | (backBits != 0x10)):
      status = self.MI_ERR
      
    return (status,backBits)
  
  
  def MFRC522_Anticoll(self):
    backData = []
    serNumCheck = 0
    
    serNum = []
  
    self.Write_MFRC522(self.BitFramingReg, 0x00)
    
    serNum.append(self.PICC_ANTICOLL)
    serNum.append(0x20)
    
    (status,backData,backBits) = self.MFRC522_ToCard(self.PCD_TRANSCEIVE,serNum)
    
    if(status == self.MI_OK):
      i = 0
      if len(backData)==5:
        while i<4:
          serNumCheck = serNumCheck ^ backData[i]
          i = i + 1
        if serNumCheck != backData[i]:
          status = self.MI_ERR
      else:
        status = self.MI_ERR
  
    return (status,backData)
  
  def CalulateCRC(self, pIndata):
    self.ClearBitMask(self.DivIrqReg, 0x04)
    self.SetBitMask(self.FIFOLevelReg, 0x80);
    i = 0
    while i<len(pIndata):
      self.Write_MFRC522(self.FIFODataReg, pIndata[i])
      i = i + 1
    self.Write_MFRC522(self.CommandReg, self.PCD_CALCCRC)
    i = 0xFF
    while True:
      n = self.Read_MFRC522(self.DivIrqReg)
      i = i - 1
      if not ((i != 0) and not (n&0x04)):
        break
    pOutData = []
    pOutData.append(self.Read_MFRC522(self.CRCResultRegL))
    pOutData.append(self.Read_MFRC522(self.CRCResultRegM))
    return pOutData
  
  def MFRC522_SelectTag(self, serNum):
    backData = []
    buf = []
    buf.append(self.PICC_SElECTTAG)
    buf.append(0x70)
    i = 0
    while i<5:
      buf.append(serNum[i])
      i = i + 1
    pOut = self.CalulateCRC(buf)
    buf.append(pOut[0])
    buf.append(pOut[1])
    (status, backData, backLen) = self.MFRC522_ToCard(self.PCD_TRANSCEIVE, buf)
    
    if (status == self.MI_OK) and (backLen == 0x18):
      print "Size: " + str(backData[0])
      return    backData[0]
    else:
      return 0
  
  def MFRC522_Auth(self, authMode, BlockAddr, Sectorkey, serNum):
    buff = []

    # First byte should be the authMode (A or B)
    buff.append(authMode)

    # Second byte is the trailerBlock (usually 7)
    buff.append(BlockAddr)

    # Now we need to append the authKey which usually is 6 bytes of 0xFF
    i = 0
    while(i < len(Sectorkey)):
      buff.append(Sectorkey[i])
      i = i + 1
    i = 0

    # Next we append the first 4 bytes of the UID
    while(i < 4):
      buff.append(serNum[i])
      i = i +1

    # Now we start the authentication itself
    (status, backData, backLen) = self.MFRC522_ToCard(self.PCD_AUTHENT,buff)

    # Check if an error occurred
    if not(status == self.MI_OK):
      print "AUTH ERROR!!"
    if not (self.Read_MFRC522(self.Status2Reg) & 0x08) != 0:
      print "AUTH ERROR(status2reg & 0x08) != 0"

    # Return the status
    return status
  
  def MFRC522_StopCrypto1(self):
    self.ClearBitMask(self.Status2Reg, 0x08)
 
  
  def MFRC522_Read(self, blockAddr):
    recvData = []
    recvData.append(self.PICC_READ)
    recvData.append(blockAddr)
    pOut = self.CalulateCRC(recvData)
    recvData.append(pOut[0])
    recvData.append(pOut[1])
    (status, backData, backLen) = self.MFRC522_ToCard(self.PCD_TRANSCEIVE, recvData)
#rfid card check for nodes ###########################################################################

    comread = compass.hmc5883l()
    degrees =comread.degrees(comread.heading())
    def path():
      Tcp_connect( '192.168.43.28', 17098)
      if backData[0]==1:
        Tcp_Write('a')
        data=[]
        data=Tcp_Read()
        return data
      elif backData[0]==2:
        Tcp_Write('b')
        data=[]
        data=Tcp_Read()
        return data
      elif backData[0]==3:
        Tcp_Write('c')
        data=[]
        data=Tcp_Read()
        return data
      elif backData[0]==4:
        Tcp_Write('d')
        data=[]
        data=Tcp_Read()
        return data
      elif backData[0]==5:
        Tcp_Write('e')
        data=[]
        data=Tcp_Read()
        return data
      elif backData[0]==6:
        Tcp_Write('f')
        data=[]
        data=Tcp_Read()
        return data
      elif backData[0]==7:
        Tcp_Write('g')
        data=[]
        data=Tcp_Read()
        return data
      elif backData[0]==8:
        Tcp_Write('h')
        data=[]
        data=Tcp_Read()
        return data
      elif backData[0]==9:
        Tcp_Write('i')
        data=[]
        data=Tcp_Read()
        return data
      elif backData[0]==10:
        Tcp_Write('j')
        data=[]
        data=Tcp_Read()
        return data
      elif backData[0]==11:
        Tcp_Write('k')
        data=[]
        data=Tcp_Read()
        return data
      elif backData[0]==12:
        Tcp_Write('l')
        data=[]
        data=Tcp_Read()
        return data
      elif backData[0]==13:
        Tcp_Write('m')
        data=[]
        data=Tcp_Read()
        return data
      elif backData[0]==14:
        Tcp_Write('n')
        data=[]
        data=Tcp_Read()
        return data
      elif backData[0]==15:
        Tcp_Write('0')
        data=[]
        data=Tcp_Read()
        return data
      elif backData[0]==16:
        Tcp_Write('p')
        data=[]
        data=Tcp_Read()
        return data
      elif backData[0]==17:
        Tcp_Write('q')
        data=[]
        data=Tcp_Read()
        return data
      else:
        return 0
    data=path()
    def recive():
      #data=path()
          
      if (len(data)>=1):
          if data[0]=='a' :
              data1=1
              return data1
              #print data[0]
          elif data[0]=='b' :
              data1=2
              return data1
          elif data[0]=='c' :
              data1=3
              return data1
              #print data[0]
          elif data[0]=='d' :
              data1=4
              return data1
          elif data[0]=='e' :
              data1=5
              return data1
              #print data[0]
          elif data[0]=='f' :
              data1=6
              return data1
          elif data[0]=='g' :
              data1=7
              return data1
          elif data[0]=='h' :
              data1=8
              return data1
              #print data[0]
          elif data[0]=='i' :
              data1=9
              return data1
          elif data[0]=='j' :
              data1=10
              return data1
              #print data[0]
          elif data[0]=='k' :
              data1=11
              return data1
           
          elif data[0]=='l' :
              data1=12
              return data1
              #print data[0]
          elif data[0]=='m' :
              data1=13
              return data1
          elif data[0]=='n' :
              data1=14
              return data1
          elif data[0]=='0' :
              data1=15
              return data1
              #print data[0]
          elif data[0]=='p' :
              data1=16
              return data1
          elif data[0]=='q' :
              data1=17
              return data1
              #print data[0]


    def recive1():
      #data=path()
      
      if (len(data)>=2):
          if data[1]=='a' :
              data1=1
              return data1
          elif data[1]=='b' :
              data1=2
              return data1
          elif data[1]=='c' :
              data1=3
              return data1
              #print data[0]
          elif data[1]=='d' :
              data1=4
              return data1
          elif data[1]=='e' :
              data1=5
              return data1
              #print data[0]
          elif data[1]=='f' :
              data1=6
              return data1
          elif data[1]=='g' :
              data1=7
              return data1
          elif data[1]=='h' :
              data1=8
              return data1
              #print data[0]
          elif data[1]=='i' :
              data1=9
              return data1
          elif data[1]=='j' :
              data1=10
              return data1
              #print data[0]
          elif data[1]=='k' :
              data1=11
              return data1
          elif data[1]=='l' :
              data1=12
              return data1
              #print data[0]
          elif data[1]=='m' :
              data1=13
              return data1
          elif data[1]=='n' :
              data1=14
              return data1
          elif data[1]=='0' :
              data1=15
              return data1
              #print data[0]
          elif data[1]=='p' :
              data1=16
              return data1
          elif data[1]=='q' :
              data1=17
              return data1
    def recive2():
      
      #data=path()
      if (len(data)>=3):
          if data[2]=='a' :
              data1=1
              return data1
          elif data[2]=='b' :
              data1=2
              return data1
          elif data[2]=='c' :
              data1=3
              return data1
              #print data[0]
          elif data[2]=='d' :
              data1=4
              return data1
          elif data[2]=='e' :
              data1=5
              return data1
              #print data[0]
          elif data[2]=='f' :
              data1=6
              return data1
    def recive3():
      
      #data=path()
      if (len(data)>=4):
          if data[3]=='a' :
              data1=1
              return data1
          elif data[3]=='b' :
              data1=2
              return data1
          elif data[3]=='c' :
              data1=3
              return data1
              #print data[0]
          elif data[3]=='d' :
              data1=4
              return data1
          elif data[3]=='e' :
              data1=5
              return data1
              #print data[0]
          elif data[3]=='f' :
              data1=6
              return data1 
    if backData[0] == recive() :#if node is correct
      for x in range(2,16):   #check the nodes regarding to the system input
        
        if (backData[x]==recive1()):
          turn = backData[x+1] #access degree to turn
          print turn
          print "get it"
          clockwise()
          time.sleep(0.6)
          if turn==215:
            print degrees
            if 85<=degrees<=145:
              right_nin()
              time.sleep(0.4)

            if 264<=degrees<=324:
              left_nin()
              time.sleep(0.4)

            if 0<=degrees<=52:
              turn_nin()
              time.sleep(0.9)
            if 120<=degrees<=270:
              print "right direction"
 
            '''  
            while(0<=degrees<=210):   #set turning direction
                obsright()
                degrees =comread.degrees(comread.heading()) #update degrees
                print degrees

            while(220<=degrees<=350):   #set turning direction
                obsleft()
                degrees =comread.degrees(comread.heading()) #update degrees

            ''' 
          elif turn==23:
            #left_nin()
            #time.sleep(0.5)
            if 85<=degrees<=145:
              left_nin()
              time.sleep(0.4)

            if 264<=degrees<=324:
              right_nin()
              time.sleep(0.4)

            if 120<=degrees<=270:
              turn_nin()
              time.sleep(0.9)
            if 0<=degrees<=52:
              print "right direction"
            '''
            while(250<=degrees<=359):   #set turning direction
                obsright()
                degrees =comread.degrees(comread.heading()) #update degrees
                print degrees 
            while(0<=degrees<=18):   #set turning direction
                obsright()
                degrees =comread.degrees(comread.heading()) #update degrees
                print degrees
    
            while(28<=degrees<=300):   #set turning direction
                obsleft()
                degrees =comread.degrees(comread.heading()) #update degrees

             ''' 


          elif turn==295:
            if 85<=degrees<=145:
              turn_nin()
              time.sleep(0.9)

            if 120<=degrees<=270:
              left_nin()
              time.sleep(0.4)

            if 0<=degrees<=52:
              right_nin()
              time.sleep(0.4)
            if 264<=degrees<=324:
              print "right direction"
            '''
            while(220<=degrees<=290):   #set turning direction
                obsright()
                degrees =comread.degrees(comread.heading()) #update degrees
                print degrees
            while(300<=degrees<=370):   #set turning direction
                obsleft()
                degrees =comread.degrees(comread.heading()) #update degrees
            '''
          elif turn==117:
            print "get 117"
            
            if 264<=degrees<=324:
              turn_nin()
              time.sleep(0.9)

            if 120<=degrees<=270:
              left_nin()
              time.sleep(0.4)

            if 0<=degrees<=52:
              right_nin()
              time.sleep(0.4)
            if 85<=degrees<=145:
              print "right direction"
          else:
            print "error"
            '''
            while(0<=degrees<=110):   #set turning direction
                obsright()
                degrees =comread.degrees(comread.heading()) #update degrees
                print degrees
            while(120<=degrees<=250):   #set turning direction
                obsleft()
                degrees =comread.degrees(comread.heading()) #update degrees
            '''
          '''
          while(turn-10<=degrees<=turn-5):   #set turning direction
            obsright()
            degrees =comread.degrees(comread.heading()) #update degrees
            print degrees

          while(turn+5<=degrees<=turn+10):   #set turning direction
            obsleft()
            degrees =comread.degrees(comread.heading()) #update degrees
            print degrees
          '''
          #while(0<=degrees <= (turn-5)):
           # obsright()
            #degrees =comread.degrees(comread.heading())
            #print degrees
           
          #while((turn+5)<=degrees<=269):
           # obsleft()
            #degrees =comread.degrees(comread.heading())
            #print degrees
            
          
      x=x+2
      
##############################################################################################    
    if not(status == self.MI_OK):
      print "Error while reading!"
    i = 0
    if len(backData) == 16:
      print "Sector "+str(blockAddr)+" "+str(backData)
      hault()



  

  def MFRC522_Init(self):
    GPIO.output(self.NRSTPD, 1)
  
    self.MFRC522_Reset();
    
    
    self.Write_MFRC522(self.TModeReg, 0x8D)
    self.Write_MFRC522(self.TPrescalerReg, 0x3E)
    self.Write_MFRC522(self.TReloadRegL, 30)
    self.Write_MFRC522(self.TReloadRegH, 0)
    
    self.Write_MFRC522(self.TxAutoReg, 0x40)
    self.Write_MFRC522(self.ModeReg, 0x3D)
    self.AntennaOn()
