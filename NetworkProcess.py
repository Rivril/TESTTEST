# -*- coding: utf-8 -*-
from EventHandler import EventHandler

class NetworkProcess(EventHandler):

  def __init__(self, Sender, Receiver):
    self.sender = Sender
    self.messages = []
    self.receiver = Receiver

  def handleEvent(self):
    self.messages = self.sender.retrieveMessages()
    for element in self.messages:
      self.receiver.deliverMessage(element)
    Receiver = self.receiver
    return Receiver 


"""
TODO: Implement a NetworkProcess class

Use EventHandler as a base class (see Sender/ Receiver)

In the constructor (__init__ function) take a sender instance 
and a receiver instance.as arguments

Implement the handleEvent method to get messages from the sender and
deliver each message to the receiver.

"""