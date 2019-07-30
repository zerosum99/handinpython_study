class UserError(Exception) :
    def __init__(self,err_no,err_pgm,err_msg) :
        super().__init__(err_msg)
        self.err_no = err_no
        self.err_pgm = err_pgm
        self.err_msg = err_msg