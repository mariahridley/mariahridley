#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int my_strlen(char *str) {
  /* TODO #1:
   * Return the length of string str using the C convention of
   * being terminated by the NULL character.
   * Do not call any other functions whatsoever.
   * Even my_strlen -- no solutions involving recursion. */
  int counter = 0;
	while(*s != '\0')
	{
		counter++;
		s++;
	}
	return counter;
}

void str_reverse(char *str) {
  /* TODO #2:
   * Modify str to be the reverse string.
   * If str is "hello" when the function is called, then it
   * should be "olleh" when the function is completed.
   * The only function you can call is my_strlen.
   * Do not call malloc.  */
  int i;
	int len = strlen(str);
	for (i = 0; i < len; i++)
	{
		char keeper = str[len - 1];
		str[len-1] = str[i];
		str[i] = keeper;
		len--;
	}
}

int main(int argc, char *argv[]) {
  if (argc < 2) {
    printf("Usage: %s <string>\n", argv[0]);
    exit(EXIT_FAILURE);
  } else {
    // Attempt to reverse the string using your str_reverse function
    char *str = malloc(strlen(argv[1]) + 1);
    strcpy(str, argv[1]);
    str_reverse(str);
    printf("Original string: %s, reversed string: %s\n", argv[1], str);
    exit(EXIT_SUCCESS);
 }
}

int main()
{
char *str = malloc(strlen("hello world")+1);
    strcpy(str, "hello world");
    str_reverse(str);
    if (strcmp(str, "dlrow olleh") == 0)
    {
        printf("Congrats!  You have successfully reversed \"hello world\" to \"%s\"\n", str);
        exit(EXIT_SUCCESS);
    }
    else
    {
        printf("Project does not work yet.  You reversed \"hello world\" to \"%s\"\n", str);
        exit(EXIT_FAILURE);
    }
}