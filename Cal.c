#include <stdio.h>

void monstrous_calculator() {
    printf("Welcome to the Monstrous Calculator!\n");
    printf("I am MONSTER, your calculating companion.\n");

    while (1) {
        printf("\nChoose your monstrous operation:\n");
        printf("1. Add\n");
        printf("2. Subtract\n");
        printf("3. Multiply\n");
        printf("4. Divide\n");
        printf("5. Quit\n");

        char choice;
        printf("Enter the number of your choice: ");
        scanf(" %c", &choice);

        if (choice == '5') {
            printf("Farewell, mortal. MONSTER will haunt your calculations no more!\n");
            break;
        }

        if (choice < '1' || choice > '4') {
            printf("Invalid choice! MONSTER demands a proper selection.\n");
            continue;
        }

        double num1, num2;
        printf("Enter the first monstrous number: ");
        scanf("%lf", &num1);

        printf("Enter the second monstrous number: ");
        scanf("%lf", &num2);

        double result;
        switch (choice) {
            case '1':
                result = num1 + num2;
                break;
            case '2':
                result = num1 - num2;
                break;
            case '3':
                result = num1 * num2;
                break;
            case '4':
                if (num2 != 0) {
                    result = num1 / num2;
                } else {
                    printf("MONSTER doesn't divide by zero. Try again.\n");
                    continue;
                }
                break;
        }

        printf("The monstrous result is: %.2lf\n", result);
    }
}

int main() {
    monstrous_calculator();
    return 0;
}
