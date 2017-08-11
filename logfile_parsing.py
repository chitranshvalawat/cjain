##################################################################
# FILE NAME: logfile_parsing.py
#
# PURPOSE: Parse the srio logs files and generate the csv file which
#          is containing pass/fail information of test case and also
#          calculate the number of pass and fail 
#
# AUTHOR: Chitransh Jain(chitransh.valawat@gmail.com)
#
# DATE: 10/08/2017
##################################################################

import csv

class Result:

    def __init__(self):
        self.total_count=0
        self.fail_count=0
        self.pass_count=0
    
    def det_pass_fail(self, filename):
        list1=filename.split(".",1)
        csv_filename=list1[0]+'.csv'
        GeneratedFile = open(csv_filename, 'w')
        GeneratedFile.write('\nS.N.')
        GeneratedFile.write(',Test Case')
        GeneratedFile.write(',Result')
        GeneratedFile.write('\n')
            
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        fail=0
        for line in lines:
            if line.find( "Test Case" )!= -1:
                #print(line)
                line = line.replace('\r','').replace('\n','')
                GeneratedFile.write(str(self.total_count+1))
                GeneratedFile.write(','+str(line))
                if fail != 0:
                    self.fail_count=self.fail_count+1
                    #print("Failed")
                    GeneratedFile.write(',Failed')
                else:
                    self.pass_count=self.pass_count+1
                    #print("Passed")
                    GeneratedFile.write(',Passed')

                self.total_count=self.total_count+1
                fail=0
                GeneratedFile.write('\n')
            
            if line.find( "Fail __X__" )!= -1:
                fail=fail+1
                
        GeneratedFile.write('\n\n,Total')
        GeneratedFile.write(','+str(self.total_count))
        GeneratedFile.write('\n,Pass')
        GeneratedFile.write(','+str(self.pass_count))
        GeneratedFile.write('\n,Fail')
        GeneratedFile.write(','+str(self.fail_count))

def main():
    log1=Result()
    log2=Result()
    log3=Result()
    
    log1.det_pass_fail("srio_test_app_log_mode0_VB0.txt")
    log2.det_pass_fail("srio_test_app_log_mode0_VB1.txt")
    log3.det_pass_fail("srio_test_app_log_mode0_VB2.txt")    

main()
