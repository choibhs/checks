#include <stdio.h>
#include <cs50.h>

int main(void)
{
    float dollar = get_float("Enter asdf: ");
    printf("That response is valid");
    char letter = get_char("Enter asdf: ");
    printf("That is invalid");
    int num = get_int("Enter asdf: ");
    printf("That is invalid");
}