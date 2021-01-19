import EventHandler
import NetworkProcess
##You need to implement this class from scratch. It should inherit fromEventHandlerand have a constructor that takes aSenderinstance and aReceiverinstance.In thehandleEvent()function, it shall retrieve the messages from theSenderinstance, and deliver all of them to theReceiverinstance.
import internetApplication
#Now you need to write a program that creates an instance of each of the threeclassesSender,ReceiverandNetworkProcess.   Then,  each  of  these  classeshandleEvent()functions shall be called 100 times.  This shall lead to outputfrom theReceiveron a number (around 500-600) of delivered messages if youimplemented everything correctly.
import Receiver
##TheReceiver has a deliverMessage(message)function  that  takes  amessage  and  adds  it  to  a  list  of  delivered  messages.   TheReceiveralso  is  asubclass ofEventHandler.  ThehandleEvent()implementation inReceiverhandles the messages in the list and deletes them.
import Sender
##When theSender handleEvent()is called, a number of 1-10 messages shallbe  created  and  stored  in  a  list.   You  will  implement  this  function,  and  theSender retrieveMessages()member  function  that  returns  the  messages  inthe list, and empties the list.  When these have been implemented, the tests insenderTestshall pass.
import senderTest

import testReport


EventHandler()

