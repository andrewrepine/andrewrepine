import random as rd
import math
class BubbleSort:

  def randomList(length, maxNum):
      if length < 1:
          return "Length below one, please try again."
      if maxNum < 1:
          return "Maximum number below minimum of one, please try again."
      added = 0
      arra = []
      while added <= length:
          randomadd = rd.randint(1, maxNum)
          arra.append(randomadd)
          added += 1
      return arra


  def swap(arr, index_1, index_2):
      if arr[index_1] > arr[index_2]:
          temp = arr[index_1]
          arr[index_1] = arr[index_2]
          arr[index_2] = temp


  def avg(list):
      count = 0
      for i in list:
          count += i
      return count / len(list)


  def bubbleSortString(arr):
      count = 0
      for el in range(len(arr)):
          print("{0} total swaps: {1}".format(count, arr))
          for i in range((len(arr) - 1 - el)):
              if arr[i] > arr[i + 1]:
                  BubbleSort.swap(arr, i, i + 1)
                  count += 1

      return "Sorted: {0}".format(arr)


  def bubbleSort(arr):
      count = 0
      for el in range(len(arr)):
          for i in range((len(arr) - 1 - el)):
              if arr[i] > arr[i + 1]:
                  BubbleSort.swap(arr, i, i + 1)
                  count += 1

      return arr


  def randomBubbleSort(length, maxNum, printList):
      arr = BubbleSort.randomList(length, maxNum)
      count = 0
      for el in range(len(arr)):
          if printList:
              print("{0} total swaps: ----------\n{1}".format(count, arr))
          else:
              print("{0} total swaps ----------".format(count))
          for i in range((len(arr) - 1 - el)):
              if arr[i] > arr[i + 1]:
                  BubbleSort.swap(arr, i, i + 1)
                  count += 1

      return "Sorted: {0}".format(arr)


  def countBubbleSort(length, maxNum):
      arr = BubbleSort.randomList(length, maxNum)
      swaps = 0
      for el in range(len(arr)):
          for i in range((len(arr) - 1 - el)):
              if arr[i] > arr[i + 1]:
                  BubbleSort.swap(arr, i, i + 1)
                  swaps += 1

      return swaps


  def bubbleTestList(testCount, length, maxNum):
      arr = []
      tests = 0
      while tests <= testCount:
          arr.append(BubbleSort.countBubbleSort(length, maxNum))
          tests += 1
      return "Using BubbleSort for {3} random lists with a length of {0} and max number of {1}:\n{2}".format(
          length, maxNum, arr, testCount)


  def bubbleTestAvg(testCount, length, maxNum):
      arr = []
      tests = 0
      while tests <= testCount:
          arr.append(BubbleSort.countBubbleSort(length, maxNum))
          tests += 1
      ave = round(BubbleSort.avg(arr), 2)
      return "The average swaps needed using BubbleSort for {3} random lists with a length of {0} and max number of {1}: {2}".format(
          length, maxNum, ave, testCount)


  def bubbleTestMaxMin(testCount, length, maxNum):
      print("----------------\nBUBBLE SORT TEST|\n----------------\n")
      arr = []
      tests = 0
      print("----------------\nStage 1 Starting|\n----------------")
      while tests <= testCount * .1:
          arr.append(BubbleSort.countBubbleSort(length, maxNum))
          tests += 1
      print("[10%]")
      while tests <= testCount * .2:
          arr.append(BubbleSort.countBubbleSort(length, maxNum))
          tests += 1
      print("[20%]")
      while tests <= testCount * .3:
          arr.append(BubbleSort.countBubbleSort(length, maxNum))
          tests += 1
      print("[30%]")
      while tests <= testCount * .4:
          arr.append(BubbleSort.countBubbleSort(length, maxNum))
          tests += 1
      print("[40%]")
      while tests <= testCount * .5:
          arr.append(BubbleSort.countBubbleSort(length, maxNum))
          tests += 1
      print("[50%]")
      while tests <= testCount * .6:
          arr.append(BubbleSort.countBubbleSort(length, maxNum))
          tests += 1
      print("[60%]")
      while tests <= testCount * .7:
          arr.append(BubbleSort.countBubbleSort(length, maxNum))
          tests += 1
      print("[70%]")
      while tests <= testCount * .8:
          arr.append(BubbleSort.countBubbleSort(length, maxNum))
          tests += 1
      print("[80%]")
      while tests <= testCount * .9:
          arr.append(BubbleSort.countBubbleSort(length, maxNum))
          tests += 1
      print("[90%]")
      while tests <= testCount:
          arr.append(BubbleSort.countBubbleSort(length, maxNum))
          tests += 1
      print("[100%]\n----------------\nStage 1 Complete|\n----------------\n")
      ave = round(BubbleSort.avg(arr), 2)
      print("----------------\nStage 2 Starting|\n----------------")
      arr1 = arr[:len(arr)//4]
      arr1.sort()
      print("[25%]")
      arr2 = arr[:len(arr)//2]
      arr2.sort()
      print("[50%]")
      arr3 = arr[:math.floor(len(arr)*.75)]
      arr3.sort()
      print("[75%]")
      arr4 = arr[math.floor(len(arr)*.75):]
      arr4.sort()
      sortArr = arr1 + arr2 + arr3 + arr4
      print("[100%]")
      print("----------------\nStage 2 Complete|\n----------------")
      max = sortArr[-1]
      min = sortArr[0]
      return "Using BubbleSort for {5} random lists with a length of {0} and max number of {1}:\nMax: {2}\nMin: {3}\nAvg: {4}".format(
          length, maxNum, max, min, ave, testCount)


  def bubbleTestMaxMinOptimized(testCount, length, maxNum):
      arr = []
      tests = 0
      print("Stage 1 Starting")
      while tests <= testCount:
          arr.append(BubbleSort.countBubbleSort(length, maxNum))
          tests += 1
      print("Stage 1 Complete")
      ave = round(BubbleSort.avg(arr), 2)
      print("Stage 2 Starting")
      sortArr = BubbleSort.bubbleSort(arr)
      print("Stage 2 Complete")
      max = sortArr[-1]
      min = sortArr[0]
      return "Using BubbleSort for {5} random lists with a length of {0} and max number of {1}:\nMax: {2}\nMin: {3}\nAvg: {4}".format(
          length, maxNum, max, min, ave, testCount)