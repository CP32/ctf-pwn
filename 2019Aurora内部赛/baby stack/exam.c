#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int FLAGSIZE=105;
char answersheet[200];
int point=300;
void backdoor(int a)
{
	char buf[FLAGSIZE];
	FILE *f = fopen("flag","r");
	if (f == NULL) 
	{
		printf("Flag File is Missing. Please contact an Admin if you are running this on the shell server.\n");
		exit(0);
	}
	if(a==30)
	{
		if(point==666)
		{
			fgets(buf,FLAGSIZE,f);
			puts(buf);
		}
		else
		{
			puts("Your points are too low. See you next year~");
		}
	}
	else
	{
		puts("you can't get in the backdoor");
	}
}

void readQuestion()
{
	puts("Q1:Give four examples of ecosystem\n");
	puts("Q2:Name the noble gas atom that has the same electron configuration as each of the ions in the following compounds.\n");
	puts("Q3:Consider an electron trapped in an infinite well whose width is 98.5pm .If it is in a state with n=15,what are (a)its energy(b)The uncertainty in its momentum(c)The uncertainty in its position.\n");
}

void writeAnswer()
{
	char draft[100];
	int length=0;
	int i;
	char choice;
	while(1)
	{
		puts("write on the draft paper:");
		length=read(0,draft,128);
		puts("copy this to the answer sheet?[Y/N]");
		scanf("%c",&choice);
		getchar();
		if(choice=='Y')
		{
			for(i=0;i<length;i++)
			{
				answersheet[i]=draft[i];
			}
			break;
		}
		else if (choice=='N')
		{
			continue;
		}
		else
		{
			puts("wrong input");
		}
	}
}

void askTeacher()
{
	char question[100];
	puts("What's your question?");
	read(0,question,100);
	printf("your question is : ");
	printf(question);
	printf(", right?\n");
	puts("wait a minute, I will go to ask another teacher");
}

void takeAnap()
{
	puts("zzzzzzzzz");
	sleep(150*60);
	puts("exam over");
}

int menu()
{
	int choice;
	puts("");
	puts("you can only do these in the exam or you will be considered to be cheating");
	puts("1.read the question");
	puts("2.write your answer");
	puts("3.ask the examiner");
	puts("4.sleep");
	puts("5.leave the room");
	puts("your choice:");
	scanf("%d",&choice);
	getchar();
	if(choice<1||choice>5)
	{
		puts("CHEAT! GET OUT!");
		exit(0);
	}	
	else
	{	
		return choice;
	}
}

int main()
{
	setvbuf(stdout, NULL, _IONBF, 0);
	int choice=0;
	puts("--------------------------------------------------------------------");
	puts("-------Welcome to the College Entrance Examination in 2019----------");
	puts("-------You forgot the Chinese exam and Math exam on yesterday-------");
	puts("-------It seems that you can't get into SHEN ZHEN UNIVERSITY--------");
	puts("-------Unless you get 500 points in this Science synthesis exam-----");
	puts("-------HA HA HA HA HA HA HA HA HA HA HA HA HA HA HA HA HA-----------");
	puts("-------Now the Science synthesis exam begin-------------------------");
	puts("--------------------------------------------------------------------");
	while(1)
	{
		choice=menu();
		switch(choice)
		{
			case 1: readQuestion();
				break;
			case 2: writeAnswer();
				break;
			case 3: askTeacher();
				break;
			case 4: takeAnap();
				break;
			case 5: exit(0);
				
		}
	}
	puts("see you next year~");
	return 0;
}
