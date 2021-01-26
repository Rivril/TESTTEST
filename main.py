import NetworkProcess
import Receiver
import Sender
import senderTest

"""
TODO: Implement an internet application program

Create instances of the Sender, Receiver and NetworkProcess classes

Create a loop, where the handleEvent functions of these instances are called
100 times 

"""

send = Sender.Sender() # Creates new instance of Sender class
receive = Receiver.Receiver() # Creates new instance of Receiver class
netpro = NetworkProcess.NetworkProcess(send, receive)

x = 0
while x < 100:

  send.handleEvent()
  netpro.handleEvent()
  receive.handleEvent()

  x += 1