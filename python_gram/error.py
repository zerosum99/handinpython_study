import UserError as UE
try :
    raise UE.UserError(1,__name__,"장애가 발생했습니다.")
except UE.UserError as e :
    print(e.err_no)
    print(e.err_pgm)
    print(e.err_msg)