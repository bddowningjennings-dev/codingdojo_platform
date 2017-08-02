from datetime import timedelta, datetime
from time import strftime

class Call(object):
  counter = 0
  def __init__(self, name, number, reason,):
    Call.counter += 1
    self.time = (datetime.utcnow() - timedelta(hours = 7)).strftime('%Y-%m-%d %H:%M:%S') 
    self.name = name.capitalize()
    self.number = str(number)
    self.reason = reason.lower()
    self.id = str(Call.counter) + '-' + self.name + '-' + self.number + '-' + self.time
  def display (self):
    print '---- Call (' + str(self.id) + ') details ----'
    # for attr, value in self.__dict__.iteritems():
    #   print attr.capitalize() + ":", value
    print "Name:", self.name
    print "Phone Number:", self.number
    print "Reason:", self.reason
    print "Time:", self.time
    return self

class CallCenter(object):
  def __init__(self,):
    self.calls = []
    self.queue_size = 0
  def add(self, call):
    # print "Added:"
    # call.display()
    self.calls.append(call)
    self.queue_size += 1
    return self
  def takeCall(self):
    if self.queue_size > 0:
      # print "Removed:"
      # self.calls[0].display()
      del self.calls[0]
      self.queue_size -= 1
    return self
  def removeCall(self, number):
    number = str(number)
    for call in self.calls:
      if call.number == number:
        self.calls.remove(call)
        self.queue_size -= 1
        return self
      else:
        print 'Phone number', number, 'not found\n'
    return self
  def sort(self):
    if self.queue_size > 0:
      indx = 0
      latest = self.calls[0]
      for j in range(0, self.queue_size):
        for i in range(0, self.queue_size - j):
          if self.calls[i].time > latest.time:
            latest = self.calls[i]
            indx = i 
        self.calls.remove(latest)
        self.calls.append(latest)
    else:
      print "No calls in queue."
    return self

  def info(self):
    print "Call center-- Queue length:", self.queue_size
    for call in self.calls:
      call.display()
    print "\n"

call_1 = Call('bob', 5555, 'farts')
call_2 = Call('sbob', '555-5644', 'fartest')

# call_1.display()

center_1 = CallCenter()
# call_2.time = 4
# call_1.time = 6
center_1.add(call_2).add(call_1).info()
# center_1.takeCall().info()
center_1.sort().info()
# center_1.removeCall(11).info()
# center_1.removeCall(5).info()
