#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    float float_amount = 0;
    do
    {
        float_amount = get_float("Enter amount: ");
    }
    while(float_amount <= 0);

    int amount = round(float_amount * 100);
    int coin_counter = 0;

    while(amount >= 25)
    {
        amount -= 25;
        // printf("amount = %i\n", amount);
        coin_counter++;
    }
    // printf("# of quarters = %i\n", coin_counter);

    while(amount >= 10)
    {
        amount -= 10;
        coin_counter++;
    }

    while(amount >= 5)
    {
        amount -= 5;
        coin_counter++;
    }

    coin_counter += amount;

    printf("%i\n", coin_counter);

    /*
    while(amount >= 0)
    {
        amount -= 25;
        coin_counter++;
    }
    coin_counter--;
    amount += 25;

    while(amount >= 0)
    {
        amount -= 10;
        coin_counter++;
    }
    coin_counter--;
    amount += 10;

    while(amount >= 0)
    {
        amount -= 5;
        coin_counter++;
    }
    coin_counter--;
    amount += 5;

    coin_counter += amount;

    printf("%i\n", coin_counter);
    */
}