#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#include <string.h> 

#define MAX_EXPRESSION_LENGTH 100

/**
 * parseNumber - Parses a number (integer or floating point) from the expression
 * @expr: The input expression
 * @index: The current position in the expression
 * 
 * Return: The parsed number
 */
double parseNumber(const char *expr, int *index);

/**
 * parseTerm - Parses a term (handles multiplication, division, and power)
 * @expr: The input expression
 * @index: The current position in the expression
 * 
 * Return: The parsed term
 */
double parseTerm(const char *expr, int *index);

/**
 * parseFactor - Parses a factor (handles numbers, parentheses, and scientific functions)
 * @expr: The input expression
 * @index: The current position in the expression
 * 
 * Return: The parsed factor
 */
double parseFactor(const char *expr, int *index);

/**
 * parseExpression - Parses an expression (handles addition and subtraction)
 * @expr: The input expression
 * 
 * Return: The parsed expression
 */
double parseExpression(const char *expr, int *index);

/**
 * skipSpaces - Skips spaces in the input expression
 * @expr: The input expression
 * @index: The current position in the expression
 */
void skipSpaces(const char *expr, int *index)
{
    while (isspace(expr[*index]))
    {
        (*index)++;
    }
}

/**
 * parseNumber - Parses a number (integer or floating point) from the expression
 * @expr: The input expression
 * @index: The current position in the expression
 * 
 * Return: The parsed number
 */
double parseNumber(const char *expr, int *index)
{
    double result = 0.0;
    double fraction = 1.0;
    int sign = 1;

    skipSpaces(expr, index);

    if (expr[*index] == '-')
    {
        sign = -1;
        (*index)++;
    }
    else if (expr[*index] == '+')
    {
        (*index)++;
    }

    while (isdigit(expr[*index]))
    {
        result = result * 10 + (expr[*index] - '0');
        (*index)++;
    }

    if (expr[*index] == '.')
    {
        (*index)++;
        while (isdigit(expr[*index]))
        {
            result = result * 10 + (expr[*index] - '0');
            fraction *= 10;
            (*index)++;
        }
    }

    result = sign * result / fraction;
    return result;
}

/**
 * parseFactor - Parses a factor (handles numbers, parentheses, and scientific functions)
 * @expr: The input expression
 * @index: The current position in the expression
 * 
 * Return: The parsed factor
 */
double parseFactor(const char *expr, int *index)
{
    double result = 0.0;
    char func[10];
    int funcIndex = 0;

    skipSpaces(expr, index);

    if (expr[*index] == '(')
    {
        (*index)++;
        result = parseExpression(expr, index);
        if (expr[*index] == ')')
        {
            (*index)++;
        }
        else
        {
            printf("Error: Missing closing parenthesis\n");
            exit(1);
        }
    }
    else if (isalpha(expr[*index]))
    {
        while (isalpha(expr[*index]) && funcIndex < 9)
        {
            func[funcIndex++] = expr[*index];
            (*index)++;
        }
        func[funcIndex] = '\0';

        if (expr[*index] == '(')
        {
            (*index)++;
            result = parseExpression(expr, index);
            if (expr[*index] == ')')
            {
                (*index)++;
            }
            else
            {
                printf("Error: Missing closing parenthesis\n");
                exit(1);
            }
        }
        if (strcmp(func, "sqrt") == 0)
        {
            result = sqrt(result);
        }
        else if (strcmp(func, "sin") == 0)
        {
            result = sin(result);
        }
        else if (strcmp(func, "cos") == 0)
        {
            result = cos(result);
        }
        else if (strcmp(func, "tan") == 0)
        {
            result = tan(result);
        }
        else if (strcmp(func, "log") == 0)
        {
            result = log(result);
        }
        else if (strcmp(func, "exp") == 0)
        {
            result = exp(result);
        }
        else
        {
            printf("Error: Unknown function %s\n", func);
            exit(1);
        }
    }
    else
    {
        result = parseNumber(expr, index);
    }

    return result;
}

/**
 * parseTerm - Parses a term (handles multiplication, division, and power)
 * @expr: The input expression
 * @index: The current position in the expression
 * 
 * Return: The parsed term
 */
double parseTerm(const char *expr, int *index)
{
    double result = parseFactor(expr, index);

    skipSpaces(expr, index);

    while (expr[*index] == '*' || expr[*index] == '/' || expr[*index] == '^')
    {
        char op = expr[*index];
        (*index)++;
        double operand = parseFactor(expr, index);

        if (op == '*')
        {
            result *= operand;
        }
        else if (op == '/')
        {
            if (operand != 0)
            {
                result /= operand;
            }
            else
            {
                printf("Error: Division by zero\n");
                exit(1);
            }
        }
        else if (op == '^')
        {
            result = pow(result, operand);
        }

        skipSpaces(expr, index);
    }

    return result;
}

/**
 * parseExpression - Parses an expression (handles addition and subtraction)
 * @expr: The input expression
 * @index: The current position in the expression
 * 
 * Return: The parsed expression
 */
double parseExpression(const char *expr, int *index)
{
    double result = parseTerm(expr, index);

    skipSpaces(expr, index);

    while (expr[*index] == '+' || expr[*index] == '-')
    {
        char op = expr[*index];
        (*index)++;
        double operand = parseTerm(expr, index);

        if (op == '+')
        {
            result += operand;
        }
        else if (op == '-')
        {
            result -= operand;
        }

        skipSpaces(expr, index);
    }

    return result;
}

/**
 * main - Entry point of the program
 * 
 * Return: Always 0 (Success)
 */
int main(void)
{
    char expression[MAX_EXPRESSION_LENGTH];
    int index = 0;

    printf("Enter an expression to evaluate (e.g., 2 + (3 * 4) - 5): ");
    fgets(expression, MAX_EXPRESSION_LENGTH, stdin);

    if (expression[strlen(expression) - 1] == '\n')
    {
        expression[strlen(expression) - 1] = '\0';
    }

    double result = parseExpression(expression, &index);
    printf("Result: %.2lf\n", result);

    return 0;
}
