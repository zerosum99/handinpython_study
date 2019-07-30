import logging
log = logging.getLogger("log_doit")
log.setLevel(logging.DEBUG) 

def doIt():
    log.warning(" 함수 내부의 로깅을 처리")
    
    raise TypeError("doIt function : type error for testing")
        