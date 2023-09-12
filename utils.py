class utils:
    def reversed(self,num):
        assert(isinstance(num, int))
        return int(str(num)[::-1])
    def formatter(self,num):
        assert(isinstance(num, int))
        return bin(num),oct(num)
        
        
