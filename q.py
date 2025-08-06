class Queue:
    
    def __init__(self):
        self.cap=1
        self.data=self.cap * [None]
        self.size=0
        self.front=0
    
    def is_empty(self):
        return (self.size == 0)
    
    def dequeue(self):
        if(self.is_empty()):
            raise Exception('Queue is empty!')
        ans=self.data[self.front]
        self.data[self.front]=None
        self.front=(self.front+1)%self.cap
        self.size-=1
        return ans
    
    def enqueue(self, val):
        if self.size==self.cap:
            self.resize(2*self.cap)
        ind=(self.front+self.size)%self.cap
        self.data[ind]=val
        self.size+=1
    
    def resize(self, c):
        B=c*[None]
        for el in range(self.cap):
            B[el]=self.data[self.front]
            self.front=(self.front+1)%self.cap
        self.data=B
        self.front=0
        self.cap=c