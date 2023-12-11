def TowerofHanoi(n,s_pole,d_pole,i_pole):
    if n==1:
        print("Move Disc 1 From Pole",s_pole,"to pole",d_pole)
        return
    TowerofHanoi(n-1,s_pole,i_pole,d_pole)
    print("Move Disc",n,"from pole",s_pole,"to pole",d_pole)
    TowerofHanoi(n-1,i_pole,d_pole,s_pole)

n=3
TowerofHanoi(n,'A','C','B')
