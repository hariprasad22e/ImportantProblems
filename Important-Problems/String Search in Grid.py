class Solution():
  def __init__(self,grid):
    self.grid=grid
    self.dir=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
    self.R=len(grid)
    self.C=len(grid[0])
  
  def search_dir(self,word,row,col):
    if self.grid[row][col]!=word[0]:
      return False
    
    for x,y in self.dir:
      rd=row+x
      cd=col+y
      flag=True
      for t in range (1,len(word)):
        if (0<=rd<self.R) and 0<=cd<self.C and (self.grid[rd][cd]==word[t]):
          rd=+x
          cd+=y
        else:
         flag=False
         break
      if flag:
        return True
    return False
        




  def search(self,word):
    for i in range(self.R):
      for j in range(self.C):
        if self.search_dir(word,i,j):
          print("Found at : {} , {}".format(i+1,j+1))


grid = ["GEEKSFORGEEKS","GEEKSQUIZGEEK","IDEQAPRACTICE"]
s1=Solution(grid)
s1.search("GEEKS")