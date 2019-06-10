#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<unistd.h>

int xor(char *code)
{
	char a=0;
	char b=0;
	for(int i=0;i<30;i+=2)
	{
		a^=code[i];
		b^=code[i+1];
	}
	if(a==b)
		return 1;
	else 
		return 0;
	
}

int main()
{
	setvbuf(stdout, NULL, _IONBF, 0);
	char buf[32];
	int result=0;
	puts("I'm wall facer Ray Diaz.");
	puts("I won't let you know what I want to do.");
	puts("Want to talk with me? OK,you will get nothing from me.");
	puts("What do you want to ask?");
	read(0,buf,30);
	if(strlen(buf)<30)
	{
		puts("What? Too short, I didn't get it");
		exit(0);
	}
	if(strchr(buf,0x90))
	{
		puts("You silent, want to observe my expression?");
		puts("I have said that, you will get nothing.");
		exit(0);
	}
	result=xor(buf);
	if(result==0)
		puts("What you said seems reasonable, but I don't care.");
	else
	{
		((void (*)(void))(buf))();
		
	}
	
	return 0;
}
