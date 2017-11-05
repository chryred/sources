# 해당 디렉토리의 모듈을 *를 이용하여 import 할때
# 해당 디렉토리의 __init__.py파일에
# __all__이라는 변수를 설정하고 import가능한 모듈을 정의하면
# 정의한 모듈을 import할 수 있다.

# from 패키지.패키지(폴더) import * (모듈)
# from 패키지.패키지.모듈 import * (여기서의 *는 모듈내에 있는 함수들을 지칭한다.)
version=1.0
__all__ = ['mylib'] # mylib모듈로 정의되어 있으면 mylib만 불러올 수 있다.