#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>


int infosum=0;

typedef struct{
	char *buf;
	int (*func)(const char *);
} message;

message *info[4];
int menu()
{
	int choice;
	puts("1.add info");
	puts("2.delete info");
	puts("3.show info");
	puts("4.exit");
	puts("choice:");
	scanf("%d",&choice);
	//getchar();
	if(choice<1||choice>4)
	{
		puts("wrong choice");
		exit(0);
	}	
	else
	{	
		return choice;
	}
}

void addInfo()
{
	int size;
	if(infosum>=4)
	{
		puts("too mucn info");
		return;
	}
	message *a=malloc(sizeof(message));	
	puts("input length");
	scanf("%d",&size);
	//getchar();
	a->buf=malloc(size);
	puts("input message");
	read(0,a->buf,size);
	a->func=&puts;
	(a->func)("your message is:");
	(a->func)(a->buf);
	info[infosum++]=a;
}

void delInfo()
{
	int index;
	puts("which info you want to delete");
	scanf("%d",&index);
	if(index<0||index>3||info[index]==0)
	{
		puts("wrong index");
		return;
	}
	char *temp=info[index]->buf;
	free(info[index]);
	free(temp);
	
}

void showInfo()
{
	int index;
        puts("which info you want to watch");
        scanf("%d",&index);
        if(index<0||index>3||info[index]==0)
        {
                puts("wrong index");
                return;
        }
	printf("info %d's message is ",index+1);
	(info[index]->func)(info[index]->buf);

}


int main()
{
	setvbuf(stdout, NULL, _IONBF, 0);
	int choice=3;
	puts("this is a simple info manage system");
	while(1)
	{
		choice=menu();
		switch(choice)
		{
			case 1: addInfo();
				break;
			case 2: delInfo();
				break;
			case 3: showInfo();
				break;
			case 4: exit(0);
				
		}
	}
	return 0;
}
