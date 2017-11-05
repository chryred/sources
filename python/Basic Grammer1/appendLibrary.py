'''[os 모듈]
   os.environ : 시스템의 환경 변수 값들을 보여준다.
   os.chdir : 현재 디레토리의 위치를 변경하는 함수
   os.getcwd : 자신의 현재 위치를 확인하는 함수
   os.system("명령어") : 시스템의 유틸리티나 dos명령어들을 파이썬에서 호출할 때 사용한다.
   os.popen : 시스템 명령어를 시킨 결과값을 읽기모드의 파일 객체로 돌려준다.
   
   * 기타 os 모듈의 유용한 함수들
   os.mkdir(디렉토리명) : 디렉토리를 생성한다.
   os.rmdir(디렉토리명) : 디렉토리를 삭제한다.(디렉토리가  비어 있어야 한다.)
   os.unlink(파일명) : 파일을 지운다.
   os.rename(src, dst) : src이름 파일을 dst파일명으로 변경한다.

   [shutil모듈] : 파일을 복사해 주는 모듈
   shutil.copy(src, dst) : src라는 이름으로 파일을 dst로 복사한다.
                                 1. dst가 디렉토리일 경우 src파일명으로 복사
								 2. src에 대한 동일 파일명이 존재할 경우 덮어쓴다.

   [glob모듈] : 디렉토리에 있는 파일들을 리스트로 만들 때 사용한다.

'''
import os
print(os.environ)
print(os.environ["PATH"])
#os.chdir("D:\\Lecture")
print(os.getcwd())
#os.system("dir/w")

#import shutil
#shutil.copy("dump.txt", "dump_copy.txt")

import glob
print(os.listdir(os.getcwd()))
print(glob.glob(os.getcwd() + "/*"))