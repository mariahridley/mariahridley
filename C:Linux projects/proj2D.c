#include <stdio.h>
#include <stdlib.h>

typedef enum
{
   ADD,
   MULT,
   SUBTRACT,
   DIV,
   UNSUPPORTED
} MathOperation;

void IssueBadNumberError()
{
    printf("The string does not represent a floating point number.\n");
    exit(EXIT_FAILURE);
}

void IssueBadOperationError()
{
    printf("The string does not represent a valid operation.\n");
    exit(EXIT_FAILURE);
}

MathOperation GetOperation(char *op)
{
    if (op[0] == '+')
    {
        return ADD;
    }
    else if (op[0] == '-')
    {
        return SUBTRACT;
    }
    else if (op[0] == 'x')
    {
        return MULT;
    }
    else if (op[0] == '/')
    {
        return DIV;
    }
    else
    {
        return UNSUPPORTED;
    }
}

double StringToDouble(char *str)
{
    double result = 0.0;
    double dec_place = 1.0;
    int sign = 1;
    int decimal = 0;
    int i = 0;
    

    if (str[0] == '-')
    {
        sign = -1;
        i++;
    }

    while (str[i] != '\0'){
        if (str[i] == '.')
        {
            decimal = 1;
            i++;
            continue;
        }

        if (str[i] >= '0' && str[i] <= '9'){
            if (decimal){
                dec_place += 0.1;
                result += (str[i] - '0') * dec_place;
            } else {
                result = result * 10 + (str[i] - '0');
            }
        } else{
            IssueBadNumberError();
        }
        i++;
    }

    return sign * result;
}

int main(int argc, char *argv[])
{
    double v = StringToDouble(argv[1]);
    MathOperation op = GetOperation(argv[2]);
    double v2 = StringToDouble(argv[3]);
    double result = 0.0;
    switch (op)
    {
        case ADD:
            result = v + v2;
            break;
        case SUBTRACT:
            result = v - v2;
            break;
        case MULT:
            result = v * v2;
            break;
        case DIV:
            if (v2 == 0)
            {
                printf("Division by zero is not allowed.\n");
                return EXIT_FAILURE;
            }
            result = v / v2;
            break;
        case UNSUPPORTED:
            IssueBadOperationError();
            break;
    }

    printf("%d\n", (int)result);

    return 0;
}

