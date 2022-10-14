#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int player[5][5],ai[5][5];
void init(){
	for(int i=1;i<=3;i++){
		for(int j=1;j<=3;j++){
			player[i][j]=0;
			ai[i][j]=0;
		}
	}
}

bool check(){
	bool p=0,a=0;
	for(int i=1;i<=3;i++){
		for(int j=1;j<=3;j++){
			if(player[i][j]==0)p=1;
			if(ai[i][j]==0)a=1;
		}
	}
	if(p&&a)return true;
	else return false;
}

void player_move(int x){
	char c;
	cin>>c;
	int i;
	if(c=='K')i=1;
	else if(c=='E')i=2;
	else if(c=='X')i=3;
	else{
		printf("%c line does not exist,please input again:\n",c);
		player_move(x);
		return;
	}
	bool flag=0;
	for(int j=1;j<=3;j++){
		if(player[i][j]==0){
			flag=1;
			player[i][j]=x;
			for(int l=1;l<=3;l++){
				if(ai[i][l]==x)ai[i][l]=0;
			}
			break;
		}
	}
	if(!flag){
		printf("%c line is full,please input again:\n",c);
		player_move(x);
		return;
	}
}

void ai_move(int y){
	int i=rand()%3+1;
	bool flag=0;
	for(int j=1;j<=3;j++){
		if(ai[i][j]==0){
			flag=1;
			ai[i][j]=y;
			for(int l=1;l<=3;l++){
				if(player[i][l]==y)player[i][l]=0;
			}
			break;
		}
	}
	if(!flag){
		ai_move(y);
		return;
	}
	if(i==1)printf("the computer moves in K line\n");
	if(i==2)printf("the computer moves in E line\n");
	if(i==3)printf("the computer moves in X line\n");
}

int cnt[2][7];
bool fg[2][7];
bool win(){
	int ai_score=0;
	int player_score=0;
	for(int i=1;i<=3;i++){
		for(int x=1;x<=6;x++)cnt[0][x]=0,cnt[1][x]=0,fg[0][x]=0,fg[1][x]=0;
		for(int j=1;j<=3;j++){
			if(player[i][j]!=0)cnt[0][player[i][j]]++;
			if(ai[i][j]!=0)cnt[1][ai[i][j]]++;
		}
		for(int j=1;j<=3;j++){
			if(player[i][j]!=0){
				if(!fg[0][player[i][j]]){
					fg[0][player[i][j]]=1;
					player_score+=player[i][j]*pow(cnt[0][player[i][j]],2);
				}
			}
			if(ai[i][j]!=0){
				if(!fg[1][ai[i][j]]){
					fg[1][ai[i][j]]=1;
					ai_score+=ai[i][j]*pow(cnt[1][ai[i][j]],2);
				}
			}
		}
	}
	printf("your score is:%d\n",player_score);
	printf("computer score is:%d\n",ai_score);
	if(player_score>ai_score)return true;
	else return false;	
}

void show(){
	printf("player:\n");
	for(int i=1;i<=3;i++){
		for(int j=1;j<=3;j++){
			printf("%-6d",player[i][j]);
		}
		cout<<endl;
	}
	printf("computer:\n");
	for(int i=1;i<=3;i++){
		for(int j=1;j<=3;j++){
			printf("%-6d",ai[i][j]);
		}
		cout<<endl;
	}
}

int easy_num(){
	int a=rand()%3+3;
	int b=rand()%2;
	int x=a+b;
	return x;
}

int normal_num(){
	int x=rand()%6+1;
	return x;
}

int hard_num(){
	int a=rand()%2+1;
	int b=rand()%2;
	int c=rand()%2;
	int d=rand()%2;
	int x=a+b+c+d;
	return x;
}

void easy_mode(){
	int cnt=0;
	while(check()){
		cnt++;
		if(cnt&1){
			int x;
			if(cnt%3==0)x=normal_num();
			else x=easy_num();
			printf("the score you get is:%d\n",x);
			printf("please input the line you want to move:\n");
			player_move(x);
		}
		else{
			int y;
			if(cnt%4==0)y=normal_num();
			else y=hard_num();
			printf("the score computer get is:%d\n",y);
			ai_move(y);
		}
		show();
	}
}

void normal_mode(){
	int cnt=0;
	while(check()){
		cnt++;
		if(cnt&1){
			int x=normal_num();
			printf("the score you get is:%d\n",x);
			printf("please input the line you want to move:\n");
			player_move(x);
		}
		else{
			int y=normal_num();
			printf("the score computer get is:%d\n",y);
			ai_move(y);
		}
		show();
	}
}

void hard_mode(){
	int cnt=0;
	while(check()){
		cnt++;
		if(cnt&1){
			int x;
			if(cnt%3==0)x=normal_num();
			else x=hard_num();
			printf("the score you get is:%d\n",x);
			printf("please input the line you want to move:\n");
			player_move(x);
		}
		else{
			int y;
			if(cnt%4==0)y=normal_num();
			else y=hard_num();
			printf("the score computer get is:%d\n",y);
			ai_move(y);
		}
		show();
	}
}

void work(){
	init();
	srand((int)time(0));
	printf("easy:1\n");
	printf("normal:2\n");
	printf("hard:3\n");
	printf("please choose how hard you want to play:\n");
	int opt;
	cin>>opt;
	if(opt==1)easy_mode();
	if(opt==2)normal_mode();
	if(opt==3)hard_mode();
	if(win())printf("Congratulations!You win!!!\n");
	else printf("Sorry,You lose.\n");
}

int main(){
	work();
	return 0;
}
