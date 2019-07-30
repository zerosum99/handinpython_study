import logging
log = logging.getLogger("log_doit")
log.setLevel(logging.DEBUG) 

def doIt():
    log.warning(" 함수 내부의 로깅을 처리")
    
    raise TypeError("doIt function : type error for testing")
    
if __name__ == "__main__" :
    print(" Main processing ")
    try :
        doIt()
    except TypeError as e:
        log.exception(e.args[0])
    log.warning(" 함수 내부의 로깅을 처리")