    '''
    plenth = len(lenth())
    #print data
    
    if backData[0] == recive() : #if node is correct
      for x in range(1,16):   #check the nodes regarding to the system input
        
        if (backData[x]==recive1()):
          turn = backData[x+2] #access degree to turn
          print turn 

          while(270<=degrees<=359):   #set turning direction
            Hright()
            degrees =comread.degrees(comread.heading()) #update degrees
            print degrees
          while(0<=degrees <= (turn-5)):
            Hright()
            degrees =comread.degrees(comread.heading())
            print degrees
          while((turn+5)<=degrees<=269):
            Hleft()
            degrees =comread.degrees(comread.heading())
            print degrees 
          
      x=x+3

    elif backData[0]==recive1(): # second node 
      if plenth>2:  # if the recived path hass more than  2 nodes continue
        for x in range(1,16):
          if (backData[x]==recive2()):
            turn= backData[x+2]
            while(210<=degrees<=359):   #set turning direction
              Hright()
              degrees =comread.degrees(comread.heading()) #update degrees
              print degrees
            while(0<=degrees <= (turn-5)):
              Hright()
              degrees =comread.degrees(comread.heading())
              print degrees
            while((turn+5)<=degrees<=211):
              Hleft()
              degrees =comread.degrees(comread.heading())
              print degrees 

            
          x=x+3
    elif backData[0]==recive2(): # second node 
      if plenth>3:  # if the recived path hass more than  2 nodes continue
        for x in range(1,16):
          if (backData[x]==recive2()):
            turn= backData[x+2]
            while(210<=degrees<=359):   #set turning direction
              Hright()
              degrees =comread.degrees(comread.heading()) #update degrees
              print degrees
            while(0<=degrees <= (turn-5)):
              Hright()
              degrees =comread.degrees(comread.heading())
              print degrees
            while((turn+5)<=degrees<=211):
              Hleft()
              degrees =comread.degrees(comread.heading())
              print degrees 

            
          x=x+3
    elif backData[0]==recive3(): # second node 
      if plenth>4:  # if the recived path hass more than  2 nodes continue
        for x in range(1,16):
          if (backData[x]==recive2()):
            turn= backData[x+2]
            while(210<=degrees<=359):   #set turning direction
              Hright()
              degrees =comread.degrees(comread.heading()) #update degrees
              print degrees
            while(0<=degrees <= (turn-5)):
              Hright()
              degrees =comread.degrees(comread.heading())
              print degrees
            while((turn+5)<=degrees<=211):
              Hleft()
              degrees =comread.degrees(comread.heading())
              print degrees 

            
          x=x+3
      else:
        print("Arivved")  #if the recived path only has 2 nodes 
        hault()
      
    else:   # if recived node not match to the current node 
      print("node not match")
      Tcp_connect( '192.168.43.28', 17098) #send the node to the server
      if backData[0]==1 :
        Tcp_Write('a')
      elif backData[0]==2 :
        Tcp_Write('b')
      elif backData[0]==3 :
        Tcp_Write('c')
      elif backData[0]==4 :
        Tcp_Write('d')
      elif backData[0]==5 :
        Tcp_Write('e')
      elif backData[0]==6 :
        Tcp_Write('f')
      '''   
