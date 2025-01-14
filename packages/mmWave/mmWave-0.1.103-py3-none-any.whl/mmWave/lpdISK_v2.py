# Long range People Detect Raw Data (LPD)
# ver:0.0.1
# 2022/11/03
# parsing Long range People Detect 
# hardware:(Batman-201): ISK IWR6843 ES2.0
# company: Joybien Technologies: www.joybien.com
# author: Zach Chen
#===========================================
# output: V6,V7,V8,v9 Raw data
# v0.0.1 : 2022/11/03 release

import serial
import time
import struct
import numpy as np

class header:
	version = 0
	totalPacketLen = 0
	platform = 0
	frameNumber = 0
	timeCpuCycles = 0
	numDetectedObj = 0
	numTLVs = 0
	subFrameNumber = 0
	
class LpdISK:
	
	magicWord =  [b'\x02',b'\x01',b'\x04',b'\x03',b'\x06',b'\x05',b'\x08',b'\x07',b'\0x99']
	port = ""
	hdr = header

	tlvLength = 0
	numOfPoints = 0
	# for debug use 
	dbg = False #Packet unpacket Check: True show message 
	sm = False  #Observed StateMachine: True Show message
	plen = 16 
	zOffset = 0.0
	
	def __init__(self,port,zOffset = None):
		self.port = port
		self.zOffset =  0.0 if zOffset == None else zOffset
		print("(jb)Long range People Detect(LPD) lib initial")
		print("(jb)For Hardware:Batman-201(ISK)")
		print("(jb)Hardware: IWR-6843")
		print("(jb)Firmware: LPD 4.12.0")
		print("(jb)UART Baud Rate:921600")
		print("==============Info=================")
		print("Output: V6,V7,V8,V9 data:(RAW)")
		print("V6: Point Cloud Spherical")
		print("v6 structure: [(range,elevation,azimuth,doppler,x,y,z),......]")
		print("V7: Target Object List")
		print("V7 structure: [(tid,posX,posY,posZ,velX,velY,velZ,accX,accY,accZ,EC[16],g,confi),....]")
		print("V8: Target Index")
		print("V8 structure: [id1,id2....]")
		print("V9: Point Cloud Side Info")
		print("V9 [(snr,noise'),....]")
		print("===================================")
	 
		
	def useDebug(self,ft):
		self.dbg = ft
		
	def stateMachine(self,ft):
		self.sm = ft
		
	def getHeader(self):
		return self.hdr
		
	def headerShow(self):
		print("***Header***********") 
		print("Version:     \t%x "%(self.hdr.version))
		print("TotalPackLen:\t%d "%(self.hdr.totalPacketLen))
		print("Platform:    \t%X "%(self.hdr.platform))
		print("PID(frame#): \t%d "%(self.hdr.frameNumber))
		print("time cpu cycles: \t%d "%(self.hdr.timeCpuCycles))
		print("numDetectedObj:     \t%d "%(self.hdr.numDetectedObj))
		print("numTLVs:     \t%d "%(self.hdr.numTLVs))
		print("subframe#  : \t%d "%(self.hdr.subFrameNumber))
		print("***End Of Header***") 
		
	
			
	#for class internal use
	def tlvTypeInfo(self,dtype,count,dShow):
		sbyte = 8  #tlvHeader Struct = 8 bytes
		unitByte = 20 
		dataByte = 0
		pString = ""
		nString = "numOfPoints :"
		stateString = "V6"
		if dtype == 6:
			unitByte = 0   #pointUnit= 20bytes
			sbyte = 8      #tlvHeader Struct = 8 bytes
			dataByte= 16    #pointStruct 8bytes:(range,azimuth,elevation,doppler)
			pString = "Point Cloud Spherical TLV"
			nString = ""
			stateString = "V6"
		elif dtype == 7:
			unitByte = 0   #pointUnit= 0bytes 
			sbyte = 8 	   #tlvHeader Struct = 8 bytes
			dataByte = 112  #target struct bytes:(tid,posX,posY,posZ,velX,velY,velZ,accX,accY,accZ,ec[16],g,confidenceLevel)  11 * 4 + 16(ec) * 4 + 4(tid) = 112 
			pString = "Target Object List TLV"
			nString = "numOfObjects:"
			stateString = "V7"
		elif dtype == 8:
			unitByte = 0 #pointUnit= 0bytes 
			sbyte = 8    #tlvHeader Struct = 8 bytes
			dataByte = 1 #targetID = 1 byte
			pString = "Target Index TLV"
			nString = "numOfIDs"
			stateString = "V8"
		elif dtype == 9:
			unitByte = 0 #pointUnit= 0bytes 
			sbyte = 8    #tlvHeader Struct = 8 bytes
			dataByte = 4 #(snr,noise") =  4 byte
			pString = "Point Cloud Side Info"
			nString = "numOfIDs"
			stateString = "V9"
		else:
			unitByte = 0
			sbyte = 1
			pString = "*** Type Error ***"
			stateString = 'idle'
		 
		#retCnt = count - unitByte - sbyte
		nPoint = count / dataByte
		if dShow == True:
			print("-----[{:}] ----:{:}".format(pString,stateString))
			print("tlv Type({:2d}Bytes):  \t{:d}".format(sbyte,dtype))
			print("tlv length:      \t{:d}".format(count)) 
			print("num of point:    \t{:d}".format(int(nPoint)))
			print("value length:    \t{:d}".format(count))  
		
		return unitByte,stateString, sbyte, dataByte,count, int(nPoint)
		
