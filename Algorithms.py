import time as t
runningProcess,processIndex,error,counter,answer,heat=[],[],0,0,' ',0
types ={
    'FIFO': 'FIFO',
    'LRU': 'LRU'
}
def algorythm(cell,processes,type=types['FIFO']):#Algorythms
    global runningProcess,processIndex,error,counter,answer,heat,file
    
    if (type==types['FIFO']):#if type FIFO follow the instructions below
      file=open("Algorithms_out_test.txt","a")
      file.write("\n\n\"FIFO\"\n")
      file.write("String/Cell \t ")
      for i in range(cell):
          file.write(str(i)+"   ")
      file.write(" Fault\n   \n")
      
      for i in processes:#checking each element of the processes board sent and filling it appropriately to runningProcess
          if i not in runningProcess:
              #if an element is not in the runningProcess memory and it is not full, add the appropriate element
              #if it is overloaded, replace it with the item that has been stored in runningProcess's memory the longest
              if len(runningProcess)<cell: runningProcess.append(i)
              else:
                  runningProcess[counter] = i
                  counter+=1
                  counter%=cell
              answer = str(i)
              error+=1
          else:
              answer = '-'
              heat+=1
          file.write('  {}\t\t'.format(i)+'\t\t ')
          for i in runningProcess:
              file.write(str(i)+'   ')
          for i in range(cell-len(runningProcess)):
              file.write('-  '+' ')
          file.write('   {}\n'.format(answer))
          t.sleep(1)
      del runningProcess[:]
      
      printAlgorythm(processes,error,heat)
      error,counter,heat=0,0,0
      file.close()

    if (type==types['LRU']):#algorythm LRU
       file=open("Algorithms_out_test.txt","a")
       file.write("\n\"LRU\"\n")
       file.write("String/Cell \t ")
       for i in range(cell):
          file.write(str(i)+"   ")
       file.write(" Fault\n   \n")
       
       for i in processes:
           if i not in runningProcess:
               #if an element is not in the runningProcess memory and it is not full, add the appropriate element
               #if it is overloaded, replace it with the item that has been stored in runningProcess's memory the oldest
               #processIndex is responsible for storing and exchanging runningProcess's indexes
               if len(runningProcess)<cell:
                   runningProcess.append(i)
                   processIndex.append(len(runningProcess)-1)
               else:
                   counter=processIndex.pop(0)
                   runningProcess[counter] = i
                   processIndex.append(counter)
               answer = str(i)
               error+=1
           else:
               index=processIndex.index(runningProcess.index(i))
               processIndex.append(processIndex.pop(index))
               answer = '-'
               heat+=1
           file.write('  {}\t\t'.format(i)+'\t\t ')
           for i in runningProcess:
               file.write(str(i)+'   ')
           for i in range(cell-len(runningProcess)):
               file.write('-  '+' ')
           file.write('   {}\n'.format(answer))
           t.sleep(1)
       del runningProcess[:]
       
       printAlgorythm(processes,error,heat)
       error,counter,heat=0,0,0
       file.close()
       
def printAlgorythm(processes,error,heat):#prints the final result
      p=round(((error/len(processes))*100),2)
      result='\nAll requests: {}'.format(len(processes))
      result+='\nAll page faults: {}'.format(error)
      result+='\nAll page heats: {}'.format(heat)
      result+='\nFault rate: {}%\n\n'.format(p)
      file.write(result)
