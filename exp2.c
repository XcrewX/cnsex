#include<stdio.h>
#include<stdlib.h>
#include<string.h>
void main()
{
	char str[]="Hello World";
	char str1[11];
	char str2[11];
	char str3[11];
	int i,len;
	len = strlen(str);
	printf("The Plain Text: ");
	for (i=0;i<len;i++)
	{
		printf("%c", str[i]);
	}
	printf("\nCipher text after AND Operation: ");
	for(i=0;i<len;i++)
	{
		str1[i] = str[i]&127;
		printf("%c",str1[i]);
	}
	printf("\nCipher text XOR Operation: ");
	for(i=0;i<len;i++)
	{
		str3[i] = str[i]^127;
		printf("%c",str3[i]);
	}
	printf("\nCipher text OR Operation: ");
	for(i=0;i<len;i++)
	{
		str2[i] = str[i]|127;
		printf("%c",str2[i]);
	}
	printf("\n");
}

