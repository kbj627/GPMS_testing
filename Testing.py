import pytest

if __name__ == "__main__":
    #pytest결과를 html형식 보고서로 출력한다.
    #실행을 위해서는 pip을 통해 pytest-html 설치가 필요하다.
    args = ['--html=report/report.html']
    
    pytest.main(args=args)