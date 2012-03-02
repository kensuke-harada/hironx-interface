# -*- coding:utf-8 -*-
import sys
if sys.platform[0:4] == 'java':
    class float_info:
        # Java の sys.float_info.epsilon は、Jython のマシンイプシロンとは異なるので、ここで求める 
        def get_epsilon(self):
            try:
                return self.eps
            except AttributeError:
                e = 1.0
                while (1.0 + e <> 1.0):
                    e /= 2.0
                self.eps = e
                return e
    
        epsilon = property(get_epsilon, None)
        
    sys.float_info = float_info()
    


    
    if __name__ == '__main__':
        print sys.float_info.epsilon
    
else:
    print 'warning: patch_jython do only on jython.'