#
# TLV: Type-Length-Value
# read TLV data
# input:
#     disp: True:print message
#			False: hide printing message
# output:(return parameter)
# (pass_fail, v6, v7, v8, v9)
#  pass_fail: True: Data available    False: Data not available
#
#  v6: DPIF point cloud Spherical infomation
#  v7: Target Object List information
#  v8: Target Index information
#  v9: DPIF Point Cloud Side Infomation
#
	def tlvRead(self,disp):
		#print("---tlvRead---")
		#ds = dos
		typeList = [6,7,8,9]
		idx = 0
		lstate = 'idle'
		sbuf = b""
		lenCount = 0
		unitByteCount = 0
		dataBytes = 0
		numOfPoints = 0
		tlvCount = 0
		pbyte = 16
		v6 = ([])
		v7 = ([])
		v8 = ([])
		v9 = ([])
	
		while True:
			try:
				ch = self.port.read()
			except:
				return (False,v6,v7,v8,v9)
			#print(str(ch))
			if lstate == 'idle':
				#print(self.magicWord)
				if ch == self.magicWord[idx]:
					#print("*** magicWord:"+ "{:02x}".format(ord(ch)) + ":" + str(idx))
					idx += 1
					if idx == 8:
						
						idx = 0
						lstate = 'header'
						rangeProfile = b""
						sbuf = b""
				else:
					#print("not: magicWord state:")
					idx = 0
					rangeProfile = b""
					return (False,v6,v7,v8,v9)
		
			elif lstate == 'header':
				sbuf += ch
				idx += 1
				if idx == 32: 
					#print("------header-----")
					#print(":".join("{:02x}".format(c) for c in sbuf)) 	 
					#print("len:{:d}".format(len(sbuf))) 
					# [header - Magicword]
					try: 
						(self.hdr.version,self.hdr.totalPacketLen,self.hdr.platform,
						self.hdr.frameNumber,self.hdr.timeCpuCycles,self.hdr.numDetectedObj,
						self.hdr.numTLVs,self.hdr.subFrameNumber) = struct.unpack('8I', sbuf)
						
					except:
						if self.dbg == True:
							print("(Header)Improper TLV structure found: ")
						return (False,v6,v7,v8,v9)
					
					if disp == True:  
						self.headerShow()
					
					tlvCount = self.hdr.numTLVs
					if self.hdr.numTLVs == 0:
						return (False,v6,v7,v8,v9)
						
					if self.sm == True:
						print("(Header)")
						
					sbuf = b""
					idx = 0
					lstate = 'TL'
					  
				elif idx > 48:
					idx = 0
					lstate = 'idle'
					return (False,v6,v7,v8,v9)
					
			elif lstate == 'TL': #TLV Header type/length
				sbuf += ch
				idx += 1
				if idx == 8:
					#print(":".join("{:02x}".format(c) for c in sbuf))
					try:
						ttype,self.tlvLength = struct.unpack('2I', sbuf)
						#print("(TL)numTLVs({:d}): tlvCount({:d})-------ttype:tlvLength:{:d}:{:d}".format(self.hdr.numTLVs,tlvCount,ttype,self.tlvLength))
						
						if ttype not in typeList or self.tlvLength > 10000:
							if self.dbg == True:
								print("(TL)Improper TL Length(hex):(T){:d} (L){:x} numTLVs:{:d}".format(ttype,self.tlvLength,self.hdr.numTLVs))
							sbuf = b""
							idx = 0
							lstate = 'idle'
							self.port.flushInput()
							return (False,v6,v7,v8,v9)
							
					except:
						print("TL unpack Improper Data Found:")
						if self.dbg == True:
							print("TL unpack Improper Data Found:")
						self.port.flushInput()
						return (False,v6,v7,v8,v9)
					
					
					unitByteCount,lstate ,plen ,dataBytes,lenCount, numOfPoints = self.tlvTypeInfo(ttype,self.tlvLength,disp)
					
					if self.sm == True:
						print("(TL:{:d})=>({:})".format(tlvCount,lstate))
						
					tlvCount -= 1
					idx = 0  
					sbuf = b""
			
			elif lstate == 'V6': # count = Total Lentgh - 8
				sbuf += ch
				idx += 1
				if (idx%dataBytes == 0):
					try:
						#print(":".join("{:02x}".format(c) for c in sbuf))
						(r,a,e,d) = struct.unpack('4f', sbuf)
						#print("({:2d}:{:4d})(idx:({:4d}) elv:{:.4f} azimuth:{:.4f} doppler:{:.4f} range:{:.4f}".format(numOfPoints,lenCount,idx,e,a,d,r))
						zt = r * np.sin(e) + self.zOffset 
						xt = r * np.cos(e) * np.sin(a)
						yt = r * np.cos(e) * np.cos(a)
						
						v6.append((r,a,e,d,xt,yt,zt))
						
						sbuf = b""
					except:
						if self.dbg == True:
							print("(6.1)Improper Type 6 Value structure found: ")
						return (False,v6,v7,v8,v9)
					
				if idx == lenCount:
					if disp == True:
						print("v6[{:d}]".format(len(v6)))
					idx = 0
					sbuf = b""
					if tlvCount <= 0: # Back to idle
						lstate = 'idle'
						if self.sm == True:
							print("(V6:tlvCnt={:d})=>(idle) :true".format(tlvCount))
						return (True,v6,v7,v8,v9)
						
					else: # Go to TL to get others type value
						lstate = 'TL' #'tlTL'
						if self.sm == True:
							print("(V6:tlvCnt={:d})=>(TL)".format(tlvCount))
					
				elif idx > lenCount:
					idx = 0
					sbuf = b""
					lstate = 'idle'
					return (False,v6,v7,v8,v9)
					
			elif lstate == 'V9':  
				sbuf += ch
				idx += 1
				if (idx%dataBytes == 0):
					try:
						#print(":".join("{:02x}".format(c) for c in sbuf))
						(snr,noise) =  struct.unpack('2h', sbuf)
						v9.append((snr,noise))
						sbuf = b""
					except:
						if self.dbg == True:
							print("(7)Improper Type 9 Value structure found: ")
						return (False,v6,v7,v8,v9)
				if idx >= lenCount:
					if disp == True:
						print("count= v9[{:d}]".format(len(v9)))
						
					sbuf = b""
					if tlvCount == 0:
						lstate = 'idle'
						if self.sm == True:
							print("(V9)=>(idle) :true")
						return (True,v6,v7,v8,v9)
					else: # Go to TL to get others type value
						lstate = 'TL'
						idx = 0
						if self.sm == True:
							print("(V9)=>(TL)")
							
				if idx > lenCount:
					idx = 0 
					lstate = 'idle'
					sbuf = b""
					return (False,v6,v7,v8,v9)
					
			elif lstate == 'V7':
				sbuf += ch
				idx += 1
				if (idx%dataBytes == 0):
					#print("V7:dataBytes({:d}) lenCount({:d}) index:{:d}".format(dataBytes,lenCount,idx))
					try:
						(tid,posX,posY,posZ,velX,velY,velZ,accX,accY,accZ,
						ec0,ec1,ec2,ec3,ec4,ec4,ec6,ec7,ec8,ec9,ec10,ec11,ec12,ec13,ec14,ec15,g,confidenceLevel) = struct.unpack('I27f', sbuf) 
						v7.append((tid,posX,posY,posZ,velX,velY,velZ,accX,accY,accZ,
						ec0,ec1,ec2,ec3,ec4,ec4,ec6,ec7,ec8,ec9,ec10,ec11,ec12,ec13,ec14,ec15,g,confidenceLevel))
						sbuf = b""
					except:
						if self.dbg == True:
							print("(7)Improper Type 7 Value structure found: ")
						return (False,v6,v7,v8,v9)
						
				if idx >= lenCount:
					if disp == True:
						print("v7[{:d}]".format(len(v7)))
					 
					sbuf = b""
					if tlvCount == 0:
						lstate = 'idle'
						if self.sm == True:
							print("(V7)=>(idle) :true")
						return (True,v6,v7,v8,v9)
						
					else: # Go to TL to get others type value
						lstate = 'TL'
						idx = 0
						if self.sm == True:
							print("(V7)=>(TL)")

				if idx > lenCount:
					idx = 0 
					lstate = 'idle'
					sbuf = b""
					return (False,v6,v7,v8,v9)
				
			elif lstate == 'V8':
				idx += 1
				v8.append(ord(ch))
				if idx == lenCount:
					if disp == True:
						print("=====V8 End====")
					sbuf = b""
					idx = 0
					lstate = 'idle'
					if self.sm == True:
						print("(V8:{:d})=>(idle)".format(tlvCount))
					return (True,v6,v7,v8,v9)
				
				if idx > lenCount:
					sbuf = b""
					idx = 0
					lstate = 'idle'
					return (False,v6,v7,v8,v9)




