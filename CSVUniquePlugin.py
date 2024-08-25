import sys
import numpy
import random
import PyPluMA

def is_number(s):
    try:
        float(s)
        return True
    except:
        return False

class CSVUniquePlugin:
   def input(self, filename):
      self.txtfile = open(filename, 'r')
      self.parameters = dict()
      for line in self.txtfile:
         contents = line.split('\t')
         self.parameters[contents[0]] = contents[1].strip()
      if len(PyPluMA.prefix()) != 0:
         self.parameters['csvfile'] = PyPluMA.prefix() + "/" + self.parameters['csvfile']

   def run(self):
      self.newlines = []
      column = self.parameters['column']
      csvfile = open(self.parameters['csvfile'], 'r')
      self.header = csvfile.readline().strip() # First line has the target column
      idx = self.header.split(',').index(column)
      self.results = set()
      for line in csvfile:
          contents = line.strip().split(',')
          self.results.add(contents[idx])

   def output(self, filename):
      filestuff2 = open(filename, 'w')
      mylen = len(self.results)
      count = 0
      for element in self.results:
          filestuff2.write(element)
          if (count < mylen-1):
             filestuff2.write("\n")
          count += 1

