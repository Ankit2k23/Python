
"""
Approch:
First we will try to go at all boundry "O" element and if we will make all element visited 
and which is directly or indirectly connected with boundry "O" element.
Now we have visited matrix which tell us that which "O' position element is conneted with boundry "O".

Now we will check in mat  that the cell which is not visited and have value "O" . We will replace O wuth "X" 




"""



def dfs(i,j,Visited,mat,Row,Col,tempRow,tempCol):
    #make the cell visited
    Visited[i][j]=1
    
    for x in range(4):
        next_row=i+tempRow[x]
        next_col=j+tempCol[x]
        #base condition check
        #we call dfs only if condition satisfy and next cell is not visited as well as value is "O"
        if(next_row>=0 and next_row<Row and next_col>=0 and next_col<Col and (not Visited[next_row][next_col]) and mat[next_row][next_col]=='O'):
            dfs(next_row,next_col,Visited,mat,Row,Col,tempRow,tempCol)






def boundryElement_O(mat,Visited,Row,Col):
    #Traverse first Row nad Last Row for element "O"
    tempRow=[-1,0,1,0]
    tempCol=[0,1,0,-1]
    for j in range(Col):
        if( (not Visited[0][j]) and mat[0][j]=='O'):#recursive call for valid cell
            dfs(0,j,Visited,mat,Row,Col,tempRow,tempCol)
        if((not Visited[Row-1][j]) and mat[Row-1][j]=='O'):#recurr call for valid cell
            dfs(Row-1,j,Visited,mat,Row,Col,tempRow,tempCol)



    for i in range(Row):
        #Traverse first col and Last col for element "O"
        if( (not Visited[i][0]) and mat[i][0]=='O'):
            dfs(i,0,Visited,mat,Row,Col,tempRow,tempCol)
        if((not Visited[i][Col-1]) and mat[i][Col-1]=='O'):
            dfs(i,Col-1,Visited,mat,Row,Col,tempRow,tempCol)
    
    for i in range(Row):

        for j in range(Col):
            #if "O" not visited and present at pos mat[i][j]=='O' 
            #it means we have to reaplce with "X"
            if((not Visited[i][j]) and mat[i][j]=='O'):
                mat[i][j]='X'
        
    


if __name__ == '__main__':
    Row=int(input("Enter Your input for row :"))
    Col=int(input("Enter your input for column :"))
    """
    mat = [ [ 'X', 'O', 'X', 'O', 'X'  ],
			[ 'X', 'O', 'X', 'X', 'O'  ],
			[ 'X', 'X', 'X', 'O', 'X'  ],
			[ 'O', 'X', 'X', 'X', 'X'  ],
			[ 'X', 'X', 'X', 'O', 'X'  ]]
    
    """
    mat = [['0' for x in range(Row)] for y in range(Col)] 
    #for User Input
    for i in range(Row):
    
        for j in range(Col):
            ur_val=input()#Enter your value "X " or "O"  USER INPUT
            mat[i][j]=ur_val
    Visited=[[0 for i in range(Col)] for j in range(Row)]

    boundryElement_O(mat,Visited,Row,Col)
    for r in range(Row):

        for c in range(Col):
            print(f"{mat[r][c]} ",end=" ")
        print()


        
